import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def obtener_cantidad_paginas(driver, productos_por_pagina=28):
    """Obtiene la cantidad total de páginas de productos a partir del contador de resultados."""

    try:
        # Esperar a que aparezca el contador
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span.vtex-search-result-3-x-showingProductsCount")
            )
        )

        texto = elemento.text  # Por ejemplo: "28 de 42"
        partes = texto.split("de")
        if len(partes) == 2:
            total = int(partes[1].strip())
            cantidad_paginas = math.ceil(total / productos_por_pagina)
            logger.info(f"Total de productos: {total}")
            logger.info(f"Total de páginas: {cantidad_paginas}")
            return cantidad_paginas
        else:
            logger.info("No se pudo interpretar el texto del contador.")
            return 1 # Eso es cuando dice "Has visto todos los X productos"

    except Exception as e:
        logger.error(f"Error al obtener cantidad de páginas: {e}")
        return 1
