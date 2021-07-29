from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard

Builder.load_string(
"""
<RoundButton>:
    width: '55dp'
    size_hint_x: None
    elevation: 0
    md_bg_color: app.theme_cls.opposite_bg_normal
    radius: '10dp'
    text: ''
    ripple_behavior: True
    theme_text: 'Custom'
    MDLabel:
        theme_text_color: root.theme_text
        text_color: app.theme_cls.bg_normal
        halign: 'center'
        text: root.text
        font_size: '12sp'
"""
)


class RoundButton(MDCard):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return True
        else:
            return super().on_touch_down(touch)
        