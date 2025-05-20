from scraping.navegador import iniciar_driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_primer_plan_personal():
    """
    Extrae la oferta de megas y el precio mensual de la página de Personal.
    """
    driver = iniciar_driver()
    
    # Abrir la página
    driver.get('https://www.personal.com.ar/internet') 

    wait = WebDriverWait(driver, 150)

    # Buscar solo el div con data-index="0"
    div_data_index_0 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-index="0"]'))
    )

    # Inicializar valores
    oferta = None
    precio = None

    # Buscar la oferta
    try:
        # Hay dos h2: uno para "Internet 300 MB" y otro para "Flow Full sin deco"
        h2_elements = div_data_index_0.find_elements(By.CSS_SELECTOR, 'h2')
        oferta = ' + '.join(h2.text.strip() for h2 in h2_elements if h2.text.strip())
    except Exception:
        oferta = None

    # Buscar el precio
    try:
        price_container = div_data_index_0.find_element(By.CSS_SELECTOR, '.CardComponent_priceRichText__WuzS7 span')
        precio = price_container.text.strip()
    except Exception:
        precio = None

    driver.quit()
    # Retornar todo como un diccionario
    return {
        "Compañía": "Personal", 
        'oferta': oferta,
        'precio': precio
    }