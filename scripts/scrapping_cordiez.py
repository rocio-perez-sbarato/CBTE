import requests
import pandas as pd

# TO DO: automatizar el cálculo de páginas, nombre de archivo con fecha,
# guardar excel carpeta del super, iterar en categorías  

def obtener_productos(url, headers, num_paginas=10, productos_por_pagina=18):
    productos_totales = []
    
    for pagina in range(num_paginas):  
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

def guardar_en_excel(datos, nombre_archivo="productos.xlsx"):
    df = pd.DataFrame(datos, columns=["Nombre", "Precio", "Oferta"])
    df.to_excel(nombre_archivo, index=False)

def main():
    url = "https://www.cordiez.com.ar/api/catalog_system/pub/products/search/almacen"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Sec-Fetch-Mode": "cors"
    }
    
    productos = obtener_productos(url, headers)
    datos = procesar_productos(productos)
    guardar_en_excel(datos)
    
    print(f"\nTotal de productos obtenidos: {len(productos)}")

if __name__ == "__main__":
    main()


