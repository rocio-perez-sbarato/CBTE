import re

def limpiar_nombre(nombre):
    """Elimina la palabra 'Producto' al inicio del nombre, con o sin espacio."""
    return re.sub(r"^Producto\s*", "", nombre)  # Quita 'Producto' + cualquier espacio opcional

def limpiar_precio(texto_precio):
    """
    Limpia el precio y deja solo el número.
    """
    if not texto_precio:
        return None
    # Eliminar signos de pesos, espacios, y reemplazar puntos de miles por nada
    precio_limpio = texto_precio.replace("$", "")
    return precio_limpio

def filtrar_productos(productos):
    """Filtra los productos que son 'slider' o tienen todos los atributos 'No disponible'."""
    productos_filtrados = []
    for producto in productos:
        # Filtrar productos llamados 'slider' o con atributos 'No disponible'
        if "slider" not in producto["Nombre del producto"].lower() and \
           not (producto["Precio final"] == "No disponible" and
                producto["Precio original"] == "No disponible" and
                producto["Beneficio Mi CRF"] == "No"):
            productos_filtrados.append(producto)

    return productos_filtrados

def limpiar_url(url):
    return re.sub(r"^https://www\.carrefour\.com\.ar/", "", url)