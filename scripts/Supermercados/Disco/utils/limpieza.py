import re

def filtrar_productos(productos):
    """Filtra los productos que son 'slider' o tienen todos los atributos 'No disponible'."""
    productos_filtrados = []
    for producto in productos:
        # Filtrar productos llamados 'slider' o con atributos 'No disponible'
        if "slider" not in producto["Producto"].lower() and \
           not (producto["Precio"] == "No disponible" and
                producto["Producto"] == "No disponible"):
            productos_filtrados.append(producto)

    return productos_filtrados

def limpiar_url(url):
    return re.sub(r"^https://www\.disco\.com\.ar/", "", url)