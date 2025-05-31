import re
from urllib.parse import urlparse

def limpiar_precio(texto_precio):
    """
    Limpia el precio.
    """
    # Quitar espacios en blanco
    texto_precio = texto_precio.strip()
    
    # Quitar símbolos comunes (ejemplo $, €, %, espacios)
    for simbolo in ['$', '€', '%', ' ', '/mes']:
        texto_precio = texto_precio.replace(simbolo, '')
    
    # Quitar puntos de miles y cambiar coma decimal por punto
    texto_precio = texto_precio.replace('.', '').replace(',', '.')
    
    try:
        precio_float = float(texto_precio)
    except ValueError:
        precio_float = None  # O el valor que quieras poner si no se puede parsear
    
    # Formatear con 3 decimales para conservar ceros finales si querés string
    precio_formateado = f"{precio_float:.3f}" if precio_float is not None else None
    
    return precio_formateado

def limpiar_barrio(nombre):
    """Elimina la palabra 'Producto' al inicio del nombre, con o sin espacio."""
    barrio_cordoba = re.sub(r"^Departamento en Alquiler en*", "", nombre)  
    barrio = re.sub(r"^, Cordoba", "", barrio_cordoba)
    return barrio 

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
    """Genera un nombre de archivo solo a partir de las categorías en el path de la URL."""
    parsed_url = urlparse(url)
    
    # Tomar solo el path (por ejemplo: "/libreria/marcadores-y-resaltadores")
    categorias = parsed_url.path.strip("/")

    # Reemplazar barras por guiones bajos y limpiar caracteres inválidos
    nombre_base = re.sub(r'[\\/:"*?<>|]', '_', categorias)

    return nombre_base