import time
from selenium.webdriver.common.by import By
import re
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')


def obtener_total_paginas(driver):
    """Obtiene el número total de páginas desde el texto 'Página X de Y' en Disco."""
    try:
        time.sleep(3)  # Esperar a que cargue el contenido

        span_info = driver.find_element(By.CLASS_NAME, "discoargentina-search-result-custom-1-x-span-selector-pages")
        texto = span_info.text  # Ejemplo: "Página 1 de 6"

        # Usamos regex para extraer el número final
        match = re.search(r"de\s+(\d+)", texto)
        if match:
            total_paginas = int(match.group(1))
            logger.info(f"Total de páginas detectadas: {total_paginas}")
            return total_paginas
        else:
            logger.info("No se pudo interpretar el texto de paginación.")
            return 1

    except Exception as e:
        logger.error(f"Error obteniendo total de páginas: {e}")
        return 1
