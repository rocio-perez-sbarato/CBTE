import os
import datetime
import pandas as pd
from utils.limpieza import limpiar_url
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def agregar_fecha(nombre_base):
    """Agrega la fecha actual al nombre del archivo, respetando la extensión."""
    fecha_hoy = datetime.datetime.today().strftime("%d-%m-%Y")
    
    # Remover caracteres no válidos del nombre base (ejemplo: "/")
    nombre_base = nombre_base.replace("/", "_")
    
    # Separar la extensión
    nombre, extension = os.path.splitext(nombre_base)
    
    return f"{nombre}_{fecha_hoy}{extension}"

def guardar_en_excel(productos, url_categoria):
    """Guarda los productos en un archivo Excel con el nombre de la subcategoría."""
    if not productos:
        logger.info("No hay productos para guardar.")
        return

    # Ruta relativa para ir a la carpeta superior y luego a "data"
    directorio = os.path.abspath(os.path.join(".", "data/supermercados/carrefour"))

    os.makedirs(directorio, exist_ok=True) 

    nombre_categoria = limpiar_url(url_categoria)
    nombre_archivo = os.path.join(directorio, agregar_fecha(f"{nombre_categoria}.xlsx"))

    df = pd.DataFrame(productos)
    df.to_excel(nombre_archivo, index=False)

    logger.info(f"Datos guardados correctamente en '{nombre_archivo}'")