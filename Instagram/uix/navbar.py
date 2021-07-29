from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string(
"""
<NavBar>:
    orientation: 'vertical'
    size_hint_y: None
    height: '70dp'
    radius: app.radius, app.radius, 0, 0
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        padding: '10dp', '5dp'
        spacing: '5dp'
        Iconly:
            icon: '\U0000E933'
            screen: 'home'
        Iconly:
            icon: '\U0000E94B'
            screen: 'search'
        Iconly:
            icon: '\U0000E948'
            screen: 'upload'
        Iconly:
            icon: '\U0000E931'
            screen: 'reaction'
        Iconly:
            icon: '\U0000E949'
            screen: 'profile'
    MDBoxLayout:
        size_hint_y: None
        height: '15dp'

"""
)

class NavBar(MDBoxLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            for widget in self.walk_reverse(loopback=True):
                if widget != self:
                    super().on_touch_down(touch)
                else:
                    return True
        else:
            return super().on_touch_down(touch)
