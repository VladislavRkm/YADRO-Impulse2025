import logging
import requests 
   
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

urls = [
    "https://httpstat.us/103",
    "https://httpstat.us/204",
    "https://httpstat.us/308",
    "https://httpstat.us/418",
    "https://httpstat.us/508",
]

def make_request(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if 100 <= status_code < 400:
            logging.info(f"Ответ {status_code}: {response.text}")
        elif 400 <= status_code < 600:
            raise Exception(f"Ошибка {status_code}: {response.text}")
    except Exception as e:
        logging.error(f"Запрос к {url} завершился ошибкой: {e}")

for url in urls:
    make_request(url)

