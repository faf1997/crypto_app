from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget, ThreeLineAvatarListItem
from kivy.lang import Builder
from kivy.clock import Clock

from system import Async




Builder.load_string("""
<DrawerClickableItem@MDNavigationDrawerItem>
    #focus_color: "#2596be"
    text_color: "#000000"
    icon_color: "#000000"
    #ripple_color: "#c5bdd2"
    #selected_color: "#0c6c4d"
    radius:[0,0,0,0]


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#000000"
    icon_color: "#000000"
    focus_behavior: False
    selected_color: "#ffffff"
    _no_ripple_effect: True


#-------------------------------
<PBoxLayout@MDBoxLayout>:
    padding: 20
    spacing: 20
    size_hint: 1,1
    orientation: 'vertical'


<ScreenList>:
    name: 'screen_list'

#-------------------------------------------------------
    MDNavigationLayout:

        MDScreenManager:

            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: "Cryptos"
                        elevation: 0
                        #pos_hint: {"top": 1}
                        specific_text_color: "#ffffff"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["dots-vertical", lambda x: None]]
                    PBoxLayout:
                        MDScrollView:
                            MDList:
                                id: list_data



        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Crypto App"
                    title_color: "#000000"
                    text: "Menu"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                # MDNavigationDrawerLabel:
                #     text: "Mail"

                DrawerClickableItem:
                    icon: "cog"
                    right_text: ""
                    text_right_color: "#000000"
                    text: "Configs"
                    on_release: 
                        app.sm.current = "screen_config"
                        app.sm.get_screen("screen_list").manager.transition.direction = "left"
                        nav_drawer.set_state("close")



""")




class ScreenList(MDScreen):
    def __init__(self, **kwargs):
        super(ScreenList, self).__init__(**kwargs)
        self.__async = Async()
        self.__widgets_cryptos = MDApp.get_running_app().sys.get_price_cryptos()
        self.__async.add_job("init_list",self.__init_list())

        

    def __init_list(self):
        path = "imgs/"
        list_data = self.ids.get("list_data")
        cryptos = MDApp.get_running_app().sys.get_price_cryptos()
        for key in cryptos:
            line = ThreeLineAvatarListItem(
                                            text=key.title(),
                                            secondary_text=f"USD {cryptos[key]}",
                                            tertiary_text=f""
                                            )
            self.__widgets_cryptos[key] = line
            line.add_widget(IconLeftWidget(icon=f"{path}{key}.png"))
            list_data.add_widget(line)
        self.update_price = Clock.schedule_interval(lambda x: self.func_update_price(), 1)
        self.__async.is_finish()


    def update_price_widgets(self, dict_cryptos: dict):
        for key in dict_cryptos:
            self.__widgets_cryptos[key].secondary_text = f'USD {dict_cryptos[key]}'


    def func_update_price(self):
        app = MDApp.get_running_app()
        if app.sys.is_finishing_request_price_cryptos():
            self.update_price_widgets(app.sys.get_price_cryptos())
            prices = app.sys.request_price_cryptos()
        















    