from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.uix.modalview import ModalView
from kivy.properties import BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.animation import Animation
from uix.commentcard import CommentCard


Builder.load_string(
"""
<CommentView>:
    app: app
    comment: comment
    size_hint_y: None
    orientation: 'vertical'
    radius: '30dp'
    height: self.height_value
    elevation: 0
    md_bg_color: app.theme_cls.bg_normal
    FloatLayout:
        size_hint: 1, None
        height: '20dp'
        Iconly:
            id: iconly
            icon: '\U0000E912'
            theme_mode: 'Custom'
            is_nav: False
            icon_color: app.theme_cls.opposite_bg_normal
            pos_hint: {'y':root.y_offset}
            on_press:
                root.open()
            canvas.before:
                PushMatrix
                Rotate: 
                    angle: root.chevron_angle
                    origin: self.center
            canvas.after:
                PopMatrix

    ScrollView:
        MDBoxLayout:
            id: comment
            orientation: 'vertical'
            adaptive_height: True
            spacing: '15dp'
"""
)

class CommentView(MDCard):
    comments = ListProperty()
    pc = ObjectProperty()
    chevron_angle = NumericProperty()
    y_offset = NumericProperty()
    height_value = NumericProperty(defaultvalue=Window.height * 0.35)

    def open_comment(self):
        self.ids.iconly.icon_color = [1, 1, 1, 1] if self.app.post_pad == [0, 0, 0, 0] else self.app.theme_cls.opposite_bg_normal
        anim = Animation(y_offset=1, chevron_angle=180, height_value=Window.height * 0.92, d=.1)
        pc_anim = Animation(pad=30, d=.2)
        pc_anim.start(self.pc)
        anim.start(self)
    def close_comment(self):
        self.ids.iconly.icon_color = [0, 0, 0, 1]if self.app.post_pad == [0, 0, 0, 0] else self.app.theme_cls.opposite_bg_normal
        anim = Animation(y_offset=0, chevron_angle=0, height_value=Window.height * 0.35, d=.1)
        pc_anim = Animation(pad=self.app.bottom_pad, d=.2)
        pc_anim.start(self.pc)
        anim.start(self)
    def open(self):
        if self.height_value == Window.height * 0.35:
            self.open_comment()
        else:
            self.close_comment()
    
    def load_comments(self, comments):
        for comment in comments:
            comment_card = CommentCard()
            comment_card.name = comment['name']
            comment_card.text = comment['comment']
            comment_card.source = comment['profile_pic']
            self.ids.comment.add_widget(comment_card)
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            for widget in self.walk_reverse(loopback=True):
                if widget != self:
                    super().on_touch_down(touch)
                else:
                    return True
        else:
            return super().on_touch_down(touch)
