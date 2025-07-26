import requests
from bs4 import BeautifulSoup
import html
import json
import pandas as pd
from utils.archivos import dict_en_excel
from scraping.pasajes import obtener_precios_pasajes
from config import destinos, datos, pagina 
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

logger.info("===========INICIANDO SCRAPING DE CENTRAL DE PASAJES===========")
    
for lugar in destinos: 
    lugar_formateado = lugar.replace(" ", "-")
    link_destino = pagina + lugar_formateado + datos
    
    response = requests.get(link_destino)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar el input hidden
    input_hidden = soup.find('input', {'id': 'hidListaBusTrip'})

    if input_hidden and input_hidden.has_attr('value'):
        json_str = html.unescape(input_hidden['value'])
        data = json.loads(json_str)
        dict_info_pasajes = obtener_precios_pasajes(data)
        dict_en_excel(dict_info_pasajes, lugar_formateado)
    else:
        logger.debug("La fecha no está disponible")

logger.info("===========SCRAPING DE CENTRAL DE PASAJES FINALIZADO===========")
    