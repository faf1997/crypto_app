from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.window import Window
from plyer import notification
import os
from kivymd.uix.screenmanager import ScreenManager
#from kivymd.uix.list import TwoLineListItem
#from kivymd.theming import ThemeManager

from system import System
from custom_widgets.screens import SCREENS
from custom_widgets import THEME_COLORS






    



class MyApp(MDApp):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)
        self.sys = System()
        self.theme_cls.theme_style = self.sys.get_theme_mode()  # Tema claro por defecto
        self.theme_cls.primary_palette = "Orange"
        self.sm = ScreenManager()
        self.action_list = []
        self.clock = Clock.schedule_interval( self.run_action, 1)


    def on_stop(self):
        self.sys.theme_mode = self.theme_cls.theme_style
        self.sys.clear_prices()
        self.sys.save_data()
        return super().on_stop()


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


    def lanzar_notificacion(self, titulo, mensaje):
        notification.notify(title=titulo, message=mensaje)


    def get_screen(self, nombre_pantalla):
        return self.sm.get_screen(nombre_pantalla)


    def get_widget(self, nombre_pantalla, nombre_widget):
        pantalla = self.sm.get_screen(nombre_pantalla)
        widget = pantalla.ids.get(nombre_widget)
        return widget


    def change_screen(self, pantalla_siguiente, direccion='left'):
        """Direction: 'up', 'down', 'left', 'right'"""
        self.sm.transition.direction = direccion
        self.sm.current = pantalla_siguiente


    def get_image(self, nombre_image):
        for path in self.path_imagenes:
            if nombre_image in path:
                return path
        else:
            return ''


    def get_size_Screen(self):
        return Window.size


    def build(self):
        return self.sm



if __name__ == '__main__':
    MyApp().run()