from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screenmanager import ScreenManager
#from kivymd.uix.list import TwoLineListItem
#from kivymd.theming import ThemeManager

from system import System
from custom_widgets.screens import SCREENS
from custom_widgets import THEME_COLORS



class MyApp(MDApp):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)
        self.theme_cls.theme_style = "Dark"  # Tema claro por defecto
        self.theme_cls.primary_palette = "Purple"
        self.sys = System()
        self.sm = ScreenManager()
        self.action_list = []
        self.clock = Clock.schedule_interval( self.run_action, 0.01)


    def add_action(self, function, action='d'):
        if action not in ['d', 'c']:
            raise ValueError('Invalid action')
        self.action_list.append((action, function))


    def run_action(self, *args):
        """
        actions:
            d = delete
            c = continue
        """
        for i, action_data in enumerate(self.action_list):
            action, function = action_data
            function()
            if action == 'd':
                del self.action_list[i]


    def on_start(self):
        for name, screen in SCREENS:
            screen_instance = screen()
            screen_instance.name = name
            self.sm.add_widget(screen_instance)


    def build(self):
        return self.sm



if __name__ == '__main__':
    MyApp().run()