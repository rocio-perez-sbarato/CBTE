from scraping.productos import obtener_productos
from utils.archivos import guardar_en_excel
from utils.limpieza import procesar_productos
from utils.rendimiento import medir_recursos
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

# TODO: pasar formato de precios a inglés

def main():
    categorias = ["almacen/sal/sal-fina", 
                  "bebidas/aguas/sodas",
                  "bebidas/jugos/jugos-en-polvo"]
    base_url = "https://www.cordiez.com.ar/api/catalog_system/pub/products/search/"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Sec-Fetch-Mode": "cors"
    }

    logger.info("===========INICIANDO SCRAPING DE CORDIEZ===========")
    with medir_recursos():
        for categoria in categorias:
            logger.info(f"Scrapeando categoría {categoria}...")
            url = f"{base_url}{categoria}"
            
            productos = obtener_productos(url, headers)
            if not productos:
                logger.critical(f"No se encontraron productos en la categoría {categoria}")
                continue

            datos = procesar_productos(productos)
            guardar_en_excel(datos, categoria)

            logger.info(f"* {len(productos)} productos en '{categoria}'")
    
    logger.info("===========SCRAPING DE CORDIEZ FINALIZADO===========")

if __name__ == "__main__":
    main()


