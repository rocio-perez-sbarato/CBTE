from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.paginacion import obtener_total_paginas
import time

def obtener_productos_y_precios_pencilbag(driver, max_reintentos=5, espera_entre_intentos=3): 
    """Extrae productos, precios, stock y ofertas desde la web de Pencilbag Librería."""

    for intento in range(max_reintentos):
        print("---------\n")
        print(f"😦 Intento {intento + 1} de {max_reintentos}")
        print("---------\n")

        # Scroll para cargar productos
        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "js-item-info-container"))
            )

            contenedores = driver.find_elements(By.CLASS_NAME, "js-item-info-container")
            
            print(f"{len(contenedores)} productos visibles")

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
                            tiene_oferta = "Sí"
                    except:
                        precio_original = precio_final
                        tiene_oferta = "No"

                except:
                    precio_final = "No disponible"
                    precio_original = "No disponible"
                    tiene_oferta = "No"

                productos_precios.append({
                    "Nombre del producto": nombre,
                    "Precio final": precio_final,
                    "Precio original": precio_original,
                    "Tiene oferta": tiene_oferta,
                    "Stock": stock
                })

            productos_filtrados = productos_precios

            if productos_filtrados:
                print(f"* {len(productos_filtrados)} productos.")
                return productos_filtrados
            else:
                print("😢 No se encontraron productos. Reintentando...")
                time.sleep(espera_entre_intentos)

        except Exception as e:
            print(f"😢 Error en intento {intento + 1}: {e}")
            time.sleep(espera_entre_intentos)

    print("😢 No se encontraron productos luego de varios intentos.\n")
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
        print(f"🕵️ Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_productos_y_precios_pencilbag(driver)
        todos_los_productos.extend(productos_pagina)

    return todos_los_productos

