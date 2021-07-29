from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.properties import OptionProperty
from kivy.clock import Clock

Builder.load_string(
"""
<VixToggle>:
    elevation: 0
    md_bg_color: [1, 1, 1, 0]
    text: ''
    font_size: '11sp'
    bold: True
    theme_mode: 'Custom'
    md_bg_color: [0, 0, 0, 0]
    elevation: 0
    icon_color: [1, 1, 1, 1]
    MDLabel:
        halign: 'right'
        text: root.text
        font_size: root.font_size
        bold: True
        theme_text_color: root.theme_mode
        text_color: root.icon_color
    MDFloatLayout:
        width: '50dp'
        size_hint_x: None
        MDBoxLayout:
            md_bg_color: [1, 1, 1, 1]
            size_hint: None, None
            size: '35dp', '18dp'
            radius: '8dp'
            pos_hint: {'center_x':.5, 'center_y':.45}
        MDIcon:
            id: tgl_icn
            icon: ''
            width: self.texture_size[0]
            size_hint_x: None
            font_size: '45sp'
            theme_text_color: root.theme_mode
            text_color: [.7, .7, .7, 1] if root.toggle_state == 'on' else [0, 0, 0, .9]
            pos_hint: {'center_x':.5, 'center_y':.5}

        
"""
)


class VixToggle(MDCard):
    toggle_state = OptionProperty('off', options=['on','off'])
    def on_kv_post(self, base_widget):
        Clock.schedule_once(self.set_toggle)
        return super().on_kv_post(base_widget)

    def set_toggle(self, dt):
        _toggle = {
            'on':'toggle-switch',
            'off':'toggle-switch-off'
        }

        self.ids.tgl_icn.__setattr__('icon', _toggle[self.toggle_state])

    def on_press(self):
        self.toggle()
        return super().on_press()

    def toggle(self):
        self.toggle_on() if self.toggle_state == 'off' else self.toggle_off()
    
    def toggle_on(self):
        self.ids.tgl_icn.icon = 'toggle-switch'
        self.toggle_state = 'on'
    
    def toggle_off(self):
        self.ids.tgl_icn.icon = 'toggle-switch-off'
        self.toggle_state = 'off'
