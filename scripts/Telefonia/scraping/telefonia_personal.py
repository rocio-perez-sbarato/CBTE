from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.navegador import iniciar_driver

def obtener_primer_plan_telefonia_personal():
    """
    Extrae la oferta de megas y el precio mensual de la página de Personal.
    """
    driver = iniciar_driver()
    
    # Abrir la página
    driver.get('https://www.personal.com.ar/planes-internet-movil?icn=planes&ici=homeperso_quicklinks') 

    wait = WebDriverWait(driver, 150)

    # Buscar el div con data-index="0"
    div_data_index_0 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-index="0"]'))
    )

    # Inicializar valores
    oferta = None
    precio = None

    # Buscar la oferta
    try:
        # En Telefonía, la oferta está en un <p class="title">
        title_element = div_data_index_0.find_element(By.CSS_SELECTOR, 'p.title')
        oferta = title_element.text.strip()
    except Exception:
        oferta = None

    # Buscar el precio
    try:
        price_container = div_data_index_0.find_element(By.CSS_SELECTOR, '.priceRichText span')
        precio = price_container.text.strip()
    except Exception:
        precio = None
        
    driver.quit()
    # Retornar todo como un diccionario
    return {
        'Compañía': 'Personal',
        'oferta (GB)': oferta,
        'precio': precio
    }