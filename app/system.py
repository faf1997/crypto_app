# import sys
# sys.path.append("..")

from utils import get_price_crypto_binance, check_internet_connection, read_json_file, write_json_file, download_img_png
import threading


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
        self.__crypto_dict: dict = {
                            "bitcoin": "BTCUSDT",
                            "ethereum": "ETHUSDT",
                            "binance coin": "BNBUSDT",
                            "ripple": "XRPUSDT",
                            "cardano": "ADAUSDT",
                            "solana": "SOLUSDT",
                            "polkadot": "DOTUSDT",
                            "dogecoin": "DOGEUSDT",
                            "litecoin": "LTCUSDT",
                            "monero": "XMRUSDT"
                            }
        self.__crypto_prices: dict = { #crypto price
                            "bitcoin": "---",
                            "ethereum": "---",
                            "binance coin": "---",
                            "ripple": "---",
                            "cardano": "---",
                            "solana": "---",
                            "polkadot": "---",
                            "dogecoin": "---",
                            "litecoin": "---",
                            "monero": "---"
                            }
        self.check_internet_connection()

    def check_internet_connection(self):
        self.__async.add_job("check_internet_connection",self.__check_internet_connection())
        

    def __check_internet_connection(self):
        self.__internet_connection  = check_internet_connection()
        self.__update_status = self.__internet_connection

        

    def get_symbol_crypto(self, name_crypto):
        '''
        returns the symbol of the cryptocurrency
        indicating its name
        '''
        if not name_crypto in self.__crypto_dict:
            raise ValueError("Crypto name is not in the list")
        return self.__crypto_dict[name_crypto]


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
            raise ValueError("Only boolean values ​​are accepted")
        self.__update_status = value


    def get_crypto_names(self)-> list:
        '''
        returns a list of the names
        of the available cryptocurrencies
        '''
        return [key for key in self.__crypto_dict]
    

    def get_crypto_symbols(self)-> list:
        '''
        returns a list of symbols available
        to check cryptocurrency prices on binance
        '''
        return [self.__crypto_dict[key] for key in self.__crypto_dict]


    def get_price_cryptos(self):
        '''
        returns a dictionary of cryptocurrency prices,
        To update prices call
        self.request_price_cryptos(), and check the
        update status with self.is_finishing_request_price_cryptos()
        '''
        return self.__crypto_prices.copy()


    def __set_result_request(self,crypto_name, symbol):
        '''
        modifies the price of the cryptocurrency
        upon completion of the asynchronous price query
        '''
        try:
            self.__crypto_prices[crypto_name] = f'{get_price_crypto_binance(symbol)}'
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
            for crypto_name in self.__crypto_dict:
                symbol = self.__crypto_dict[crypto_name]
                self.__async.add_job(
                    crypto_name,
                    lambda: self.__set_result_request(
                        crypto_name,
                        symbol
                        )
                    )














if __name__ == "__main__":
    sys = System()
    # sys.request_price_cryptos()
    # while True:
    #     if sys.is_finishing_request_price_cryptos():
    #         break
    # print(sys.get_price_cryptos())



