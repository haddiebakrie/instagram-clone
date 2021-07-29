from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from kivy.core.window import Window
from uix.postcard import PostCard
from kivy.properties import DictProperty, NumericProperty
from kivy.animation import Animation
from kivy.clock import Clock
from kivymd.utils.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.carousel import Carousel

Builder.load_string(
"""
<StoryScreen>:
    app: app
    MDFloatLayout:
        md_bg_color: app.theme_cls.bg_normal
        Carousel:
            id: carousel
            scroll_timeout: 0
            anim_move_duration: .1
            pos_hint: {'center_y':.5, 'center_x':.5}
        MDCard:
            size_hint_x: None
            width: root.width * 0.3
            opacity: 0
            on_release: root.prev_pic()
            pos_hint: {'x':0, 'center_y':.5}
    
        MDCard:
            size_hint_x: None
            width: root.width * 0.3
            opacity: 0
            pos_hint: {'right':1, 'center_y':.5}
            on_release: root.next_pic()
            md_bg_color: [0, 0, 0, 1]
        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp', '5dp', '20dp', '20dp'
            spacing: '10dp'
            MDBoxLayout:
                id: story_count
                size_hint_y: None
                spacing: '5dp'
                height: '10dp'
            PostCardHeader:
                text: root.data['name']
                source: root.data['profile_pic']
                isize: '25dp', '25dp'
                Iconly: 
                    icon: '\U0000E923'
                    size_hint: None, None
                    size: '20dp', '20dp'
                    radius: '7dp'
                    md_bg_color: [.2, .2, .2, .8]
                    theme_mode: 'Custom'
                    icon_color: [1, 1, 1, 1]
                    pos_hint: {'center_y':.5}
                    on_press: app.close_story()
            MDBoxLayout:
            MDBoxLayout:
                size_hint_y: None
                height: '40dp'
                spacing: '15dp'
                MDBoxLayout:
                    size_hint_y: None
                    height: '40dp'
                    spacing: '10dp'
                    radius: '15dp'
                    padding: '10dp'
                    md_bg_color: [.2, .2, .2, .9]
                    TextInput:
                        background_color: [0, 0, 0, 0]
                        cursor_color: [1, 1, 1, 1]
                        multiline: False
                        font_size: '15dp'
                        foreground_color: [1, 1, 1, 1]
                        hint_text_color: [1, 1, 1, 1]
                        hint_text: 'Send Message'
                        bold: True
                        pos_hint: {'center_y':.5}
                        padding: 0
                    MDSeparator:
                        orientation: 'vertical'
                        md_bg_color: [1, 1, 1, 1]
                    FitImage:
                        source: 'emoji.png'
                        size_hint: None, None
                        size: '20dp', '20dp'
                        pos_hint: {'center_y':.5}

                Iconly: 
                    icon: '\U0000E94C'
                    size_hint: None, None
                    size: '35dp', '35dp'
                    radius: '12dp'
                    md_bg_color: [.2, .2, .2, .8]
                    theme_mode: 'Custom'
                    icon_color: [1, 1, 1, 1]
                    pos_hint: {'center_y':.5}
                    icon_size: '15sp'
                    bold: True
        
"""
)

class StoryScreen(Screen):
    data = DictProperty(defaultvalue={
        "profile_pic": "",
        "name": "",
        "caption": "",
        "stories": [""],
        "verified": False,
        "index": 0
    })
    img_count = NumericProperty()
    def on_kv_post(self, base_widget):
        Clock.schedule_once(self._add_images)
        Clock.schedule_once(self.update_prog)
        return super().on_kv_post(base_widget)

    def _add_images(self, dt):
        for src in self.data['stories']:
            self.img_count += 1
            image = FitImage()
            image.source = src
            self.ids.carousel.add_widget(image)
        print(self.img_count)
        
    def update_prog(self, dt=1, index=0):
        if self.img_count == 1:
            return
        self.ids.story_count.clear_widgets()
        for i in range(self.img_count):
            if i == index:
                story_dot = MDBoxLayout(md_bg_color=[1, 1, 1, 1])
                story_dot.size_hint_y = None
                story_dot.pos_hint = {'center_y':.5}
                story_dot.size = '15dp', '3dp'
                story_dot.radius= '2dp'
            else:
                story_dot = MDBoxLayout(md_bg_color=[1, 1, 1, .5])
                story_dot.size_hint_y = None
                story_dot.pos_hint = {'center_y':.5}
                story_dot.size = '5dp', '3dp'
                story_dot.radius= '2dp'
            self.ids.story_count.add_widget(story_dot)

    def next_pic(self):
        if self.ids.carousel.index+1 == self.img_count:
            return
        self.ids.carousel.load_next()
        self.update_prog(index=self.ids.carousel.index+1)
    
    def prev_pic(self):
        if self.ids.carousel.index == 0:
            return
        self.ids.carousel.load_next(mode='prev')
        self.update_prog(index=self.ids.carousel.index-1)
