import re

def limpiar_precio(texto_precio):
    """
    Limpia el precio.
    """
    # Quitar espacios en blanco
    texto_precio = texto_precio.strip()
    
    # Quitar símbolos comunes (ejemplo $, €, %, espacios)
    for simbolo in ['$', '€', '%', ' ', '/mes', 'c/u']:
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

def limpiar_precio_kg_lt(texto):
    """Extrae el precio por kg/lt desde un string y lo devuelve como string con 3 decimales."""
    match = re.search(r"\$?\s*([\d\.,]+)", texto)
    if match:
        numero_str = match.group(1).replace('.', '').replace(',', '.')
        try:
            precio_float = float(numero_str)
            return f"{precio_float:.3f}"
        except ValueError:
            return "No disponible"
    return "No disponible"

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
    return re.sub(r"^https://www\.vea\.com\.ar/", "", url)