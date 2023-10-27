from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty
from kivy.clock import Clock

Builder.load_string("""
<SplashScreen>:
    name: "splash_screen"
    
    MDScreen:
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
""")



class SplashScreen(MDScreen):
    rotation_angle = NumericProperty(0)
    rotation_speed = 2

    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.img_update = Clock.schedule_interval(self.rotation_update, 0.01)

    def rotation_update(self, dt):
        print(f"activo: {self.rotation_angle}")
        if self.rotation_angle < -350:
            app = MDApp.get_running_app()
            app.sm.current = "screen_list"
            app.sm.get_screen("screen_list").manager.transition.direction = "left"
            Clock.unschedule(self.img_update)
            app.sys.update_cryptos = True
        else:
            self.rotation_angle -= self.rotation_speed

