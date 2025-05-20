import re
from urllib.parse import urlparse

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
                producto["Precio original"] == "No disponible"):
            productos_filtrados.append(producto)

    return productos_filtrados

def limpiar_url(url):
    """Genera un nombre de archivo solo a partir de las categorías en el path de la URL."""
    parsed_url = urlparse(url)
    
    # Tomar solo el path (por ejemplo: "/libreria/marcadores-y-resaltadores")
    categorias = parsed_url.path.strip("/")

    # Reemplazar barras por guiones bajos y limpiar caracteres inválidos
    nombre_base = re.sub(r'[\\/:"*?<>|]', '_', categorias)

    return nombre_base