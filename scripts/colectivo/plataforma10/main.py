
from scraping.navegador import crear_driver
from config import destinos, datos, pagina
from scraping.pasajes import obtener_precios_pasajes_plataforma10
from utils.archivos import guardar_en_excel
import logging 
import logging.config 


logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def main():

    logger.info("===========INICIANDO SCRAPING DE PLATAFORMA10 ===========\n")

    for lugar in destinos: 
        link_destino = pagina + lugar + datos
        logger.info(f"Scrapeando {link_destino}...\n")
        try:
            driver = crear_driver()
            pasajes = obtener_precios_pasajes_plataforma10(driver, link_destino, lugar)
            guardar_en_excel(pasajes, lugar)
        except Exception as e:
            logger.critical(f"La fecha o destino no están disponibles {link_destino}: {e}")
        finally:
            driver.quit()
    
    logger.info("===========SCRAPING DE PLATAFORMA10 FINALIZADO===========")


if __name__ == "__main__":
    main()
