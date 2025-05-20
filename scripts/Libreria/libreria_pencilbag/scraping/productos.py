from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.paginacion import obtener_total_paginas
from utils.limpieza import limpiar_precio
import time
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def obtener_productos_y_precios_pencilbag(driver, max_reintentos=5, espera_entre_intentos=3): 
    """Extrae productos, precios, stock y ofertas desde la web de Pencilbag Librería."""

    for intento in range(max_reintentos):
        logger.info(f"Intento {intento + 1} de {max_reintentos}")

        # Scroll para cargar productos
        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)

        try:
            WebDriverWait(driver, 150).until(
                EC.presence_of_element_located((By.CLASS_NAME, "js-item-info-container"))
            )

            contenedores = driver.find_elements(By.CLASS_NAME, "js-item-info-container")
            
            logger.info(f"{len(contenedores)} productos visibles")

            productos_precios = []

            for container in contenedores:
                desc = container.find_element(By.CLASS_NAME, "item-description")
                # --- STOCK
                try:
                    label_container = desc.find_element(By.CLASS_NAME, "labels")
                    stock_label = label_container.find_element(By.CLASS_NAME, "label")

                    # Analizamos el texto del stock
                    texto_label = stock_label.text.strip()
                    if "SIN STOCK" in texto_label:
                        stock = "No"
                    else:
                        stock = "Si"
                except Exception as e:
                    stock = "Si"

                # --- DESCRIPCIÓN
                try:
                    
                    nombre = desc.find_element(By.CLASS_NAME, "item-name").text.strip()
                except:
                    nombre = "Nombre no disponible"

                # --- PRECIO
                try:
                    contenedor_precio = container.find_element(By.CLASS_NAME, "item-price-container")
                    precio_final = contenedor_precio.find_element(By.CLASS_NAME, "js-price-display").text.strip()

                    try:
                        precio_original_elem = contenedor_precio.find_element(By.CLASS_NAME, "js-compare-price-display")
                        precio_original = precio_original_elem.text.strip()
                        if not precio_original or "$0" in precio_original:
                            precio_original = precio_final
                            tiene_oferta = "No"
                        else:
                            tiene_oferta = "Si"
                    except:
                        precio_original = precio_final
                        tiene_oferta = "No"

                except:
                    precio_final = "No disponible"
                    precio_original = "No disponible"
                    tiene_oferta = "No"
                    
                precio_final_limpio = limpiar_precio(precio_final)
                precio_original_limpio = limpiar_precio(precio_original)

                productos_precios.append({
                    "Nombre del producto": nombre,
                    "Precio final": precio_final_limpio,
                    "Precio original": precio_original_limpio,
                    "Tiene oferta": tiene_oferta,
                    "Stock": stock
                })

            if productos_precios:
                logger.info(f"* {len(productos_precios)} productos.")
                return productos_precios
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
        if pagina == 1:
            url_pagina = url_categoria  # La primera página no lleva /page/X/
        else:
            url_pagina = f"{url_categoria}page/{pagina}/"

        driver.get(url_pagina)
        logger.info(f"Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_productos_y_precios_pencilbag(driver)
        todos_los_productos.extend(productos_pagina)

    return todos_los_productos

