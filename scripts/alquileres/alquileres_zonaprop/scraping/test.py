from selenium import webdriver
from selenium.webdriver.common.by import By
from navegador import crear_driver
import time

driver = crear_driver()
driver.get("https://www.zonaprop.com.ar/departamentos-alquiler.html")

time.sleep(5)  # Esperar que cargue la página

# Buscar todas las tarjetas de publicaciones
cards = driver.find_elements(By.CLASS_NAME, "postingCardLayout-module__posting-card-layout")
print(cards)
for card in cards:
    try:
        titulo = card.find_element(By.CLASS_NAME, "postingLocations-module__location-address").text
    except:
        titulo = "Sin título"

    try:
        precio = card.find_element(By.CLASS_NAME, "postingPrices-module__price").text
    except:
        precio = "Sin precio"

    print(f"{titulo} - {precio}")

driver.quit()
