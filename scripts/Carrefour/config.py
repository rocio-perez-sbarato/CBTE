# Definir la URL base y las categorías
base_url = "https://www.carrefour.com.ar/"
categorias_deseadas = ["almacen/sal-aderezos-y-saborizadores/sal",
                       "desayuno-y-merienda/cafe/cafe-instantaneo",
                       "desayuno-y-merienda/azucar-y-endulzantes/azucar",
                       "almacen/aceites-y-vinagres/aceites-comunes",
                       "lacteos-y-productos-frescos/dulce-de-membrillo-y-otros-dulces/dulce-de-batata",
                       "Lacteos-y-productos-frescos/Dulce-de-leche",
                       "Bebidas/Jugos/Jugos-en-polvo",
                       "soda",
                       "Desayuno-y-merienda/Infusiones/Te",
                       "almacen/aceites-y-vinagres/vinagres-acetos-y-limon",
                       "Desayuno-y-merienda/Yerba",
                       "Desayuno-y-merienda/Mermeladas-y-otros-dulces/Mermeladas-dulces-y-jaleas"]
# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat.replace(' ', '-')}" for cat in categorias_deseadas]
