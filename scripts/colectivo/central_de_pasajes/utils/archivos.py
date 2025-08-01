import os
import datetime 
import pandas as pd
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def agregar_fecha(destino):
    fecha = datetime.datetime.today().strftime("%d-%m-%Y")
    
    # Remover caracteres no válidos del nombre base (ejemplo: "/")
    destino = destino.replace("/", "_")
    
    return f"{destino}_{fecha}.xlsx"

def dict_en_excel(datos, ruta_archivo):
    """Guarda los productos en un archivo Excel con el nombre de la subcategoría."""
    if not datos:
        logger.info("No hay productos para guardar.")
        return

    # Ruta relativa para ir a la carpeta superior y luego a "data"
    directorio = os.path.abspath(os.path.join(".", "data/colectivos/central de pasajes"))

    os.makedirs(directorio, exist_ok=True) 

    nombre_categoria = agregar_fecha(ruta_archivo)
    nombre_archivo = os.path.join(directorio, nombre_categoria)

    df = pd.DataFrame(datos, columns=["Origen", "Destino", "Empresa", "Precio"])
    df.to_excel(nombre_archivo, index=False)

    logger.info(f"Datos guardados correctamente en '{nombre_archivo}'")