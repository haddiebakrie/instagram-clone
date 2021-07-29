from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

Builder.load_string(
"""
<CommentField>:
    size_hint_y: None
    height: '40dp'
    spacing: '5dp'
    padding: '5dp',
    radius: '15dp'
    elevation: 0
    md_bg_color: [.5, .5, .5, .1]
    FitImage:
        source: root.source
        width: '30dp'
        size_hint_x: None
        radius: dp(12),
        pos_hint: {'center_y':.5}
        mipmap: True
    TextInput:
        height: '35dp'
        # size_hint_y: None
        background_color: [0, 0, 0, 0]
        cursor_color: [0, 0, 0, 1]
        multiline: False
        font_size: '15dp'
        foreground_color: [0, 0, 0, 1]
        hint_text: 'Add comment'
        pos_hint: {'center_y':.5}
    Iconly:
        icon: '\U0000E94C'
        size_hint_x: None
        size: '30dp', '30dp'
        icon_size: '15sp'
        radius: '10dp'
        bold: True
        canvas.before:
            PushMatrix
            Rotate: 
                angle: -45
                origin: self.center
        canvas.after:
            PopMatrix

"""
)

class CommentField(MDCard):
    source = StringProperty('assets/img/wiz1.jfif')
    