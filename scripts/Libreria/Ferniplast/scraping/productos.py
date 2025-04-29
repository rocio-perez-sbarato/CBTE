import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from scraping.paginacion import obtener_cantidad_paginas

# TODO: manejar ofertas

def obtener_productos_y_precios_ferniplast(driver, max_reintentos=5, espera_entre_intentos=3):
    """Extrae productos y precios de Ferniplast, reintentando hasta encontrar al menos uno filtrado."""

    for intento in range(max_reintentos):
        print("---------\n")
        print(f"😦 Intento {intento + 1} de {max_reintentos}")
        print("---------\n")

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
            print(f"{len(productos)} productos visibles")

            productos_precios = []

            for producto in productos:
                # Extraer nombre del producto desde el atributo aria-label
                nombre = producto.get_attribute("aria-label") or "Sin nombre"
                nuevo_nombre = nombre.strip()

                # Buscar el precio final
                try:
                    precio_elemento = producto.find_element(
                        By.CSS_SELECTOR,
                        "span.vtex-store-components-3-x-sellingPriceValue"
                    )
                    selling_price = precio_elemento.text.replace("\n", "").strip()
                except:
                    selling_price = "No disponible"

                # En VTEX muchas veces no está el precio tachado, se asume igual
                list_price = selling_price  # Por ahora no diferenciamos

                productos_precios.append({
                    "Nombre del producto": nuevo_nombre,
                    "Precio final": selling_price,
                    "Precio original": list_price,
                    "Tiene oferta": "No"
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

    total_paginas = obtener_cantidad_paginas(driver)

    todos_los_productos = []

    for pagina in range(1, total_paginas + 1):
        url_pagina = f"{url_categoria}?page={pagina}"
        driver.get(url_pagina)
        print(f"🕵️ Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_productos_y_precios_ferniplast(driver)
        todos_los_productos.extend(productos_pagina)

    return todos_los_productos


