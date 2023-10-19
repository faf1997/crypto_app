import unittest
from app.system import System

class TestSystem(unittest.TestCase):
    cryptos = [
                'bitcoin', 
                'ethereum',
                'binance coin',
                'ripple',
                'cardano',
                'solana',
                'polkadot',
                'dogecoin',
                'litecoin'
                ]
    symbols = [
                'BTCUSDT', 
                'ETHUSDT',
                'BNBUSDT',
                'XRPUSDT',
                'ADAUSDT',
                'SOLUSDT',
                'DOTUSDT',
                'DOGEUSDT',
                'LTCUSDT'
                ]

    def setUp(self):
        self.sys = System()

    def tearDown(self):
        pass

    def test_get_crypto_names(self):
        self.assertTrue(
            self.sys.get_crypto_names() == self.cryptos
            )


    def test_get_crypto_symbols(self):
        self.assertTrue(
            self.sys.get_crypto_names() == self.cryptos
            )


    def aux_test_update_cryptos(self, dict_cryptos: dict)-> bool:
        ret = True
        for key in dict_cryptos:
            number: str = dict_cryptos[key]
            try:
                float(number)
                ret = ret and True
            except:
                return False
        return ret 


    def test_update_cryptos(self):
        self.sys.request_price_cryptos()
        while not self.sys.is_finishing_request_price_cryptos():
            pass
        self.assertTrue(self.aux_test_update_cryptos(
                        self.sys.get_price_cryptos())
                        )


    def aux_test_off_update_cryptos(self, dict_cryptos: dict)-> bool:
        ret = True
        none_value = "---"
        for key in dict_cryptos:
            price_crypto: str = dict_cryptos[key]
            ret = ret and price_crypto == none_value
        return ret


    def test_off_update_cryptos(self):
        self.sys.update_cryptos = False
        self.sys.request_price_cryptos()
        while not self.sys.is_finishing_request_price_cryptos():
            pass
        self.assertTrue(self.aux_test_off_update_cryptos(
                        self.sys.get_price_cryptos())
                        )


if __name__ == '__main__':
    unittest.main()

