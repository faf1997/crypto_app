import requests
import json



def download_img_png(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("imgs/imagen_descargada.png", "wb") as file:
            file.write(response.content)


def get_price_crypto_binance(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = float(data.get("price"))
        
        return price
    else:
        return None


def check_internet_connection() -> bool:
    try:
        requests.get('https://www.google.com')
        return True
    except:
        return False



def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data



def write_json_file(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)




