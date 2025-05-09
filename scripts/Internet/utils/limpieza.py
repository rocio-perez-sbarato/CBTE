import re

def limpiar_precio(precio):
    """Convierte el precio en un número uniforme eliminando símbolos y texto adicional."""
    precio = re.sub(r"[^\d]", "", precio)  # Eliminar todo excepto números
    return f"{int(precio)}"  # Agregar separador de miles

def limpiar_oferta(oferta):
    """Elimina todas las letras y deja solo los números en la oferta."""
    numeros = re.findall(r"\d+", oferta)  # Buscar solo números
    return " ".join(numeros) if numeros else ""  # Unir números separados por espacios
