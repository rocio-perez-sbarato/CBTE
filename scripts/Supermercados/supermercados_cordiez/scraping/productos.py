import requests
import math 
import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def obtener_productos(url, headers, productos_por_pagina=10):
    productos_totales = []

    # Primer request para saber cuántos productos hay
    params = {"_from": "0", "_to": str(productos_por_pagina - 1), "O": "OrderByScoreDESC"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code not in [200, 206]:
        logger.error(f"Error al obtener productos: {response.status_code}")
        return []

    if "resources" not in response.headers:
        logger.info("No se encontró el header 'resources'.")
        return []

    total_productos = int(response.headers["resources"].split("/")[-1])
    logger.info(f"Total de productos: {total_productos}")

    productos_totales.extend(response.json())

    # Si ya los obtuvimos todos en la primera request, terminamos
    if total_productos <= productos_por_pagina:
        return productos_totales

    # Si hay más, seguimos scrapendo el resto
    total_paginas = math.ceil(total_productos / productos_por_pagina)

    for pagina in range(1, total_paginas):
        from_index = pagina * productos_por_pagina
        to_index = from_index + productos_por_pagina - 1
        params = {"_from": str(from_index), "_to": str(to_index), "O": "OrderByScoreDESC"}

        response = requests.get(url, params=params, headers=headers)
        if response.status_code not in [200, 206]:
            logger.error(f"Error en página {pagina}: {response.status_code}")
            continue

        productos_totales.extend(response.json())

    return productos_totales