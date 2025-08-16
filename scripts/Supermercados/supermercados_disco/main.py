from scraping.navegador import crear_driver
from scraping.productos import obtener_productos_y_precios_disco
from utils.rendimiento import medir_recursos
from config import links_categorias
from utils.archivos import guardar_en_excel
import pandas as pd
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def main():
    categorias_fallidas_disco = []

    logger.info("===========INICIANDO SCRAPING DE DISCO===========")
    
    with medir_recursos():
        for url_categoria in links_categorias:
            logger.info(f"Scrapeando categoría {url_categoria}...")
            driver = crear_driver()
            driver.get(url_categoria)
            try:
                productos = obtener_productos_y_precios_disco(driver)
                guardar_en_excel(productos, url_categoria)        
            except Exception as e:
                logger.error(f"Error al procesar {url_categoria}: {e}")
                categorias_fallidas_disco.append(url_categoria)
            finally:
                driver.quit()

        if categorias_fallidas_disco:
            logger.info("Categorías que fallaron")
            for cat in categorias_fallidas_disco:
                print(f"- {cat}")
            pd.DataFrame(categorias_fallidas_disco, columns=["Categoría"]).to_csv("categorias_fallidas_disco.csv", index=False)
        else:
            logger.info("¡Todas las categorías se scrapearon correctamente!")
        
    logger.info("===========SCRAPING DE DISCO FINALIZADO===========")
    
if __name__ == "__main__":
    main()