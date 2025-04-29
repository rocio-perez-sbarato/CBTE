# Definir la URL base y las categorías
base_url = "https://www.disco.com.ar/"
categorias_deseadas = ["almacen/aceites-y-vinagres/aceites-comunes",
                       "almacen/aceites-y-vinagres/vinagres",
                       "almacen/arroz-y-legumbres/arroz"]

# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat.replace(' ', '-')}" for cat in categorias_deseadas]
