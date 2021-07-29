from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty

Builder.load_string(
"""
<TopBar>:
    type: 'home'
    size_hint_y: None
    height: '30dp'
    padding: '20dp', '5dp'
    md_bg_color: app.theme_cls.bg_normal
    Iconly:
        icon: '\U0000E94D'
        icon_align: 'left'
        is_nav: False
        on_press: 
            root.open_setting()
    MDLabel:
        font_style: 'Scriptbl' 
        text: 'Instagram' if root.type == 'home' else ''
        bold: True
        halign: 'center'
    MDIcon:
        icon: 'email-outline'
        halign: 'right'
        font_size: '20sp'
        
"""
)

class TopBar(MDBoxLayout):
    setting = ObjectProperty()
    def open_setting(self):
        self.setting.open_setting()