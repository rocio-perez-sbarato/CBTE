from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.firefox.options import Options

def crear_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)

# Ir a una categoría con paginación
driver = crear_driver()
driver.get("https://pencilbaglibreria.com.ar/escritura1/resaltadores1/")
time.sleep(3)

# Hacer scroll hasta 600px
driver.execute_script("window.scrollTo(0, 600);")
time.sleep(2)

try:
    # Esperar el contenedor más específico
    contenedor = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "div.row.justify-content-center.align-items-center.my-4"
        ))
    )

    print("🧱 Contenedor encontrado:")
    print(contenedor.get_attribute("outerHTML"))

    spans = contenedor.find_elements(By.TAG_NAME, "span")
    print("\n📌 Contenido de los spans:")
    for span in spans:
        print("-", span.text.strip())

except Exception as e:
    print(f"❌ Error: {e}")

driver.quit()
