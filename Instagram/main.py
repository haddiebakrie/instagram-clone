from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles
from kivy.core.window import Window
from kivy.clock import Clock
from functools import partial
from kivy.properties import ListProperty, NumericProperty, OptionProperty, StringProperty

Window.size = (310, 600)

from uix.uix import *
from screens.screens import *

class WindowManager(ScreenManager):
    pass

class Instagram(MDApp):
    radius = NumericProperty('25dp')
    spacing = NumericProperty('-52dp')
    bottom_pad = NumericProperty('20dp')
    bottom_push = NumericProperty('5dp')
    old_pad = NumericProperty(0)
    text_theme = OptionProperty('Custom', options=['Custom', 'Primary'])
    shadow = StringProperty('shadow.png')
    post_pad = ListProperty([0, 0, 0, 0])
    post_border = ListProperty([0, 0, 0, 0])
    prog_y = NumericProperty(.93)
    # post_detail_pad = ListProperty([0, 0, 0, 0])
    def build(self):
        self.wm = WindowManager(transition=NoTransition())
        self.gradient = 'assets/img/gradient.png'
        LabelBase.register(name='Iconly', fn_regular='Iconly-light.ttf', fn_bold='Iconly-Bold.ttf')
        theme_font_styles.append('Iconly')
        self.theme_cls.font_styles['Iconly'] = ['Iconly', 45, False, 0.15,]

        LabelBase.register(name='Scriptbl', fn_regular='CHRISTMAS AND SANTONA.TTF')
        theme_font_styles.append('Scriptbl')
        self.theme_cls.font_styles['Scriptbl'] = ['Scriptbl', 20, False, 0.15,]

        screens = [
            Home(name='home')
        ]

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm
    
    def show_post(self, data):
        if self.wm.has_screen('post'):
            return
        post = Post(name='post')
        post.data = data
        self.wm.add_widget(post)
        Clock.schedule_once(partial(self.goto, 'post'), .35)
    
    def show_story(self, data):
        if self.wm.has_screen('story'):
            return
        story = StoryScreen(name='story')
        story.data = data
        self.wm.add_widget(story)
        Clock.schedule_once(partial(self.goto, 'story'), .3)
    
    def close_post(self):
        current = self.wm.get_screen('post')
        self.wm.remove_widget(current)
        self.wm.current = 'home'

    def close_story(self):
        current = self.wm.get_screen('story')
        self.wm.remove_widget(current)
        self.wm.current = 'home'
    
    def goto(self, screen, dt):
        self.wm.current = screen
    
    def change_theme(self, switch):
        if switch == 'on':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def change_viz(self, viz_type):
        if viz_type == '1':
            self.radius = '25dp'
            self.spacing = '-52dp'
            self.bottom_pad = '20dp'
            self.shadow = 'shadow.png'
            self.post_pad = [0, 0, 0, 0]
            self.old_pad = 0
            self.bottom_push = 5
            self.text_theme = 'Custom'
            self.prog_y = .93
        elif viz_type == '2':
            self.radius = '10dp'
            self.spacing = '10dp'
            self.bottom_pad = 5
            self.shadow = ''
            self.old_pad = 0
            self.post_pad = ['5dp', '45dp', '5dp', '90dp']
            self.bottom_push = 70
            self.text_theme = 'Primary'
            self.prog_y = .1
        elif viz_type == '3':
            self.radius = '10dp'
            self.spacing = '10dp'
            self.bottom_pad = 5
            self.bottom_push = 70
            self.shadow = ''
            self.post_pad = ['5dp', '45dp', '5dp', '90dp']
            self.old_pad = '15dp'
            self.text_theme = 'Primary'
            self.prog_y = .1
        self.reload_imgs()
    
    def reload_imgs(self):
        for child in self.wm.screens[0].ids.rbl.children:
            child.reload()


def main():
    Instagram().run()


if __name__ == '__main__':
    main()