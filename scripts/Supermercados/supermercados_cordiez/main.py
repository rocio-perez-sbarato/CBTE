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
                  "bebidas/jugos/jugos-en-polvo",
                  "almacen/arroz/arroz",
                  "almacen/harinas/harinas-de-trigo",
                  "almacen/harinas/harinas-de-maiz",
                  "almacen/sal/sal-fina",
                  "almacen/sal/sal-gruesa",
                  "almacen/vinagres/vinagres-de-alcohol",
                  "almacen/tomate-en-conservas/pure-de-tomates",
                  "almacen/conservas-de-vegetales/legumbres-en-bolsas",
                  "almacen/conservas-de-vegetales/legumbres-al-natural",
                  "carnes/carnes-vacunas",
                  "carnes/aves/carne-de-aves",
                  "pastas/pastas-secas/fideos",
                  "panaderia/panaderia/panificados-cordiez-elaborados",
                  "lacteos/leches",
                  "frutas-y-verduras/frutas",
                  "frutas-y-verduras/huevo",
                  "frutas-y-verduras/verduras",
                  "fiambres-y-quesos/untables",
                  "fiambres-y-quesos/quesos",
                  "fiambres-y-quesos/dulces-frescos/dulces",
                  "desayuno-y-merienda/azucar-y-edulcorante/azucar-comun",
                  "desayuno-y-merienda/cafe/cafe-instantaneo",
                  "desayuno-y-merienda/dulces-y-jaleas/dulces-de-leche",
                  "desayuno-y-merienda/dulces-y-jaleas/mermeladas-en-frasco",
                  "desayuno-y-merienda/galletas/galletas-dulces",
                  "desayuno-y-merienda/galletas/galletas-snacks",
                  "desayuno-y-merienda/infusiones/te",
                  "desayuno-y-merienda/yerbas/yerba",
                  "cuidado-personal/para-afeitar/rep-y-maq-de-afeitar",
                  "cuidado-personal/toallas-y-apositos/toallas-femeninas",
                  "cuidado-personal/shampoo-y-enjuague/shampoo",
                  "cuidado-personal/shampoo-y-enjuague/cremas-de-enjuague",
                  "cuidado-personal/jabones-y-cremas/jabones-de-tocador",
                  "cuidado-personal/desodorantes/desodorantes",
                  "cuidado-personal/cuidado-bucal/cepillos-de-dientes",
                  "cuidado-personal/cuidado-bucal/pasta-de-dientes",
                  "cuidado-de-la-ropa/jabon-en-polvo-liquido-y-en-barra/acondicionador-para-ropa",
                  "cuidado-de-la-ropa/jabon-en-polvo-liquido-y-en-barra/jabones-en-pan-p-lavar",
                  "cuidado-de-la-ropa/jabon-en-polvo-liquido-y-en-barra/detergentes-en-polvo",
                  "limpieza-y-hogar/desodorantes-de-ambiente/desodorantes-de-ambiente",
                  "limpieza-y-hogar/cuidado-del-hogar/agua-lavandina",
                  "limpieza-y-hogar/trapo-esponjas-y-guantes/fibras-y-esponjas",
                  "limpieza-y-hogar/lavavajillas/detergentes-liquidos",
                  "limpieza-y-hogar/banos-y-cocinas/limpiadores-liquidos",
                  "limpieza-y-hogar/papeles/papel-higienico",
                  "limpieza-y-hogar/trapo-esponjas-y-guantes/trapos-de-piso/"
                  ]
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


