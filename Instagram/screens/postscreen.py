from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from kivy.core.window import Window
from uix.postcard import PostCard
from kivy.properties import DictProperty
from kivy.animation import Animation
from kivy.clock import Clock
from uix.commentcard import CommentCard

Builder.load_string(
"""
<Post>:
    MDFloatLayout:
        md_bg_color: app.theme_cls.bg_normal
        MDBoxLayout:
            id: det
            orientation: 'vertical'
            pos_hint: {'center_x':.5, 'top':1}
            spacing: '5dp'
            MDBoxLayout:
                size_hint_y: None
                height: '30dp'
                padding: '15dp', 0
                Iconly:
                    icon: '\U0000E908'
                    icon_align: 'left'
                    on_release: app.close_post()
                MDBoxLayout:
                MDIcon:
                    icon: 'dots-horizontal'
                    halign: 'right'
                    font_size: '20sp'
            MDBoxLayout:
                padding: app.old_pad, 0
                size_hint_y: None
                height: pc.height
                PostCard:
                    id: pc
                    data: root.data
                    height: root.height * 0.6
                    footer_alpha: 1
                    spc: '10dp'
                    shadow: ''
            MDBoxLayout:
                CommentView:
                    id: comments
                    padding: 0, 50, 0, 0
                    pc: pc
        MDCard:
            md_bg_color: app.theme_cls.bg_normal
            height: '60dp'
            size_hint_y: None
            radius: app.radius, app.radius, 0, 0
            padding: '10dp'
            CommentField:

"""
)

class Post(Screen):
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
        Clock.schedule_once(self.animate_all)
        return super().on_kv_post(base_widget)
    
    def animate_all(self, dt):
        self.ids.comments.load_comments(self.data['comment'])
        anim = Animation(spacing=0, d=.1)
        c_anim = Animation(padding=[0, 0, 0, 0], d=.1)
        anim.start(self.ids.det)
        c_anim.start(self.ids.comments)

