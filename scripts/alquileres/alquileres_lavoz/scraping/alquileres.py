import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.paginacion import obtener_total_paginas
from utils.limpieza import limpiar_precio
import logging
import logging.config

logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')

def obtener_alquileres_y_precios_lavoz(driver, max_reintentos=5, espera_entre_intentos=3):
    """Extrae propiedades y precios desde La Voz."""

    for intento in range(max_reintentos):
        logger.info(f"Intento {intento + 1} de {max_reintentos}")

        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(2)

        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.grid"))
            )

            cards = driver.find_elements(By.CSS_SELECTOR, "div.grid div.flex.flex-wrap")

            propiedades = []

            for card in cards:
                try:
                    barrio = card.find_element(By.CSS_SELECTOR, "div.title-1lines").text.strip()
                except:
                    barrio = "No disponible"

                try:
                    precio = card.find_element(By.CSS_SELECTOR, "p.main span.price").text.strip()
                except:
                    precio = "No disponible"

                precio_limpio = limpiar_precio(precio)
                
                propiedades.append({
                    "Barrio": barrio,
                    "Precio": precio_limpio
                })

            if propiedades:
                logger.info(f"{len(propiedades)} propiedades encontradas.")
                return propiedades
            else:
                logger.warning("No se encontraron propiedades. Reintentando...")
                time.sleep(espera_entre_intentos)

        except Exception as e:
            logger.error(f"Error en intento {intento + 1}: {e}")
            time.sleep(espera_entre_intentos)

    logger.critical("No se encontraron propiedades luego de varios intentos.")
    return []


def scrapear_pagina(driver, url_filtros):
    """Recorre todas las páginas de una categoría y extrae los productos."""
    driver.get(url_filtros)
    time.sleep(3)

    total_paginas = obtener_total_paginas(driver)
    logger.info(f"Total de páginas a scrapear: {total_paginas}")
    
    todos_los_productos = []
    for pagina in range(1, total_paginas + 1):
        url_pagina = f"{url_filtros}&page={pagina}"
        driver.get(url_pagina)
        logger.info(f"Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_alquileres_y_precios_lavoz(driver)
        todos_los_productos.extend(productos_pagina)
        
    logger.info("Scraping completo.")
    return todos_los_productos


