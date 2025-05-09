from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.navegador import iniciar_driver

def obtener_primer_plan_telefonia_movistar(): 
    """
    Extrae la oferta de gigas y el precio mensual de la página de Movistar.
    """
    driver = iniciar_driver()
    
    try:
        # Abrir la página
        driver.get("https://tienda.movistar.com.ar/cambiodeplan/migra")

        # Esperar que carguen los elementos de telefonía
        gigas_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card-total-gigas"))
        )
        precio_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price-product"))
        )
        
        return {"Compañía": "Movistar", "oferta": gigas_element.text.strip(), "precio": precio_element.text.strip()}

    except Exception as e:
        print(f"Error Movistar: {e}")
        return None

    finally:
        driver.quit()
