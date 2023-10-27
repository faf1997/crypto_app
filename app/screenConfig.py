from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget, ThreeLineAvatarListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.clock import Clock


from customWidgets.itemConfirm import ItemConfirm
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog



Builder.load_string("""


<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "190dp"

    MDTextField:
        hint_text: "crypto name"

    MDTextField:
        hint_text: "Crypto symbol"
    
    MDTextField:
        hint_text: "Crypto image url"


<PBoxLayout@MDBoxLayout>:
    padding: 20
    spacing: 20
    size_hint: 1,1
    orientation: 'vertical'



<ScreenConfig>:
    name: 'screen_config'
    MDBoxLayout:
        orientation: 'vertical'
        # canvas.before:
        # Rectangle:
        #     # pos: self.pos
        #     # size: self.size
        #     # source: 'imgs/fondo.png'
        MDTopAppBar:
            elevation: 0
            title: "Configs"
            right_action_items: [["dots-vertical", lambda x: None]]
            left_action_items: [["arrow-left", lambda x: app.sm.get_screen('screen_config').current('screen_list')]]
        PBoxLayout:
            MDScrollView:
                MDList:
                    ThreeLineAvatarListItem:
                        text: "Crypto price update time:"
                        secondary_text: "1"
                        on_release:
                            app.sm.get_screen('screen_config').show_confirmation_dialog()
                        IconLeftWidget:
                            icon: "update"
                    ThreeLineAvatarListItem:
                        text: "Add cryptos:"
                        secondary_text: "1"
                        on_release:
                            app.sm.get_screen('screen_config').show_add_crypto()
                        IconLeftWidget:
                            icon: "plus"

""")




class Content(MDBoxLayout):
    pass




class ScreenConfig(MDScreen):
    def __init__(self, **kwargs):
        super(ScreenConfig, self).__init__(**kwargs)
        self.dialog = None
        self.dialog_add_crypto = None


    def current(self, *args):
        app = MDApp.get_running_app()
        app.sm.current = "screen_list"
        app.sm.get_screen("screen_list").manager.transition.direction = "right"
        app.sys.update_cryptos = True


    def show_add_crypto(self, *args):
        if not self.dialog_add_crypto:
            self.dialog_add_crypto = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog_add_crypto.open()


    def show_confirmation_dialog(self, *args):
                if not self.dialog:
                    self.dialog = MDDialog(
                        title="Select update time",
                        type="confirmation",
                        items=[
                            ItemConfirm(text="1 sec."),
                            ItemConfirm(text="5 sec."),
                            ItemConfirm(text="30 sec."),
                            ItemConfirm(text="1 min."),
                            ItemConfirm(text="5 min."),
                        ],
                        buttons=[
                            MDFlatButton(
                                text="CANCEL",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                            MDFlatButton(
                                text="OK",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                            ),
                        ],
                    )
                self.dialog.open()







