from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty

Builder.load_string(
"""
<VizButton>:
    text: ''
    num: '1'
    orientation: 'vertical'
    font_size: '11sp'
    icn: icn
    icon_align: 'center'
    bold: True
    theme_mode: 'Custom'
    md_bg_color: [0, 0, 0, 0]
    elevation: 0
    icon_color: [1, 1, 1, 1]
    padding: '5dp'
    select: [0, 0, 0, 0]
    on_press:
        app.change_viz(self.num)
    MDBoxLayout:
        elevation: 0
        md_bg_color: root.select
        radius: '15dp'
        padding: '1.5dp'
        MDLabel:
            text: root.num
            md_bg_color: [0, 0, 0, .4] if root.select == [0, 0, 0, 0] else [.4, .4, .5, .95]
            radius: '15dp'
            halign: 'center'
            theme_text_color: root.theme_mode
            text_color: root.icon_color
    MDLabel:
        id: icn
        text: root.text
        font_size: root.font_size
        halign: root.icon_align    
        theme_text_color: root.theme_mode
        text_color: root.icon_color
        height: self.texture_size[1]
        size_hint_y: None
        bold: root.bold
"""
)


class VizButton(MDCard):
    pass