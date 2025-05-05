import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TODO: limpiar los precios (idea: separar los numeros separados por el +)

def obtener_alquileres_y_precios_argenprop(driver, max_reintentos=5, espera_entre_intentos=3):
    """Extrae propiedades y precios desde Argenprop."""

    for intento in range(max_reintentos):
        print("---------\n")
        print(f"🔍 Intento {intento + 1} de {max_reintentos}")
        print("---------\n")

        for _ in range(5):
            driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(1)

        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "listing__items"))
            )

            cards = driver.find_elements(By.CSS_SELECTOR, ".listing__items .card")
            propiedades = []

            for card in cards:
                try:
                    direccion = card.find_element(By.CSS_SELECTOR, "p.card__address").text.strip()
                except:
                    direccion = "No disponible"

                try:
                    precio_texto = card.find_element(By.CSS_SELECTOR, "p.card_price").text.strip()
                    precio = precio_texto.split('\n')[0]
                except:
                    precio = "No disponible"

                try:
                    expensas = card.find_element(By.CSS_SELECTOR, "span.card__expenses").text.strip()
                except:
                    expensas = "No disponibles"


                try:
                    superficie = card.find_element(By.CSS_SELECTOR, "li:has(i.icono-superficie_cubierta)").text.strip()
                except:
                    superficie = "No disponible"

                try:
                    dormitorios = card.find_element(By.CSS_SELECTOR, "li:has(i.icono-cantidad_dormitorios)").text.strip()
                except:
                    dormitorios = "No disponible"

                propiedades.append({
                    "Dirección": direccion,
                    "Precio": precio,
                    "Expensas": expensas,
                    "Superficie": superficie,
                    "Dormitorios": dormitorios
                })

            if propiedades:
                print(f"✅ {len(propiedades)} propiedades encontradas.")
                return propiedades
            else:
                print("😢 No se encontraron propiedades. Reintentando...")
                time.sleep(espera_entre_intentos)

        except Exception as e:
            print(f"⚠️ Error en intento {intento + 1}: {e}")
            time.sleep(espera_entre_intentos)

    print("❌ No se encontraron propiedades luego de varios intentos.\n")
    return []




