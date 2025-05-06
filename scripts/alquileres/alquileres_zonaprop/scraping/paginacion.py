import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import logging.config
# TODO: manejar las paginas. Idea: avanzar de a 1 y ver si hay un boton de siguiente,
# sino no seguir. no vamos apoder obtener el total, pero vamos a determinar si
# hay un boton de siguiente o no en esa página...
logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')

def obtener_total_paginas(driver, url_base):
    """Recorre las páginas una por una hasta que no haya más botón 'Siguiente' y devuelve el total."""
    try:
        pagina = 1
        while True:
            url = f"{url_base}-pagina-{pagina}"
            driver.get(url)
            time.sleep(3)  # Esperar que cargue

            logger.info(f"Verificando página {pagina}...")

            # Verificamos si hay publicaciones (si no, se terminó)
            for _ in range(5):
                driver.execute_script("window.scrollBy(0, 800);")
                time.sleep(3)


            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.CLASS_NAME, "postingsList-module__postings-container"))
            )
            
            cards = driver.find_elements(By.CLASS_NAME, "postingCardLayout-module__posting-card-layout")
            if not cards:
                logger.info("No se encontraron más publicaciones.")
                break

            # Verificamos si hay botón "Siguiente"
            siguiente = driver.find_elements(By.CSS_SELECTOR, "a[data-qa='PAGING_NEXT']")
            if not siguiente:
                break

            pagina += 1

        logger.info(f"Total de páginas detectadas: {pagina}")
        return pagina

    except Exception as e:
        logger.error(f"Error al obtener total de páginas: {e}")
        return pagina



