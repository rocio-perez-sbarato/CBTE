import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from scraping.paginacion import obtener_cantidad_paginas
from utils.limpieza import limpiar_precio, filtrar_productos
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def obtener_productos_y_precios_ferniplast(driver, max_reintentos=5, espera_entre_intentos=3): 
    """Extrae productos y precios de Ferniplast, incluyendo detección de ofertas."""
    
    for intento in range(max_reintentos):
        logger.info(f"Intento {intento + 1} de {max_reintentos}")

        # Scroll para cargar productos
        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "section[aria-label]"))
            )

            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

            productos = driver.find_elements(By.CSS_SELECTOR, "section[aria-label]")
            logger.info(f"{len(productos)} productos visibles")

            productos_precios = []

            for producto in productos:
                try:
                    nombre_elemento = producto.find_element(
                        By.CSS_SELECTOR,
                        "span.vtex-product-summary-2-x-productBrand"
                    )
                    nuevo_nombre = nombre_elemento.text.strip()
                except:
                    nuevo_nombre = "Sin nombre"

                # Precio final (siempre intentamos extraerlo)
                try:
                    precio_elemento = producto.find_element(
                        By.CSS_SELECTOR,
                        "span.vtex-store-components-3-x-sellingPriceValue"
                    )
                    selling_price = precio_elemento.text.replace("\n", "").strip()
                    selling_price_num = float(selling_price.replace("$", "").replace(".", "").replace(",", "."))
                except:
                    selling_price = "No disponible"
                    selling_price_num = 0.0

                # Precio original (si existe)
                try:
                    list_price_element = producto.find_element(
                        By.CSS_SELECTOR,
                        "span.vtex-store-components-3-x-listPriceValue"
                    )
                    list_price = list_price_element.text.replace("\n", "").strip()
                    list_price_num = float(list_price.replace("$", "").replace(".", "").replace(",", "."))
                except:
                    list_price = selling_price
                    list_price_num = selling_price_num

                # Verificar si hay oferta
                tiene_oferta = "Si" if list_price_num > selling_price_num else "No"

                productos_precios.append({
                    "Nombre del producto": nuevo_nombre,
                    "Precio final": selling_price_num,
                    "Precio original": list_price_num,
                    "Tiene oferta": tiene_oferta
                })

            productos_filtrados = filtrar_productos(productos_precios)
            if productos_filtrados:
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

    total_paginas = obtener_cantidad_paginas(driver)

    todos_los_productos = []

    for pagina in range(1, total_paginas + 1):
        url_pagina = f"{url_categoria}?page={pagina}"
        logger.info(f"Scrapeando página {pagina} de {total_paginas}...")
        driver.get(url_pagina)
        time.sleep(3)

        productos_pagina = obtener_productos_y_precios_ferniplast(driver)
        todos_los_productos.extend(productos_pagina)

    return todos_los_productos


