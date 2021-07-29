from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivymd.utils.fitimage import FitImage
from kivymd.uix.behaviors import RectangularElevationBehavior

Builder.load_string(
"""
<CarouselImage>:
    app: app
    car: carousel
    elevation: 0 if app.post_pad == [0, 0, 0, 0] else 12
    Carousel:
        id: carousel
        pos_hint: {'center_y':.5, 'center_x':.5}
    MDBoxLayout:
        id: pic_count
        size_hint_y: None
        pos_hint: {'top':app.prog_y, 'right':1}
        size: '50dp', '20dp'
        adaptive_width: True
        spacing: '5dp'
        padding: '20dp', 0
    MDCard:
        size_hint_x: None
        width: root.width * 0.3
        opacity: 0
        # on_release: carousel.load_next(mode='prev')
        on_release: root.prev_pic()
        pos_hint: {'x':0, 'center_y':.5}
    
    MDCard:
        size_hint_x: None
        width: root.width * 0.3
        opacity: 0
        pos_hint: {'right':1, 'center_y':.5}
        # on_release: carousel.load_next()
        on_release: root.next_pic()
        md_bg_color: [0, 0, 0, 1]

"""
)

class CarouselImage(RectangularElevationBehavior, MDFloatLayout):
    sources = ListProperty()
    img_count = NumericProperty()
    car = ObjectProperty()
    def on_kv_post(self, base_widget):
        Clock.schedule_once(self._add_images)
        Clock.schedule_once(self.update_prog)
        return super().on_kv_post(base_widget)

    def update_prog(self, dt=1, index=0):
        if self.img_count == 1:
            return
        self.ids.pic_count.clear_widgets()
        for i in range(self.img_count):
            if i == index:
                post_dot = MDBoxLayout(md_bg_color=[1, 1, 1, 1])
                post_dot.size_hint = (None, None)
                post_dot.pos_hint = {'center_y':.7}
                post_dot.size = '15dp', '5dp'
                post_dot.radius= '2dp'
            else:
                post_dot = MDBoxLayout(md_bg_color=[1, 1, 1, .7])
                post_dot.size_hint = (None, None)
                post_dot.pos_hint = {'center_y':.7}
                post_dot.size = '5dp', '5dp'
                post_dot.radius= '2dp'
            self.ids.pic_count.add_widget(post_dot)
        
    def next_pic(self):
        if self.ids.carousel.index+1 == self.img_count:
            return
        self.ids.carousel.load_next()
        self.update_prog(index=self.ids.carousel.index+1)
    
    def prev_pic(self):
        if self.ids.carousel.index == 0:
            return
        self.ids.carousel.load_next(mode='prev')
        self.update_prog(index=self.ids.carousel.index-1)

    def _add_images(self, dt):
        for src in self.sources:
            image = FitImage()
            image.source = src
            image.radius = self.app.radius,
            self.ids.carousel.add_widget(image)