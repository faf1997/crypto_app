import requests



def get_price_crypto_binance(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = float(data.get("price"))
        
        return price
    else:
        return None


def check_internet_connection():
    try:
        requests.get('https://www.google.com')
        return True
    except:
        return False

