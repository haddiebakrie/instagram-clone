from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import DictProperty
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string(
"""
<Story>:
    app: app
    orientation: 'vertical'
    size_hint: None, None
    size: '55dp', '75dp'
    radius: '20dp'
    elevation: 0
    MDCard:
        size: '50dp', '50dp'
        size_hint: None, None
        elevation: 0
        pos_hint: {'center_x':.5, 'top':1}
        background: app.gradient
        padding: '2dp'
        md_bg_color: [.9, .9, .9, 1]
        radius: root.radius
        MDCard:
            size: '46dp', '46dp'
            size_hint: None, None
            elevation: 0
            radius: '18dp'
            padding: '1.5dp'

            FitImage:
                source: root.data['profile_pic']
                size: self.parent.size[0]-3, self.parent.size[1]-3
                size_hint: None, None
                radius: dp(18),
                
    MDLabel:
        text: root.data['name']
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


class Story(ButtonBehavior, MDFloatLayout):
    data = DictProperty(defaultvalue={
        "profile_pic": "",
        "name": "",
        "stories": [""],
        "verified": False,
        "index": 0
    })

    def on_press(self):
        self.app.show_story(self.data)
        return super().on_press()