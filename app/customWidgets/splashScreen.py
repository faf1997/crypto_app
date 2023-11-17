from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty
from kivy.clock import Clock

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_string("""
<SplashScreen>:
    name: "splash_screen"
    MDBoxLayout:
        id: float_layout
        orientation: 'vertical'
        padding: 20
        spacing: 20

        MDLabel:
            id: offline_label
            text: 'There is no connection'
            size_hint: 1, 0.05
            halign: 'center'
            opacity: 0

        MDFloatLayout:
            Image:
                id: img_rotation
                source: 'imgs/bitcoin.png'
                size_hint: None, None
                size: 200, 200
                pos_hint: {'center_x': .5, 'center_y': .5}
                canvas.before:
                    PushMatrix
                    Rotate:
                        angle: root.rotation_angle
                        origin: self.center
                canvas.after:
                    PopMatrix

        MDFillRoundFlatIconButton:
            id: offline_button
            icon: 'reload'
            text: 'Retry connetion'
            size_hint_x: 1
            on_release: app.sm.get_screen('splash_screen').retry_connetion()
            opacity: 0
            disabled: True

""")



class SplashScreen(MDScreen):
    
    rotation_angle = NumericProperty(0)
    rotation_speed = 2

    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.img_update = Clock.schedule_interval(self.rotation_update, 0.01)


    def retry_connetion(self):
        self.rotation_angle += 352
        self.img_update = Clock.schedule_interval(self.rotation_update, 0.01)
        self.__quit_offline_widgets()



    def rotation_update(self, dt):
        if abs(self.rotation_angle) > 350:
            app = MDApp.get_running_app()
            if app.sys.internet_connection:
                screen_list = app.sm.get_screen("screen_list")
                screen_list.manager.transition.direction = "left"
                app.sm.current = "screen_list"
                Clock.unschedule(self.img_update)
            else:
                self.__add_offline_widgets()
        else:
            self.rotation_angle -= self.rotation_speed


    def __quit_offline_widgets(self):
        self.ids.get('offline_label').opacity = 0
        self.ids.get('offline_button').opacity = 0
        self.ids.get('offline_button').disabled = True


    def __add_offline_widgets(self):
        self.ids.get('offline_label').opacity = 1
        self.ids.get('offline_button').opacity = 1
        self.ids.get('offline_button').disabled = False


