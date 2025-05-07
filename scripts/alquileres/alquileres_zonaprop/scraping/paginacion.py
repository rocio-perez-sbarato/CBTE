import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import logging.config
from bs4 import BeautifulSoup
# TODO: manejar las paginas. Idea: avanzar de a 1 y ver si hay un boton de siguiente,
# sino no seguir. no vamos apoder obtener el total, pero vamos a determinar si
# hay un boton de siguiente o no en esa página...
logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')

def hay_pagina_siguiente(driver):
    """Devuelve True si existe el botón de 'página siguiente', False en caso contrario."""
    try:
        time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")

        boton_siguiente = soup.select_one('a[data-qa="PAGING_NEXT"]')
        hay_siguiente = boton_siguiente is not None

        logger.info(f"¿Hay página siguiente?: {hay_siguiente}")
        return hay_siguiente

    except Exception as e:
        logger.warning(f"Error al verificar página siguiente: {e}")
        return False





