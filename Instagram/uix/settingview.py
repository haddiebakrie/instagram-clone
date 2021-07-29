from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.uix.modalview import ModalView
from kivy.properties import BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.behaviors import CompoundSelectionBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock


Builder.load_string(
"""
<SettingView>:
    size_hint_y: None
    orientation: 'vertical'
    radius: 0, 0, app.radius, app.radius
    height: self.height_value
    elevation: 0
    md_bg_color: [.2, .2, .2, .9]
    padding: '10dp', '25dp', '10dp', '5dp'
    MDLabel:
        halign: 'left'
        text: 'Visualization'
        font_size: '11sp'
        bold: True
        padding: '5dp', 0
        theme_text_color: 'Custom'
        text_color: [1, 1, 1, 1]
        size_hint_y: None
        height: self.texture_size[1]
    MDBoxLayout:
        SelectableBox:
            id: views
            size_hint_x: None
            width: root.width * 0.5
            VizButton:
                num: '1'
                text: 'Ample'
                select: [1, 1, 1, 1]
            VizButton:
                num: '2'
                text: 'Clean'
            VizButton:
                num: '3'
                text: 'Old'
        MDBoxLayout:
            id: toggles
            orientation: 'vertical'
            VixToggle:
                text: 'Horizontal'
            VixToggle:
                text: 'Swift chat'
            VixToggle:
                text: 'Dark Theme'
                on_release:
                    app.change_theme(self.toggle_state)
    Iconly:
        id: iconly
        icon: '\U0000E912'
        theme_mode: 'Custom'
        is_nav: False
        height: '20dp'
        size_hint_y: None
        icon_color: [1, 1, 1, 1]
        on_press:
            root.close_setting()

"""
)

class SettingView(MDCard):
    comments = ListProperty()
    pc = ObjectProperty()
    chevron_angle = NumericProperty()
    y_offset = NumericProperty(1.5)
    s = ObjectProperty()
    height_value = NumericProperty(defaultvalue=Window.height * 0.22)

    def open_setting(self):
        anim = Animation(y_offset=.91, d=.2)
        s_anim = Animation(bp=15, d=.2)
        s_anim.start(self.s)
        anim.start(self)
    def close_setting(self):
        anim = Animation(y_offset=1.5, d=.2)
        s_anim = Animation(bp=5, d=.2)
        s_anim.start(self.s)
        anim.start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            for widget in self.walk_reverse(loopback=True):
                if widget != self:
                    super().on_touch_down(touch)
                else:
                    return True
        else:
            return super().on_touch_down(touch)

class SelectableBox(CompoundSelectionBehavior, MDBoxLayout):
    def add_widget(self, widget):
        widget.bind(on_touch_down=self.button_touch_down,
                    on_touch_up=self.button_touch_up)
        return super().add_widget(widget)
    
    def button_touch_up(self, button, touch):
        if not self.collide_point(*touch.pos):
            return
        if not (button.collide_point(*touch.pos)):
            self.deselect_node(button)

    def button_touch_down(self, button, touch):
        if button.collide_point(*touch.pos):
            self.select_with_touch(button, touch)

    def select_node(self, node):
        node.select = [1, 1, 1, 1]
        return super().select_node(node)
    
    def deselect_node(self, node):
        node.select = [0, 0, 0, 0]
        return super().select_node(node)