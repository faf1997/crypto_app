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
        self.__async = Async()
        self.__crypto_dict = { 
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
        self.__prices = {
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

    def get_crypto_names(self):
        return [key for key in self.__crypto_dict]
    

    def get_crypto_symbols(self):
        return [self.__crypto_dict[key] for key in self.__crypto_dict]


    def get_crypto_dict(self):
        return self.__crypto_dict.copy()


    def get_price_cryptos(self):
        return self.__prices.copy()


    def __set_result_request(self,crypto_name, symbol):
        self.__prices[crypto_name] = f'{get_price_crypto_binance(symbol)}'

    def is_finish_request_price_cryptos(self):
        return self.__async.is_finish()


    def request_price_cryptos(self):
        dict_prices = {}
        for crypto_name in self.__crypto_dict:
            symbol = self.__crypto_dict[crypto_name]
            self.__async.add_job(crypto_name, lambda: self.__set_result_request(crypto_name, symbol))



if __name__ == "__main__":
    sys = System()
    sys.request_price_cryptos()
    while True:
        if sys.is_finish_request_price_cryptos():            
            break

