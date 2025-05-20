from scraping.navegador import iniciar_driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_primer_plan_claro():
    """
    Extrae la primera oferta de megas y el precio de la página de Claro.
    """
    
    driver = iniciar_driver()

    try:
        # Abrir la página
        driver.get("https://www.claro.com.ar/personas/internet-wifi-telefonia-tv")
        
        # Esperar que los elementos de ofertas estén presentes antes de buscarlos
        ofertas = WebDriverWait(driver, 150).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'strong[tacc="headingMarkdown-strong"]'))
        )

        # Esperar que los elementos de ofertas estén presentes antes de buscarlos
        precios = WebDriverWait(driver, 150).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p[tacc="planCard-body-price"]'))
        )

        # Tomar solo el primero de cada lista (si existen)
        primera_oferta = ofertas[0].text if ofertas else "No encontrado"
        primer_precio = precios[0].text if precios else "No encontrado"

        driver.quit()
        return {"Compañía": "Claro", "oferta": primera_oferta, "precio": primer_precio}
        
    except Exception as e:
        print(f"Error Claro: {e}")
        return None

    finally:
        driver.quit()
