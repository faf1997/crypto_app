import requests






def get_price_crypto_binance(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        precio = float(data.get("price"))
        
        return precio
    else:
        return None





if __name__ == "__main__":
    symbols = [("b", "BTCUSDT"), ("e", "ETHUSDT"), ("x", "XRPUSDT"), ("l", "LTCUSDT"), ("a", "ADAUSDT"), ("s", "SOLUSDT"), ("d", "DOTUSDT"), ("m", "MATICUSDT"), ("c", "LINKUSDT"), ("y", "YFIUSDT"), ("u", "UNIUSDT"), ("p", "BNBUSDT"), ("t", "DOGEUSDT"), ("i", "ICPUSDT"), ("o", "ATOMUSDT"), ("r", "XLMUSDT"), ("g", "GRTUSDT"), ("v", "VETUSDT"), ("h", "FILUSDT"), ("j", "XTZUSDT")]
    pool = Pool()
    #with Pool(processes=8) as pool:
    with multiprocessing.Pool() as pool:
        # Utiliza pool.starmap para aplicar la función a cada conjunto de argumentos.
        resultados = pool.starmap(get_price_crypto_binance, symbols)

    #for result in results:
    print(resultados)



