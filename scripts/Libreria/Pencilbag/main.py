from scraping.navegador import crear_driver
from scraping.paginacion import obtener_total_paginas
from utils.rendimiento import medir_recursos
from utils.archivos import guardar_en_excel
from config import links_categorias
import pandas as pd

categorias_fallidas = []

print("===========\n")
print("🚀 INICIANDO SCRAPING DE PENCILBAG")
print("===========\n")
    
with medir_recursos():
    for url_categoria in links_categorias:
        print("---------------\n")
        print(f"🕵️  Scrapeando categoría {url_categoria}")
        print("---------------\n")
        driver = crear_driver()
        driver.get(url_categoria)
        try:
            total = obtener_total_paginas(driver)
        except Exception as e:
            print(f"😢 Error al procesar {url_categoria}: {e}")
            categorias_fallidas.append(url_categoria)
        finally:
            driver.quit()

if categorias_fallidas:
    print("---------------\n")
    print("🚨 Categorías que fallaron")
    print("---------------\n")
    for cat in categorias_fallidas:
        print(f"- {cat}")
    pd.DataFrame(categorias_fallidas, columns=["Categoría"]).to_csv("categorias_fallidas.csv", index=False)
else:
    print("\n✅ ¡Todas las categorías se escrapearon correctamente!")
    
print("===========\n")
print("😎 SCRAPING DE PENCILBAG FINALIZADO")
print("===========\n")