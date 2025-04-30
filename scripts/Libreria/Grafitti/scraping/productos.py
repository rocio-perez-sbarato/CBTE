from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def obtener_productos_y_precios(driver, max_reintentos=5, espera_entre_intentos=3): 
    """Extrae productos, precios, stock y ofertas desde la web de Grafitti Librería."""

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
                EC.presence_of_element_located((By.CLASS_NAME, "item-description"))
            )

            productos = driver.find_elements(By.CLASS_NAME, "item-description")
            print(f"{len(productos)} productos visibles")

            productos_precios = []

            for producto in productos:
                try:
                    nombre = producto.find_element(By.CLASS_NAME, "item-name").text.strip()
                except:
                    nombre = "Nombre no disponible"

                # Obtener contenedor de precios
                try:
                    contenedor_precio = producto.find_element(By.CLASS_NAME, "item-price-container")

                    # Precio final
                    precio_final = contenedor_precio.find_element(By.CLASS_NAME, "item-price").text.strip()

                    # Precio original (si existe)
                    try:
                        compare_element = contenedor_precio.find_element(By.CLASS_NAME, "price-compare")
                        precio_original = compare_element.text.strip()
                        # Si el texto está vacío o es "$0", entonces no hay oferta real
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

                # Stock
                try:
                    stock_div = producto.find_element(By.CLASS_NAME, "js-stock-label")
                    style = stock_div.get_attribute("style")
                    if style and "display:none" in style:
                        stock = "Disponible"
                    else:
                        stock = "Sin stock"
                except:
                    stock = "Disponible"

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



