import time
from selenium.webdriver.common.by import By
import logging
import logging.config

logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')

def obtener_total_paginas(driver):
    """Devuelve la cantidad total de páginas basada en los botones de paginación."""
    try:
        time.sleep(3)  # Asegurarse de que cargue la página

        ul_paginacion = driver.find_element(By.CSS_SELECTOR, "ul.pagination.pagination--links")
        paginas = ul_paginacion.find_elements(By.TAG_NAME, "li")

        numeros = []
        for pagina in paginas:
            if pagina.find_elements(By.TAG_NAME, "a"):
                enlace = pagina.find_element(By.TAG_NAME, "a")
                texto = enlace.text.strip()

                # Filtrar botones "‹" y "›"
                if texto not in ["‹", "›"]:
                    try:
                        numero = int(texto)
                        numeros.append(numero)
                    except ValueError:
                        continue  # Ignorar si no es número

        total_paginas = max(numeros) if numeros else 1
        logger.info(f"Total de páginas detectadas: {total_paginas}")
        return total_paginas

    except Exception as e:
        logger.info(f"Error al obtener total de páginas: {e}")
        return 1


