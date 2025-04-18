import requests
import datetime 
import math
import os
import pandas as pd

# TODO: definir qué hacer con los productos sin stock

def obtener_productos(url, headers, productos_por_pagina=10):
    productos_totales = []

    # Primer request para saber cuántos productos hay
    params = {"_from": "0", "_to": str(productos_por_pagina - 1), "O": "OrderByScoreDESC"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code not in [200, 206]:
        print(f"Error al obtener productos: {response.status_code}")
        return []

    if "resources" not in response.headers:
        print("No se encontró el header 'resources'.")
        return []

    total_productos = int(response.headers["resources"].split("/")[-1])
    print(f"Total de productos: {total_productos}")

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
            print(f"Error en página {pagina}: {response.status_code}")
            continue

        productos_totales.extend(response.json())

    return productos_totales

def procesar_productos(productos):
    datos = []
    for producto in productos:
        nombre = producto.get("productName", "Desconocido")
        precio = producto.get("items", [{}])[0].get("sellers", [{}])[0].get("commertialOffer", {}).get("Price", "Sin precio")
        cluster = producto.get("clusterHighlights", {})
        en_oferta = "Sí" if "624" in cluster else "No"
        datos.append([nombre, precio, en_oferta])
    return datos

def agregar_fecha(categoria):
    fecha = datetime.datetime.today().strftime("%d-%m-%Y")
    
    # Remover caracteres no válidos del nombre base (ejemplo: "/")
    categoria = categoria.replace("/", "_")
    
    return f"{categoria}_{fecha}.xlsx"

def guardar_en_excel(datos, ruta_archivo):
    """Guarda los productos en un archivo Excel con el nombre de la subcategoría."""
    if not datos:
        print("No hay productos para guardar.")
        return

    # Ruta relativa para ir a la carpeta superior y luego a "data"
    directorio = os.path.abspath(os.path.join(".", "data/cordiez"))

    os.makedirs(directorio, exist_ok=True) 

    nombre_categoria = agregar_fecha(ruta_archivo)
    nombre_archivo = os.path.join(directorio, nombre_categoria)

    df = pd.DataFrame(datos)
    df.to_excel(nombre_archivo, index=False)

    print(f"Datos guardados en '{nombre_archivo}'")

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

    for categoria in categorias:
        print(f"\nProcesando categoría: {categoria}")
        url = f"{base_url}{categoria}"
        
        productos = obtener_productos(url, headers)
        if not productos:
            print(f"No se encontraron productos en la categoría {categoria}.")
            continue

        datos = procesar_productos(productos)
        guardar_en_excel(datos, categoria)

        print(f"Total de productos en '{categoria}': {len(productos)}")

if __name__ == "__main__":
    main()


