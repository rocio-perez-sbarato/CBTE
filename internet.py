from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def obtener_primer_plan_movistar(driver):
    """
    Extrae la oferta de megas y el precio mensual de la página de Personal.
    """

    try:
        # Abrir la página
        driver.get("https://www.personal.com.ar/internet")
        time.sleep(5)  # Esperar que cargue

        # Obtener todos los <h2> con la clase de oferta
        ofertas = driver.find_elements(By.CLASS_NAME, "CardComponent_title_beVVt")

        # Obtener todos los <div> con la clase de precio
        precios = driver.find_elements(By.CLASS_NAME, "CardComponent_priceRichText_WuzS7")

        # Tomar solo el primero de cada lista (si existen)
        primera_oferta = ofertas[0].text if ofertas else "No encontrado"
        primer_precio = precios[0].text if precios else "No encontrado"

        return {"oferta": primera_oferta, "precio": primer_precio}

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Cerrar navegador
        driver.quit()

def obtener_primer_plan_claro(driver):
    """
    Extrae la primera oferta de megas y el precio de la página de Claro.

    Retorna:
    - Un diccionario con la oferta y el precio.
    """

    try:
        # Abrir la página
        driver.get("https://www.claro.com.ar/personas/internet-wifi-telefonia-tv")
        time.sleep(5)  # Esperar que cargue

        # Obtener todas las ofertas de megas
        ofertas = driver.find_elements(By.CSS_SELECTOR, 'strong[tacc="headingMarkdown-strong"]')

        # Obtener todos los precios
        precios = driver.find_elements(By.CSS_SELECTOR, 'p[tacc="planCard-body-price"]')

        # Tomar solo el primero de cada lista (si existen)
        primera_oferta = ofertas[0].text if ofertas else "No encontrado"
        primer_precio = precios[0].text if precios else "No encontrado"

        return {"oferta": primera_oferta, "precio": primer_precio}

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Cerrar navegador
        driver.quit()

# Configuración de Selenium con Firefox en modo headless
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# 📌 Ejemplo de uso:
plan_movistar = obtener_primer_plan_movistar(driver)
plan_claro = obtener_primer_plan_movistar(driver)

# Imprimir el resultado
if plan_movistar and plan_claro:
    print("----------Movistar\n")
    print(f"{plan_movistar['oferta']}")
    print(f"{plan_movistar['precio']}")
    print("----------Claro\n")
    print(f"{plan_claro['oferta']}")
    print(f"{plan_claro['precio']}")
else:
    print("No se pudo obtener la información.")



    