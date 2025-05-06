import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.paginacion import obtener_total_paginas
import logging
import logging.config

logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')


def obtener_alquileres_y_precios_zonaprop(driver, max_reintentos=5, espera_entre_intentos=3):
    """Extrae propiedades y precios desde Zonaprop."""

    for intento in range(max_reintentos):
        logger.info(f"Intento {intento + 1} de {max_reintentos}")

        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(3)

        try:
            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.CLASS_NAME, "postingsList-module__postings-container"))
            )

            cards = driver.find_elements(By.CLASS_NAME, "postingCardLayout-module__posting-card-layout")
            propiedades = []

            for card in cards:
                try:
                    direccion = card.find_element(By.CLASS_NAME, "postingLocations-module__location-address").text
                except:
                    direccion = "No disponible"

                try:
                    precio = card.find_element(By.CLASS_NAME, "postingPrices-module__price").text.strip()
                except:
                    precio = "No disponible"

                try:
                    expensas = card.find_element(By.CLASS_NAME, "postingPrices-module__expenses").text.strip()
                except:
                    expensas = "No disponibles"

                try:
                    caracteristicas = card.find_element(By.CLASS_NAME, "postingMainFeatures-module__posting-main-features-block").text.strip()
                except:
                    caracteristicas = "No disponible"

                propiedades.append({
                    "Dirección": direccion,
                    "Precio": precio,
                    "Expensas": expensas,
                    "Caracteristicas": caracteristicas
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
        url_pagina = f"{url_filtros}-pagina-{pagina}"
        driver.get(url_pagina)
        logger.info(f"Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_alquileres_y_precios_zonaprop(driver)
        todos_los_productos.extend(productos_pagina)
        
    logger.info("Scraping completo.")
    return todos_los_productos


