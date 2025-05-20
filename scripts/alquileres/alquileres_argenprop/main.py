from scraping.navegador import crear_driver
from scraping.alquileres import scrapear_pagina
from config import base_url
from utils.rendimiento import medir_recursos
from utils.archivos import guardar_en_excel
import logging
import logging.config

logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')

def main():
    logger.info("===========INICIANDO SCRAPING DE ARGENPROP===========\n")

    with medir_recursos():
        logger.info(f"Scrapeando los alquileres en {base_url}")
    
        try:
            driver = crear_driver()
            logger.info("Driver creado.")
            
            logger.info("Iniciando el scraping...")
            deptos = scrapear_pagina(driver, base_url)
            logger.info(f"Se obtuvieron {len(deptos)} departamentos.")

            logger.info("Guardando resultados en Excel...")
            guardar_en_excel(deptos, base_url)
            logger.info("¡Todas los deptos se escrapearon y guardaron correctamente!")

        except Exception as e:
            logger.error(f"Error al procesar {base_url}: {e}")

        finally:
            driver.quit()
            logger.info("Driver cerrado.")

    logger.info("===========SCRAPING DE ARGENPROP FINALIZADO===========\n")

if __name__ == "__main__":
    main()

