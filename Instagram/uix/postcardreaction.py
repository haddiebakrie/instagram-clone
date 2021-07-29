from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty, StringProperty
Builder.load_string(
"""
<PostCardReaction>:
    size_hint_y: None
    height: '30dp'
    spacing: '5dp'

    ReactButton:
        text: root.likes
        icon: '\U0000E931'
    ReactButton:
        text: root.comments
        icon: '\U0000E922'
        md_bg_color: [0, 0, 0, 0]
    ReactButton:
        icon: '\U0000E94C'
        md_bg_color: [0, 0, 0, 0]
        padding: 0
    MDBoxLayout:
    MDIcon:
        icon: 'bookmark-outline'
        md_bg_color: [0, 0, 0, 0]
        size_hint: None, None
        size: self.texture_size
        text_color: [1, 1, 1, 1]
        theme_text_color: app.text_theme
        font_size: '17sp'
        pos_hint: {'center_y':.5}
"""
)

class PostCardReaction(MDBoxLayout):
    likes = StringProperty()
    comments = StringProperty()