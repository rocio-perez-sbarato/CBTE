import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.limpieza import limpiar_nombre, filtrar_productos, limpiar_precio
from scraping.paginacion import obtener_total_paginas
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

# TODO: precisar la llamada a nombre (class_="vtex-product-summary-2-x-productBrand"
# " vtex-product-summary-2-x-brandName t-body"))

def obtener_productos_y_precios(driver, max_reintentos=5, espera_entre_intentos=3):
    """Extrae productos y precios, reintentando hasta encontrar al menos uno filtrado."""
    
    for intento in range(max_reintentos):
        logger.info(f"Intento {intento + 1} de {max_reintentos}")
        # Scroll para cargar productos
        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)

        try:
            WebDriverWait(driver, 150).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "section[aria-label]"))
            )

            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

            productos = driver.find_elements(By.CSS_SELECTOR, "section[aria-label]")
            logger.info(f"{len(productos)} productos visibles")

            productos_precios = []

            for producto in productos:
                nombre = producto.get_attribute("aria-label")
                nuevo_nombre = limpiar_nombre(nombre)

                try:
                    precio_elemento = producto.find_element(By.CSS_SELECTOR, "span.valtech-carrefourar-product-price-0-x-sellingPriceValue")
                    selling_price = precio_elemento.text.replace("\n", "").strip()
                    selling_price = limpiar_precio(selling_price)
                except:
                    selling_price = "No disponible"

                try:
                    list_price_elemento = producto.find_element(By.CSS_SELECTOR, "span.valtech-carrefourar-product-price-0-x-listPrice")
                    list_price = list_price_elemento.text.replace("\n", "").strip()
                except:
                    list_price = selling_price

                try:
                    mi_crf_elemento = producto.find_element(By.CSS_SELECTOR, "div[data-highlight-name*='Mi CRF']")
                    beneficio_mi_crf = "Sí"
                except:
                    beneficio_mi_crf = "No"

                list_price_limpio = limpiar_precio(list_price)
                selling_price_limpio = limpiar_precio(selling_price)
                
                productos_precios.append({
                    "Nombre del producto": nuevo_nombre,
                    "Precio final": selling_price_limpio,
                    "Precio original": list_price_limpio if list_price_limpio != selling_price_limpio else selling_price_limpio,
                    "Tiene oferta": "Sí" if list_price_limpio != selling_price_limpio else "No",
                    "Beneficio Mi CRF": beneficio_mi_crf
                })

            productos_filtrados = filtrar_productos(productos_precios)

            if productos_filtrados:
                logger.info(f"* {len(productos_filtrados)} productos.")
                return productos_filtrados
            else:
                logger.critical("No se encontraron productos. Reintentando...")
                time.sleep(espera_entre_intentos)

        except Exception as e:
            logger.error(f"Error en intento {intento + 1}: {e}")
            time.sleep(espera_entre_intentos)

    logger.info("No se encontraron productos luego de varios intentos.\n")
    
    return []

def scrapear_categoria(driver, url_categoria):
    """Recorre todas las páginas de una categoría y extrae los productos."""
    driver.get(url_categoria)
    time.sleep(3)

    total_paginas = obtener_total_paginas(driver)

    todos_los_productos = []

    for pagina in range(1, total_paginas + 1):
        url_pagina = f"{url_categoria}?page={pagina}"
        driver.get(url_pagina)
        logger.info(f"Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_productos_y_precios(driver)
        todos_los_productos.extend(productos_pagina)

    return todos_los_productos



