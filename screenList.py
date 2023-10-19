from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget, ThreeLineAvatarListItem
from kivy.lang import Builder
from kivy.clock import Clock

from system import Async




Builder.load_string("""
<PBoxLayout@MDBoxLayout>:
    padding: 20
    spacing: 20
    size_hint: 1,1
    orientation: 'vertical'
                    
<ScreenList>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            elevation: 0
            right_action_items: [["dots-vertical", lambda x: None]]
        PBoxLayout:
            MDScrollView:
                MDList:
                    id: list_data
    MDFloatLayout:
        MDAnchorLayout:
            anchor_x:'right'
            anchor_y:'bottom'
            padding: 20
            spacing: 20

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
        



    