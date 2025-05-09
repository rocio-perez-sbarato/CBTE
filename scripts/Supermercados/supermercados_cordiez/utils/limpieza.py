
def procesar_productos(productos):
    datos = []

    for producto in productos:
        nombre = producto.get("productName", "Desconocido")
        oferta = producto.get("clusterHighlights", {})
        en_oferta = "Si" if "624" in oferta else "No"

        try:
            seller = producto["items"][0]["sellers"][0]
            precio = seller["commertialOffer"]["Price"]
            disponible = seller["commertialOffer"]["IsAvailable"]
        except Exception:
            precio = "Error"
            disponible = False

        disponibilidad = "Si" if disponible and precio not in [0, "Error"] else "No"
        datos.append([nombre, precio, en_oferta, disponibilidad])

    return datos