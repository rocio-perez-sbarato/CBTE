import time
from selenium.webdriver.common.by import By
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def obtener_total_paginas(driver):
    """Obtiene el número total de páginas de la categoría."""
    try:
        time.sleep(3)  # Asegurar que la página carga completamente

        # Buscar los botones de paginación
        paginas = driver.find_elements(By.CSS_SELECTOR, "div.valtech-carrefourar-search-result-3-x-paginationButtonPages button")

        # Extraer los números de las páginas
        numeros = []
        for pagina in paginas:
            try:
                num = int(pagina.text.strip())
                numeros.append(num)
            except ValueError:
                continue  # Ignorar valores no numéricos

        total_paginas = max(numeros) if numeros else 1
        logger.info(f"Total de páginas detectadas: {total_paginas}")
        return total_paginas

    except Exception as e:
        logger.error(f"Error obteniendo páginas: {e}")
        return 1