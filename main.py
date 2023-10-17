from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem

from system import System

from screenList import ScreenList


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
    #theme_cls = ThemeManager()
        self.sys = System()
        self.sm = ScreenManager()
        self.sm.add_widget(ScreenList())


    def build(self):
        return self.sm



if __name__ == '__main__':
    MyApp().run()