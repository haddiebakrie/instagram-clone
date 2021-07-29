from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard

Builder.load_string(
"""
<ReactButton>:
    width: '55dp'
    padding: '5dp'
    size_hint_x: None
    elevation: 0
    spacing: '2dp'
    md_bg_color: [.5, .5, .5, .7]
    radius: '12dp'
    icon_bold: True
    text: ''
    icon: ''
    
    MDIcon:
        text: root.icon
        font_style: 'Iconly'
        size_hint_x: None
        size: self.texture_size
        font_size: '15sp'
        bold: root.icon_bold
        theme_text_color: app.text_theme
        text_color: [1, 1, 1, 1]
    MDLabel:
        halign: 'center'
        text: root.text
        font_size: '9sp'
        bold: True
        theme_text_color: app.text_theme
        text_color: [1, 1, 1, 1]
"""
)


class ReactButton(MDCard):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return True
        else:
            return super().on_touch_down(touch)
        