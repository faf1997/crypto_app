from utils import get_price_crypto_binance
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


class Processing:
    def __init__(self):
        self.processes = {}

    def add_job(self, name_job, job):
        process = Process(target=job)
        self.processes[name_job] = process
        process.start()

    def is_finish(self):
        finish = True
        for name_job in self.processes:
            finish = finish and not self.processes[name_job].is_alive()
        if finish:
            self.processes = {}
        return finish

        self.results = pool.map(get_price_crypto_binance, symbols)

        for result in results:
            print(result)



class System:
    def __init__(self):
        self.__crypto_states: bool = True
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
                            "litecoin": "LTCUSDT"
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
                            "litecoin": "---"
                            }


    def get_symbol_crypto(self, name_crypto):
        '''
        returns the symbol of the cryptocurrency
        indicating its name
        '''
        return self.__crypto_dict[name_crypto]

    @property
    def update_cryptos(self)-> bool:
        '''
        check if the cryptocurrency update
        is activated or deactivated
        '''
        return self.__crypto_states


    @update_cryptos.setter
    def update_cryptos(self, value: bool):
        '''
        activate and deactivate the updating
        of cryptocurrency prices
        '''
        self.__crypto_states = value


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
        self.__crypto_prices[crypto_name] = f'{get_price_crypto_binance(symbol)}'


    def is_finishing_request_price_cryptos(self):
        '''
        Check if the cryptocurrency prices have finished updating
        '''
        return self.__async.is_finish()


    def request_price_cryptos(self):
        '''
        updates all prices of available cryptocurrencies
        '''
        if self.update_cryptos:
            dict_prices = {}
            for crypto_name in self.__crypto_dict:
                symbol = self.__crypto_dict[crypto_name]
                self.__async.add_job(crypto_name, lambda: self.__set_result_request(crypto_name, symbol))



if __name__ == "__main__":
    sys = System()
    sys.request_price_cryptos()
    while True:
        if sys.is_finishing_request_price_cryptos():            
            break

