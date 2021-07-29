from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from kivy.core.window import Window
from uix.postcard import PostCard
from kivy.animation import Animation
from kivy.clock import Clock


Builder.load_string(
"""
<Home>:
    app: app
    MDFloatLayout:
        md_bg_color: app.theme_cls.bg_normal
        MDBoxLayout:
            orientation: 'vertical'
            canvas.after:
                StencilPush
                Color:
                    rgba: app.theme_cls.bg_normal
                RoundedRectangle:
                    size: root.size[0], root.size[1]-35
                    pos: root.pos[0], root.pos[1]
                    radius: app.radius, app.radius, 0, 0
                StencilUse
                    func_op: 'greater'
                Rectangle:
                    size: root.size[0], root.size[1]-30
                    pos: root.pos[0], root.pos[1]
                StencilUnUse
                RoundedRectangle:
                    size: root.size[0], root.size[1]-35
                    radius: app.radius, app.radius, 0, 0
                    pos: root.pos[0], root.pos[1]
                StencilPop
                
            MDBoxLayout:
                orientation: 'vertical'
                # radius: 30, 30, 0, 0
                padding: 0, 35, 0, 0
                ScrollView:
                    do_scroll_x: False
                    MDBoxLayout:
                        orientation: 'vertical'
                        adaptive_height: True
                        padding: 0, 0, 0, app.bottom_pad
                        StoryView:
                            id: sty_view
                        MDBoxLayout:
                            id: rbl
                            padding: app.old_pad, 0, app.old_pad, app.bottom_push
                            orientation: 'vertical'
                            adaptive_height: True
                            spacing: app.spacing
            
        TopBar:
            type: 'home'
            pos_hint: {'center_x':.5, 'top':1}
            setting: setting
        NavBar:
            pos_hint: {'center_x':.5, 'y':0}
            md_bg_color: app.theme_cls.bg_normal
        SettingView:
            id: setting
            pos_hint: {'center_x':.5, 'center_y':self.y_offset}
            s:sty_view

"""
)

class Home(Screen):
    data = []
    def __init__(self, **kw):
        for profile in users:
            _data = {
                'name':profile['name'],
                'caption':profile['caption'],
                'profile_pic':profile['profile_pic'],
                'likes':profile['likes'],
                'comments':profile['comments'],
                'post_pics':profile['post_pics'],
                "comment":profile['comment'],
                "reactors":profile['reactors'],
                'verified':profile['verified'],
                'index':0,       
            }
            self.data.append(_data)
        super().__init__(**kw)
    
    def on_kv_post(self, base_widget):
        for data in self.data:
            post_card = PostCard()
            post_card.height = Window.height * 0.6
            post_card.data = data
            self.ids.rbl.add_widget(post_card)
        return super().on_kv_post(base_widget)