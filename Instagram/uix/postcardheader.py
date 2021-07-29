from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import BooleanProperty, NumericProperty, StringProperty
from kivymd.uix.label import MDIcon
from kivy.clock import Clock

Builder.load_string(
"""
<PostCardHeader>:
    size_hint_y: None
    height: '35dp'
    spacing: '5dp'
    isize: '30dp', '30dp'
    FitImage:
        source: root.source
        size: root.isize
        size_hint: None, None
        radius: dp(12),
        pos_hint: {'center_y':.5}
        mipmap: True
    Label:
        text: root.text
        theme_text_color: app.text_theme
        color: app.theme_cls.opposite_bg_normal if self.theme_text_color == 'Primary' else [1, 1, 1, 1]
        bold: True
        font_size: '15sp'
        width: self.texture_size[0]
        size_hint_x: None
    MDIcon:
        icon: 'check-decagram' if root.verified else ''
        theme_text_color: app.text_theme
        text_color: [1, 1, 1, 1]
        font_size: '10sp'
"""
)

class PostCardHeader(MDBoxLayout):
    source = StringProperty()
    text = StringProperty()
    img_count = NumericProperty()
    index = NumericProperty()
    verified = BooleanProperty(defaultvalue=False)

    # def on_kv_post(self, base_widget):
    #     Clock.schedule_once(self.update_prog)
    #     super().on_kv_post(base_widget)
    
    