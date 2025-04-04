from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import re
from bs4 import BeautifulSoup

def limpiar_nombre(nombre):
    """Elimina la palabra 'Producto' al inicio del nombre, con o sin espacio."""
    return re.sub(r"^Producto\s*", "", nombre)  # Quita 'Producto' + cualquier espacio opcional

def filtrar_productos(productos):
    """Filtra los productos que son 'slider' o tienen todos los atributos 'No disponible'."""
    productos_filtrados = []
    for producto in productos:
        # Filtrar productos llamados 'slider' o con atributos 'No disponible'
        if "slider" not in producto["Nombre del producto"].lower() and \
           not (producto["Precio final"] == "No disponible" and 
                producto["Precio original"] == "No disponible" and 
                producto["Beneficio Mi CRF"] == "No"):
            productos_filtrados.append(producto)
    
    return productos_filtrados

def obtener_nombre_subcategoria(url):
    """Extrae el nombre de la subcategoría desde la URL para usarlo en el nombre del archivo."""
    partes = url.split("/")[-3:]  
    return "-".join(partes)

def obtener_productos_y_precios(driver):
    """Extrae nombres de productos y sus precios asegurando correspondencia, detectando ofertas y beneficios."""
    
    # Scroll para cargar todo
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
    
    try:
        # Esperar a que los productos aparezcan
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section[aria-label]"))
        )
        
        # Simular interacción para cargar más productos
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        # Obtener todos los productos visibles
        productos = driver.find_elements(By.CSS_SELECTOR, "section[aria-label]")

        print(f"Productos encontrados: {len(productos)}")

        productos_precios = []

        for producto in productos:
            nombre = producto.get_attribute("aria-label")
            nuevo_nombre = limpiar_nombre(nombre)
            print(f"Producto encontrado: {nuevo_nombre}")

            try:
                # Obtener el selling price (precio de venta actual)
                precio_elemento = producto.find_element(By.CSS_SELECTOR, "span.valtech-carrefourar-product-price-0-x-sellingPriceValue")
                selling_price = precio_elemento.text.replace("\n", "").strip()
            except:
                selling_price = "No disponible"

            try:
                # Intentar obtener el list price (precio sin oferta)
                list_price_elemento = producto.find_element(By.CSS_SELECTOR, "span.valtech-carrefourar-product-price-0-x-listPrice")
                list_price = list_price_elemento.text.replace("\n", "").strip()
                print(list_price)
            except:
                list_price = selling_price  # Si no hay list price, el selling price es el único precio válido

            # Verificar si el producto tiene beneficio Mi CRF
            try:
                mi_crf_elemento = producto.find_element(By.CSS_SELECTOR, "div[data-highlight-name*='Mi CRF']")
                beneficio_mi_crf = "Sí"
            except:
                beneficio_mi_crf = "No"

            productos_precios.append({
                "Nombre del producto": nuevo_nombre,
                "Precio final": selling_price,
                "Precio original": list_price if list_price != selling_price else selling_price,  # Si no tiene oferta, repetir precio
                "Tiene oferta": "Sí" if list_price != selling_price else "No",
                "Beneficio Mi CRF": "Sí" if beneficio_mi_crf == "Si" else "No"
            })

        return productos_precios
    
    except Exception as e:
        print(f"Error: {e}")
        return []

def obtener_total_paginas(driver):
    """Obtiene el número total de páginas de la categoría."""
    try:
        time.sleep(3)  # Asegurar que la página carga completamente
        
        # Buscar los botones de paginación
        paginas = driver.find_elements(By.CSS_SELECTOR, "div.valtech-carrefourar-search-result-3-x-paginationButtonPages button")
        
        # Extraer los números de las páginas
        numeros = []
        for pagina in paginas:
            try:
                num = int(pagina.text.strip())
                numeros.append(num)
            except ValueError:
                continue  # Ignorar valores no numéricos

        total_paginas = max(numeros) if numeros else 1
        print(f"Total de páginas detectadas: {total_paginas}")
        return total_paginas

    except Exception as e:
        print(f"Error obteniendo páginas: {e}")
        return 1

def scrapear_categoria(driver, url_categoria):
    """Recorre todas las páginas de una categoría y extrae los productos."""
    driver.get(url_categoria)
    time.sleep(3)

    total_paginas = obtener_total_paginas(driver)
    print(f"Total de páginas encontradas: {total_paginas}")

    todos_los_productos = []

    for pagina in range(1, total_paginas + 1):
        url_pagina = f"{url_categoria}?page={pagina}"
        driver.get(url_pagina)
        print(f"Scrapeando página {pagina} de {total_paginas}...")
        time.sleep(3)

        productos_pagina = obtener_productos_y_precios(driver)
        todos_los_productos.extend(productos_pagina)

    return todos_los_productos

def guardar_en_excel(productos, url_categoria):
    """Guarda los productos en un archivo Excel con el nombre de la subcategoría."""
    if not productos:
        print("No hay productos para guardar.")
        return

    nombre_subcategoria = obtener_nombre_subcategoria(url_categoria)
    nombre_archivo = f"{nombre_subcategoria}.xlsx"

    df = pd.DataFrame(productos)
    df.to_excel(nombre_archivo, index=False)
    
    print(f"Datos guardados en '{nombre_archivo}'")

# Configuración de Selenium con Firefox en modo headless
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# URL de la página
url = "https://www.carrefour.com.ar/Bazar-y-textil/Libreria?order="
driver.get(url)

productos = scrapear_categoria(driver, url)
productos_filtrados = filtrar_productos(productos)
guardar_en_excel(productos_filtrados, url)

driver.quit()


