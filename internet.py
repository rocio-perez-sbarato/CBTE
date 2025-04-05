from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def iniciar_driver():
    """Configura y devuelve un WebDriver en modo headless."""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)


def obtener_primer_plan_movistar():
    """
    Extrae la oferta de megas y el precio mensual de la página de Movistar.
    """
    
    driver = iniciar_driver()
    
    try:
        # Abrir la página
        driver.get("https://www.movistar.com.ar/productos-y-servicios/internet")
        time.sleep(5)  # Esperar que cargue

        # Buscar el div con la clase que contiene los gigas
        gigas_element = driver.find_element(By.CLASS_NAME, "js__nombre-plan.plan__gigas")

        # Buscar el span con la clase que contiene el precio
        precio_element = driver.find_element(By.CLASS_NAME, "price.js__precio-oferta")
        
        return {"oferta_movistar": gigas_element.text, "precio_movistar": precio_element.text}

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        driver.quit()

def obtener_primer_plan_claro():
    """
    Extrae la primera oferta de megas y el precio de la página de Claro.
    """
    
    driver = iniciar_driver()

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

        return {"oferta_claro": primera_oferta, "precio_claro": primer_precio}

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        driver.quit()

plan_movistar = obtener_primer_plan_movistar()
plan_claro = obtener_primer_plan_claro()

if plan_movistar and plan_claro:
    print("----------Movistar\n")
    print(f"{plan_movistar['oferta_movistar']}")
    print(f"{plan_movistar['precio_movistar']}")
    print("----------Claro\n")
    print(f"{plan_claro['oferta_claro']}")
    print(f"{plan_claro['precio_claro']}")
else:
    print("No se pudo obtener la información.")



    