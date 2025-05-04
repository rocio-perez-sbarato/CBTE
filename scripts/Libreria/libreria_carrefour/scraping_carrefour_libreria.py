from supermercados.supermercados_carrefour.scraping.productos import scrapear_categoria
from supermercados.supermercados_carrefour.utils.archivos import guardar_en_excel
from supermercados.supermercados_carrefour.utils.rendimiento import medir_recursos
from supermercados.supermercados_carrefour.scraping.navegador import crear_driver
from config import links_categorias
import pandas as pd 

# TODO: ver si puedo arreglar los imports y sino usar el scraping de supermercados

categorias_fallidas = []

print("===========\n")
print("🚀 INICIANDO SCRAPING DE LIBRERIA DE CARREFOUR")
print("===========\n")
    
with medir_recursos():
    for url_categoria in links_categorias:
        print("---------------\n")
        print(f"🕵️ Scrapeando categoría {url_categoria}")
        print("---------------\n")
        driver = crear_driver()

        try:
            productos = scrapear_categoria(driver, url_categoria)
            guardar_en_excel(productos, url_categoria)
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
print("😎 SCRAPING DE LIBRERIA DE CARREFOUR FINALIZADO")
print("===========\n")
    