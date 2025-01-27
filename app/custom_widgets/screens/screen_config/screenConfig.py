from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget, ThreeLineAvatarListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.clock import Clock


from custom_widgets.itemConfirm import ItemConfirm
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout




Builder.load_string("""


<Content@BoxLayout>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "190dp"
    canvas.before:


    MDTextField:
        id: crypto_name_field
        hint_text: "Crypto name"
        widget: "crypto_name_field"

    MDTextField:
        id: crypto_symbol_field
        hint_text: "Crypto symbol"
        widget: "crypto_symbol_field"
    
    MDTextField:
        id: crypto_image_url_field
        hint_text: "Crypto image url"
        widget: "crypto_image_url_field"


<PBoxLayout@MDBoxLayout>:
    padding: 20
    spacing: 20
    size_hint: 1,1
    orientation: 'vertical'



<ScreenConfig>:
    name: 'screen_config'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            elevation: 0
            title: "Configs"
            specific_text_color: "#000000" if app.theme_cls.theme_style == "Light" else "#ffffff"
            right_action_items: [["dots-vertical", lambda x: None]]
            left_action_items: [["arrow-left", lambda x: app.change_screen('screen_list', 'right')]]

        PBoxLayout:
            MDScrollView:
                MDList:
                    TwoLineAvatarListItem:
                        text: "Crypto price update time:"
                        secondary_text: "1"
                        on_release:
                            app.sm.get_screen('screen_config').show_confirmation_dialog()
                        IconLeftWidget:
                            icon: "update"
                    OneLineAvatarListItem:
                        text: "Add cryptos:"
                        on_release:
                            app.sm.get_screen('screen_config').show_add_crypto()
                        IconLeftWidget:
                            icon: "plus"

                    OneLineAvatarListItem:
                        text: "Press light mode" if app.theme_cls.theme_style == "Dark" else "Press dark mode"
                        on_release:
                            app.theme_cls.theme_style = "Light" if app.theme_cls.theme_style == "Dark" else "Dark"
                            # app.theme_cls.text_color = "#ffffff" if app.theme_cls.theme_style == "Dark" else "#000000" 
                        IconLeftWidget:
                            icon: "weather-sunny" if app.theme_cls.theme_style == "Dark" else "weather-night"

""")




class Content(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Content, self).__init__(*args, **kwargs)
        
    def get_childrens(self):
        return self.children


class ScreenConfig(MDScreen):
    def __init__(self, *args, **kwargs):
        super(ScreenConfig, self).__init__(*args, **kwargs)
        self.dialog = None
        self.dialog_add_crypto = None

    def search_widget(self, widget, name):
        for w in widget.children:
            if w.widget == name:
                return w
        return None
    
    def add_crypto(self,content, *args):
        app = MDApp.get_running_app()
        crypto_name_field = self.search_widget(content, 'crypto_name_field')
        crypto_symbol_field = self.search_widget(content, 'crypto_symbol_field')
        crypto_image_url_field = self.search_widget(content, 'crypto_image_url_field')
        # print(crypto_name_field.text, crypto_symbol_field.text, crypto_image_url_field.text)
        app.sys.add_crypto(crypto_name_field.text, crypto_symbol_field.text, crypto_image_url_field.text)
        # app.sys.update_cryptos = True


    # def current(self,  *args):
    #     app = MDApp.get_running_app()
    #     app.sm.current = "screen_list"
    #     app.sm.get_screen("screen_list").manager.transition.direction = "right"
    #     app.sys.update_cryptos = True


    def show_add_crypto(self, *args):
        if not self.dialog_add_crypto:
            self.dialog_add_crypto = MDDialog(
                title="Complete crypto information:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog_add_crypto.dismiss(),
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: (self.add_crypto(self.dialog_add_crypto.content_cls)),# self.dialog_add_crypto.dismiss()),
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
                        on_release=lambda x: self.dialog.dismiss(),
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss(),
                    ),
                ],
            )
        self.dialog.open()
        







