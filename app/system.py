# import sys
# sys.path.append("..")

from utils import get_price_crypto_binance, check_internet_connection, read_json_file, write_json_file, download_image
import threading
import os

class Async:
    def __init__(self):
        self.threads = {}


    def add_job(self,name_job, job):
        thread = threading.Thread(target=job)
        self.threads[name_job] = thread
        thread.start()


    def is_finish(self):
        finish = True
        for name_job in self.threads:
            finish = finish and not self.threads[name_job].is_alive()
        if finish:
            self.threads = {}
        return finish


class System:
    def __init__(self):
        self.__internet_connection: bool = False
        self.__update_status: bool = False
        self.__async: Async = Async()
        absolut_path = os.path.abspath(__file__)
        self.__crypto_data = read_json_file("app/data/crypto_data.json")
        self.__configs = read_json_file("app/data/configs.json")
        self.check_internet_connection()

    @property
    def theme_mode(self):
        return self.__configs['theme_mode']
    
    
    @theme_mode.setter
    def theme_mode(self, theme_mode):
        self.__configs['theme_mode'] = theme_mode
        self.save_data()


    def add_crypto(self, name, symbol, url_image):
        '''
        Add a new cryptocurrency to the list
        '''
        path_img = download_image(url_image, "app/images/")
        self.__crypto_data[symbol] = {
            'par': f'{symbol.upper()}USDT',
            'price': '---',
            'image': path_img,
            'symbol': symbol.upper(),
            'name': name
        }
        self.save_data()

    def get_theme_mode(self):
        return self.__configs['theme_mode']
    
    
    def get_refresh_time(self):
        return self.__configs['refresh_time']


    def check_internet_connection(self):
        self.__async.add_job("check_internet_connection",self.__check_internet_connection())


    def __check_internet_connection(self):
        self.__internet_connection  = check_internet_connection()
        self.__update_status = self.__internet_connection


    def clear_prices(self):
        for key in self.__crypto_data:
            self.__crypto_data[key]['price'] = '---'
    
    
    def save_data(self):
        write_json_file(self.__crypto_data, "app/data/crypto_data.json")
        write_json_file(self.__configs, "app/data/configs.json")

    def get_images_path(self):
        '''
        returns the path to the images of the available cryptocurrencies
        '''
        paths = {}
        for key in self.__crypto_data:
            paths[key] = self.__crypto_data[key]['image']
        return paths

    @property
    def internet_connection(self)-> bool:
        return self.__internet_connection


    @property
    def update_cryptos(self)-> bool:
        '''
        check if the cryptocurrency update
        is activated or deactivated
        '''
        return self.__update_status


    @update_cryptos.setter
    def update_cryptos(self, value: bool):
        '''
        activate and deactivate the updating
        of cryptocurrency prices
        '''
        if not isinstance(value,(bool)):
            raise ValueError("Only boolean values are accepted")
        self.__update_status = value


    def get_crypto_names(self)-> list:
        '''
        returns a list of the names
        of the available cryptocurrencies
        '''
        return [self.__crypto_data[key]['name'] for key in self.__crypto_data]
    

    def get_crypto_symbols(self)-> list:
        '''
        returns a list of symbols available
        to check cryptocurrency prices on binance
        '''
        return [self.__crypto_data[key]['par'] for key in self.__crypto_data]


    def get_price_cryptos(self):
        '''
        returns a dictionary of cryptocurrency prices,
        To update prices call
        self.request_price_cryptos(), and check the
        update status with self.is_finishing_request_price_cryptos()
        '''
        prices = {}
        for key in self.__crypto_data:
            prices[key] = self.__crypto_data[key]['price']
        return prices


    def __set_result_request(self,crypto_name, symbol):
        '''
        modifies the price of the cryptocurrency
        upon completion of the asynchronous price query
        '''
        try:
            self.__crypto_data[crypto_name]['price'] = f'{get_price_crypto_binance(symbol)}'
        except:
            self.__internet_connection = False


    def is_finishing_request_price_cryptos(self):
        '''
        Check if the cryptocurrency prices have finished updating
        '''
        return self.__async.is_finish()


    def request_price_cryptos(self):
        '''
        updates all prices of available cryptocurrencies
        '''
        if self.__internet_connection and self.update_cryptos:
            dict_prices = {}
            for key in self.__crypto_data:
                self.__async.add_job(
                    key,
                    lambda: self.__set_result_request(
                        key,
                        self.__crypto_data[key]['par']
                        )
                    )














if __name__ == "__main__":
    sys = System()
    # sys.request_price_cryptos()
    # while True:
    #     if sys.is_finishing_request_price_cryptos():
    #         break
    # print(sys.get_price_cryptos())



