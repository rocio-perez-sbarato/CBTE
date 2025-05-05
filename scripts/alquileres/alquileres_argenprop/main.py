from scraping.navegador import crear_driver
from scraping.productos import obtener_alquileres_y_precios_argenprop
from scraping.paginacion import obtener_hrefs_paginas
from config import base_url
from utils.rendimiento import medir_recursos
from utils.archivos import guardar_en_excel
import pandas as pd

# TODO: agregar logs

print("===========\n")
print("🚀 INICIANDO SCRAPING DE ARGENPROP")
print("===========\n")

with medir_recursos():
    print("---------------\n")
    print(f"🕵️ Scrapeando los alquileres en {base_url}")
    print("---------------\n")
    driver = crear_driver()
    driver.get(base_url)
    try:
        deptos = obtener_alquileres_y_precios_argenprop(driver)
        guardar_en_excel(deptos, base_url)    
        print("\n✅ ¡Todas los deptos se escrapearon correctamente!")
    except Exception as e:
        print(f"😢 Error al procesar {base_url}: {e}")
    finally:
        driver.quit()
    
print("===========\n")
print("😎 SCRAPING DE ARGENPROP FINALIZADO")
print("===========\n")