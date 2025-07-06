# Definir la URL base y las categorías
base_url = "https://www.carrefour.com.ar/"
categorias_deseadas = ["Desayuno-y-merienda/Galletitas-bizcochitos-y-tostadas/Galletitas-dulces"]

# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat}" for cat in categorias_deseadas]