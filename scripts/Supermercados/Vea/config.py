# Definir la URL base y las categorías
base_url = "https://www.vea.com.ar/"
categorias_deseadas = ["almacen/aceites-y-vinagres/aceites-comunes"]

# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat.replace(' ', '-')}" for cat in categorias_deseadas]
