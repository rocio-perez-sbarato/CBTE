import re

def limpiar_precio(texto_precio):
    """
    Limpia el precio y lo convierte en número flotante (formato inglés).
    """
    if not texto_precio:
        return None
    # Eliminar signos de pesos, espacios, y reemplazar puntos de miles por nada
    precio_limpio = texto_precio.replace("$", "")
    return precio_limpio

def limpiar_oferta(oferta):
    """Elimina todas las letras y deja solo los números en la oferta."""
    numeros = re.findall(r"\d+", oferta)  # Buscar solo números
    return " ".join(numeros) if numeros else ""  # Unir números separados por espacios
