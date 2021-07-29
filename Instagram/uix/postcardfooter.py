from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivymd.uix.label import MDIcon
from uix.borderimg import BorderImg
from kivy.uix.widget import Widget
from kivy.clock import Clock

Builder.load_string(
"""
<PostCardFooter>:
    size_hint_y: None
    height: '25dp'
    spacing: '10dp'
    MDGridLayout:
        id: pic_count
        adaptive_width: True
        spacing: '-8dp'
        rows: 1
        orientation: 'rl-tb'
    MDLabel:
        text: root.text
        theme_text_color: app.text_theme
        text_color: [1, 1, 1, 1]
        bold: True
        font_size: '12sp'
        shorten_from: 'right'
        shorten: True
    RoundButton:
        text: 'More'
"""
)

class PostCardFooter(MDBoxLayout):
    reactors = ListProperty()
    text = StringProperty()
    def on_kv_post(self, base_widget):
        
        Clock.schedule_once(self.load_data)
        return super().on_kv_post(base_widget)
    
    def load_data(self, dt):
        for i in range(3):
            reactors = BorderImg()
            reactors.source = self.reactors[i]
            self.ids.pic_count.add_widget(reactors)