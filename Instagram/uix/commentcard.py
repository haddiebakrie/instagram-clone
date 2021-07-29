from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

Builder.load_string(
"""
<CommentCard>:
    size_hint_y: None
    height: '35dp'
    spacing: '5dp'
    padding: '10dp', 0
    elevation: 0
    md_bg_color: app.theme_cls.bg_normal
    FitImage:
        source: root.source
        size: '30dp', '35dp'
        size_hint: None, None
        radius: dp(12),
        pos_hint: {'center_y':.5}
        mipmap: True
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: root.name
            theme_text_color: 'Custom'
            text_color: [.5, .5, .5, .5]
            bold: True
            font_size: '12sp'
        MDLabel:
            text: root.text
            text_color: [1, 1, 1, 1]
            bold: True
            font_size: '12sp'
    MDBoxLayout:
        padding: '2.5dp'
        spacing: '5dp'
        adaptive_width: True
        RoundButton:
            text: 'Reply'
            md_bg_color: [.5, .5, .5, .1]
            theme_text: 'Primary'
        Iconly:
            icon: '\U0000E931'
            md_bg_color: [.5, .5, .5, .1]
            size_hint: None, None
            size: '30dp', '30dp'
            icon_size: '15sp'
            radius: '10dp'
"""
)

class CommentCard(MDCard):
    name = StringProperty()
    text = StringProperty()
    source = StringProperty()
    
    