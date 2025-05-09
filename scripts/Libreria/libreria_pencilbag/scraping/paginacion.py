import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def obtener_total_paginas(driver):
    """Obtiene el número total de páginas desde el texto '1 / X' en Pencilbag."""
    try:
        time.sleep(3)  # Espera inicial para que cargue contenido

        # Scroll hasta 600 píxeles
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(2)  # Espera breve luego del scroll

        # Esperar el contenedor más específico
        contenedor = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "div.row.justify-content-center.align-items-center.my-4"
            ))
        )

        spans = contenedor.find_elements(By.TAG_NAME, "span")

        if len(spans) >= 3:
            texto = spans[2].text  # Toma el tercer <span>, que debería tener el número total
            total_paginas = int(texto)
            logger.info(f"Total de páginas detectadas: {total_paginas}")
            return total_paginas
        else:
            logger.info("No se encontraron suficientes <span> en el contenedor.")
            return 1

    except Exception as e:
        logger.error(f"Error obteniendo total de páginas: {e}")
        return 1


