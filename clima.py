import os
import requests
from dotenv import load_dotenv
import unicodedata

# Diccionario de traducción de términos climáticos
traducciones_clima = {
    "clear sky": "cielo despejado",
    "few clouds": "pocas nubes",
    "scattered clouds": "nubes dispersas",
    "broken clouds": "nubes rotas",
    "shower rain": "lluvia ligera",
    "rain": "lluvia",
    "thunderstorm": "tormenta eléctrica",
    "snow": "nieve",
    "mist": "niebla",
    "overcast clouds": "nubes cubiertas"
}

def eliminar_acentos(texto):
    # Normalizar la cadena y eliminar los acentos
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

# Cargar las variables del archivo .env
load_dotenv()

def obtener_clima(ciudad):
    api_key = os.getenv("API_KEY")
    url = os.getenv("URL")

    if not api_key or not url:
        print("Faltan configuraciones necesarias en el archivo .env")
        return None

    url_completa = f"{url}?q={ciudad}&appid={api_key}&units=metric"

    try:
        respuesta = requests.get(url_completa, timeout=10)
        respuesta.raise_for_status()

        datos = respuesta.json()

        if 'main' in datos:
            # Inicializar el traductor
            descripcion_ingles = datos["weather"][0]["description"]
            
            # Traducir la descripción usando el diccionario
            descripcion_espanol = traducciones_clima.get(descripcion_ingles, descripcion_ingles)
            ciudad_sin_acento = eliminar_acentos(datos["name"]) 
            return {
                "ciudad": ciudad_sin_acento,
                "temperatura": datos["main"]["temp"],
                "descripcion": descripcion_espanol,
                "humedad": datos["main"]["humidity"]
            }
        else:
            print("La API no devolvió los datos esperados.")
            return None

    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error de conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Se agotó el tiempo de espera: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    return None
