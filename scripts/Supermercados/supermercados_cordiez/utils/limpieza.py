def formatear_precio(precio):
    partes = f"{precio:,.2f}".split(".")
    entero = partes[0].replace(",", ".")  # cambiar separador de miles de coma a punto
    decimal = partes[1]  # los decimales ya están con coma
    return f"{entero},{decimal}"

def procesar_productos(productos):
    datos = []

    for producto in productos:
        nombre = producto.get("productName", "Desconocido")
        oferta = producto.get("clusterHighlights", {})
        en_oferta = "Si" if "624" in oferta else "No"

        try:
            seller = producto["items"][0]["sellers"][0]
            precio = seller["commertialOffer"]["Price"]
            precio_formateado = formatear_precio(precio)
            disponible = seller["commertialOffer"]["IsAvailable"]
        except Exception:
            precio = "Error"
            disponible = False

        disponibilidad = "Si" if disponible and precio not in [0, "Error"] else "No"
        datos.append([nombre, precio_formateado, en_oferta, disponibilidad])

    return datos