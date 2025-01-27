import requests
import json
import os
from urllib.parse import urlparse



def download_image(url, save_folder="images"):
    """
    Descarga una imagen desde una URL y devuelve el nombre y la ruta del archivo.

    :param url: URL de la imagen a descargar.
    :param save_folder: Carpeta donde se guardará la imagen (por defecto es "images").
    :return: str o None
    """
    try:
        # Crear la carpeta si no existe
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # Obtener el nombre del archivo desde la URL
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)  # Extrae el nombre del archivo de la URL

        # Si el nombre del archivo está vacío, usar un nombre predeterminado
        if not file_name:
            file_name = "downloaded_image.jpg"

        # Definir la ruta completa del archivo
        file_path = os.path.join(save_folder, file_name)

        # Descargar la imagen
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la descarga falla

        # Guardar la imagen en el archivo
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Imagen descargada y guardada como: {file_path}")
        return f'{file_path}{file_name}'

    except Exception as e:
        print(f"Error al descargar la imagen: {e}")
        return ''


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




