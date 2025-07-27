
from scraping.navegador import crear_driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

driver = crear_driver()

# Ir a la página
url = 'https://www.plataforma10.com.ar/servicios/buscar-pasajes/Cordoba/Villa-Huidobro/19/773/31-07-2025/_/1/0/0'
driver.get(url)

# Esperar a que cargue el contenido dinámico
time.sleep(6)

# Seleccionar todas las tarjetas de resultados
cards = driver.find_elements(By.CSS_SELECTOR, ".searchResultCard_card__5Avpr")

for card in cards:
    
    try:
        # Empresa (alt del logo dentro del contenedor de empresa)
        img = card.find_element(By.CSS_SELECTOR, 'div[class*="content-company"] img')
        company_name = img.get_attribute("alt").strip()
    except:
        company_name = "Empresa no encontrada"
        
    try:
        # Extraer precio (p. ej., "$ 19.000")
        price_element = card.find_element(By.CSS_SELECTOR, ".searchResultCard_card__price__OPhFJ")
        price = price_element.text.strip()
        print(f"Empresa: {company_name} , Precio: {price}")
    except Exception as e:
        print("Error en una tarjeta:", e)

driver.quit()