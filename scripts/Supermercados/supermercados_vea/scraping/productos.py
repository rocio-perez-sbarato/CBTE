import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils.limpieza import filtrar_productos
from scraping.paginacion import obtener_total_paginas
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# NOTA: scrapea también lo que está en los sliders al fondo... 

def obtener_productos_y_precios_vea(driver, max_reintentos=5, espera_entre_intentos=3):
    """Extrae productos y precios desde la página de Disco."""
    
    for intento in range(max_reintentos):
        print("---------\n")
        print(f"😦 Intento {intento + 1} de {max_reintentos}")
        print("---------\n")
        
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
            productos_precios = []

            for producto in productos:
                try:
                    nombre = producto.find_element(By.CSS_SELECTOR, "div.vtex-product-summary-2-x-nameContainer h2")
                    nombre_producto = nombre.text.strip()
                except:
                    nombre_producto = "No disponible"

                try:
                    # El precio en Disco está dentro de un div con id 'priceContainer'
                    precio_elemento = producto.find_element(By.CSS_SELECTOR, "div#priceContainer")
                    precio = precio_elemento.text.strip()
                except:
                    precio = "No disponible"

                productos_precios.append({
                    "Producto": nombre_producto,
                    "Precio": precio
                })

            productos_filtrados = filtrar_productos(productos_precios)

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
        url_pagina = f"{url_categoria}?page={pagina}"
        driver.get(url_pagina)
        print(f"🕵️ Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_productos_y_precios_vea(driver)
        todos_los_productos.extend(productos_pagina)

    return todos_los_productos



