from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from data import story as stories
from uix.story import Story
from kivy.core.window import Window


Builder.load_string(
"""
<StoryView>:
    bp: 5
    height: '95dp'
    padding: '5dp', '5dp', '5dp', self.bp
    size_hint_y: None
    ScrollView:
        do_scroll_y: False
        bar_width: 0
        MDBoxLayout:
            id: rbl
            adaptive_width: True
            spacing: '5dp'
            padding: '15dp', 0
            MDFloatLayout:
                orientation: 'vertical'
                size_hint: None, None
                size: '55dp', '75dp'
                MDCard:
                    size: '46dp', '46dp'
                    size_hint: None, None
                    elevation: 0
                    pos_hint: {'center_x':.5, 'top':1}
                    padding: '2dp'
                    radius: '20dp'
                    md_bg_color: [.5, .5, .5, .8]
                    MDCard:
                        size: '42dp', '42dp'
                        size_hint: None, None
                        elevation: 0
                        md_bg_color: [1, 1, 1, 1]
                        radius: '18dp'
                        padding: '1.5dp'

                        MDLabel:
                            radius: dp(18),
                            text: '+'
                            bold: True
                            font_size: '21sp'
                            halign: 'center'
                            md_bg_color: app.theme_cls.bg_normal
                            
                MDLabel:
                    text: 'My Story'
                    halign: 'center'   
                    height: self.texture_size[1]
                    size_hint_y: None
                    shorten_from: 'right'
                    shorten: True
                    font_size: '10sp'
                    bold: True
                    pos_hint: {'center_x':.5, 'top':.3}
    
"""
)

class StoryView(MDBoxLayout):
    storys = []
    def __init__(self, **kw):
        for story in stories:
            _storys = {
                'name':story['name'],
                'profile_pic':story['profile_pic'],
                'stories':story['stories'],
                'verified':story['verified'],
                'index':0,
            }
            self.storys.append(_storys)
        super().__init__(**kw)

    def on_kv_post(self, base_widget):
        for data in self.storys:
            story = Story()
            story.data = data
            self.ids.rbl.add_widget(story)
        return super().on_kv_post(base_widget)