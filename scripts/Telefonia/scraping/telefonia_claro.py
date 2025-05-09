from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.navegador import iniciar_driver

def obtener_primer_plan_telefonia_claro():
    """
    Extrae la primera oferta de gigas y el precio de la página de Claro.
    """
    driver = iniciar_driver()

    try:
        driver.get("https://www.claro.com.ar/personas/planes-prepago-pospago")
        
        # Buscar todas las ofertas que son <strong>
        oferta_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'strong[tacc="headingMarkdown-strong"]'))
        )

        # Buscar el primer texto que tenga "Gigas" o algún número
        primera_oferta = "No encontrado"
        for elem in oferta_elements:
            texto = elem.text.strip()
            if "Gigas" in texto or any(char.isdigit() for char in texto):
                primera_oferta = texto
                break

        # Buscar el precio normalmente
        precio_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[tacc="planCard-body-price-text"]'))
        )
        precio = precio_element.text.strip() if precio_element else "No encontrado"

        return {"Compañía": "Claro", "oferta": primera_oferta, "precio": precio}

    except Exception as e:
        print(f"Error Claro: {e}")
        return None

    finally:
        driver.quit()