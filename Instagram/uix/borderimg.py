from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_string(
"""
<BorderImg>:
    size: '20dp', '20dp'
    size_hint: None, None
    elevation: 0
    md_bg_color: [1, 1, 1, 1]
    radius: fitimage.radius
    padding: '1.5dp'
    source: ''

    FitImage:
        id: fitimage
        source: root.source
        size: self.parent.size[0]-1, self.parent.size[1]-1
        size_hint: None, None
        radius: dp(9),
        mipmap: True
        pos_hint: {'center_y':.5, 'center_x':.5}
"""
)


class BorderImg(MDFloatLayout):
    pass