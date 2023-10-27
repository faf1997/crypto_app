from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem

from system import System

from splashScreen import SplashScreen
from screenList import ScreenList
from screenConfig import ScreenConfig



class MyApp(MDApp):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        #theme_cls = ThemeManager()
        self.sys = System()
        self.sm = ScreenManager()
        self.sm.add_widget(SplashScreen())
        self.sm.add_widget(ScreenList())
        self.sm.add_widget(ScreenConfig())
        


    def build(self):
        return self.sm



if __name__ == '__main__':
    MyApp().run()