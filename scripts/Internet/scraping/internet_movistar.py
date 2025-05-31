from selenium import webdriver
from scraping.navegador import iniciar_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_primer_plan_movistar():
    """
    Extrae la oferta de gigas y el precio mensual de la página de Movistar.
    """
    
    driver = iniciar_driver()
    
    try:
        # Abrir la página
        driver.get("https://www.movistar.com.ar/productos-y-servicios/internet")

        # Esperar que carguen los elementos
        gigas_element = WebDriverWait(driver, 350).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js__nombre-plan.plan__gigas"))
        )
        precio_element = WebDriverWait(driver, 350).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price.js__precio-oferta"))
        )
        
        return {"Compañía": "Movistar", "oferta": gigas_element.text, "precio": precio_element.text}

    except Exception as e:
        print(f"Error Movistar: {e}")
        return None

    finally:
        driver.quit()