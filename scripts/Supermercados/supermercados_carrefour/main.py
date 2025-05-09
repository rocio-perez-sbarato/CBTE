from scraping.navegador import crear_driver
from scraping.productos import scrapear_categoria
from utils.rendimiento import medir_recursos
from utils.archivos import guardar_en_excel
from config import links_categorias
import pandas as pd
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def main():
        
    categorias_fallidas = []

    logger.info("===========INICIANDO SCRAPING DE CARREFOUR===========\n")
        
    with medir_recursos():
        for url_categoria in links_categorias:
            logger.info(f"Scrapeando categoría {url_categoria}...")
            driver = crear_driver()

            try:
                productos = scrapear_categoria(driver, url_categoria)
                guardar_en_excel(productos, url_categoria)
            except Exception as e:
                logger.critical(f"Error al procesar {url_categoria}: {e}")
                categorias_fallidas.append(url_categoria)
            finally:
                driver.quit()

    if categorias_fallidas:
        logger.info("Categorías que fallaron")
        for cat in categorias_fallidas:
            print(f"- {cat}")
        pd.DataFrame(categorias_fallidas, columns=["Categoría"]).to_csv("categorias_fallidas.csv", index=False)
    else:
        logger.info("¡Todas las categorías se escrapearon correctamente!")
        
    logger.info("===========SCRAPING DE CARREFOUR FINALIZADO===========")

if __name__ == "__main__":
    main()