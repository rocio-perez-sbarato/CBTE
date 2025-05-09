import os
import datetime 
import pandas as pd
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def agregar_fecha(categoria):
    fecha = datetime.datetime.today().strftime("%d-%m-%Y")
    
    # Remover caracteres no válidos del nombre base (ejemplo: "/")
    categoria = categoria.replace("/", "_")
    
    return f"{categoria}_{fecha}.xlsx"

def guardar_en_excel(datos, ruta_archivo):
    """Guarda los productos en un archivo Excel con el nombre de la subcategoría."""
    if not datos:
        logger.info("No hay productos para guardar.")
        return

    # Ruta relativa para ir a la carpeta superior y luego a "data"
    directorio = os.path.abspath(os.path.join(".", "data/supermercados/cordiez"))

    os.makedirs(directorio, exist_ok=True) 

    nombre_categoria = agregar_fecha(ruta_archivo)
    nombre_archivo = os.path.join(directorio, nombre_categoria)

    df = pd.DataFrame(datos, columns=["Nombre", "Precio", "Oferta", "Disponible"])
    df.to_excel(nombre_archivo, index=False)

    logger.info(f"Datos guardados correctamente en '{nombre_archivo}'")