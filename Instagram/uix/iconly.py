from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty

Builder.load_string(
"""
<Iconly>:
    icon: ''
    orientation: 'vertical'
    icon_size: '20sp'
    icn: icn
    icon_align: 'center'
    default_size_hint: 1, 1
    default_size: self.size
    bold: False
    theme_mode: 'Primary'
    icon_color: [1, 1, 1, 1]
    font_style: 'Iconly'
    MDLabel:
        id: icn
        text: root.icon
        font_style: root.font_style
        font_size: root.icon_size
        halign: root.icon_align    
        size_hint: root.default_size_hint
        size: root.default_size
        bold: root.bold
        theme_text_color: root.theme_mode
        text_color: root.icon_color
"""
)


class Iconly(ButtonBehavior, MDBoxLayout):
    is_nav = BooleanProperty(defaultvalue=True)
    def on_press(self):
        if not self.is_nav:
            return
        self.icn.bold = not self.icn.bold
