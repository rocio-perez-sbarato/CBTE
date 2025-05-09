import time
from selenium.webdriver.common.by import By
import logging
import logging.config

logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')

def obtener_total_paginas(driver):
    """Obtiene el número total de páginas desde el paginador de La Voz."""
    try:
        time.sleep(3)  # Espera para asegurar carga

        # Buscar todos los elementos <li> del paginador
        paginador = driver.find_elements(By.CSS_SELECTOR, "div.wrapper.py2 li")

        numeros = []
        for item in paginador:
            texto = item.text.strip()
            try:
                numero = int(texto)
                numeros.append(numero)
            except ValueError:
                continue  # Ignora íconos, flechas, etc.

        total_paginas = max(numeros) if numeros else 1
        logger.info(f"Total de páginas detectadas: {total_paginas}")
        return total_paginas

    except Exception as e:
        logger.critical(f"Error obteniendo páginas: {e}")
        return 1


