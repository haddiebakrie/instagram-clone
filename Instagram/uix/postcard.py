from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.properties import BooleanProperty, DictProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivymd.utils.fitimage import FitImage
from kivy.uix.carousel import Carousel
from functools import partial

Builder.load_string(
"""
<PostCard>:
    app: app
    size_hint_y: None
    radius: app.radius
    app: app
    footer_alpha: 0
    spc: '20dp'
    elevation: 12 if app.post_pad == [0, 0, 0, 0] else 0
    pad: app.bottom_pad
    MDFloatLayout:
        MDCard:
            pos_hint: {'center_y':.5, 'center_x':.5}
            padding: app.post_pad
            radius: app.radius
            elevation: 0
            CarouselImage:
                id: post_img
                sources: root.data['post_pics']
                img_count: len(root.data['post_pics'])

        MDIcon:
            icon: 'dots-horizontal'
            pos_hint: {'top':.98, 'right':1}
            theme_text_color: app.text_theme
            padding: '20dp', 0
            size_hint: None, None
            size: self.texture_size
            text_color: [1, 1, 1, 1]
            opacity: 0 if app.prog_y == .93 else 1
            disabled: True if self.opacity == 0 else False
        MDCard:
            size_hint_x: None
            width: root.width * 0.40
            pos_hint: {'center_x':.5, 'center_y':.5}
            opacity: 0
            on_press: root.post_detail()
        MDBoxLayout:
            orientation: 'vertical'
            pos_hint: {'center_y':.5, 'center_x': .5}
            padding: root.pad
            PostCardHeader:
                id: post_head
                pos_hint: {'top':1}
                source: root.data['profile_pic']
                text: root.data['name']
                verified: root.data['verified']
                img_count: len(root.data['post_pics'])
                index: root.data['index']
            MDBoxLayout:
                orientation: 'vertical'
                spacing: root.spc
                # padding: 0, 0, 0, '10dp'
                PostCardReaction:
                    id: react
                    likes: root.data['likes']
                    comments: root.data['comments']
                PostCardFooter:
                    id: footer
                    # opacity: root.footer_alpha
                    reactors: root.data['reactors']
                    text: root.data['caption']
                    # disabled: True if root.footer_alpha == 0 else False
"""
)

class PostCard(MDCard):
    # profile_pic = StringProperty()
    # name = StringProperty()
    # caption = StringProperty()
    # likes = StringProperty()
    # comments = StringProperty()
    # post_pics = ListProperty([""])
    # comment = ListProperty([""])
    # reactors = ListProperty(["","",""])
    # verified = BooleanProperty()
    # index = NumericProperty(0)
    data = DictProperty(defaultvalue={
        "profile_pic": "",
        "name": "",
        "caption": "",
        "likes": "",
        "comments": "",
        "post_pics": [""],
        "comment": [""],
        "reactors": ["","",""],
        "verified": False,
        "index": 0
    })
    def on_kv_post(self, base_widget):
        Clock.schedule_once(self.load_images)
        return super().on_kv_post(base_widget)
        
    def post_detail(self):
        self.app.show_post(self.data)
    
    def load_images(self, dt):
        self.ids.post_img.sources = self.data['post_pics']            
        
    def reload(self):
        for child in self.ids.post_img.walk(restrict=True):
            if type(child) == FitImage:
                child.radius = self.app.radius, 
    
