from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
                EC.presence_of_element_located((By.CLASS_NAME, "item-product"))
            )

            contenedores = driver.find_elements(By.CLASS_NAME, "item-product")
            print(f"{len(contenedores)} productos visibles")

            productos_precios = []

            for container in contenedores:
                # --- DATA VARIANTS
                try:
                    label_container = container.find_element(By.CLASS_NAME, "labels")
                    stock_label = label_container.find_element(By.CLASS_NAME, "js-stock-label")

                    # Analizamos el texto y estilo
                    texto_label = stock_label.text.strip()
                    style = stock_label.get_attribute("style")

                    if "SIN STOCK" in texto_label and ("display:none" not in style if style else True):
                        stock = "No"
                    else:
                        stock = "Si"
                except Exception as e:
                    stock ="Si"

                # --- DESCRIPCIÓN
                try:
                    desc = container.find_element(By.CLASS_NAME, "item-description")
                    nombre = desc.find_element(By.CLASS_NAME, "item-name").text.strip()
                except:
                    nombre = "Nombre no disponible"

                # --- PRECIO
                try:
                    contenedor_precio = container.find_element(By.CLASS_NAME, "item-price-container")
                    precio_final = contenedor_precio.find_element(By.CLASS_NAME, "item-price").text.strip()

                    try:
                        precio_original_elem = contenedor_precio.find_element(By.CLASS_NAME, "price-compare")
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




