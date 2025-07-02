# Definir la URL base y las categorías
base_url = "https://www.carrefour.com.ar/"
categorias_deseadas = ["almacen/aceites-y-vinagres/vinagres-acetos-y-limon",
                        "Almacen/Pastas-secas/Fideos-largos",
                        "desayuno-y-merienda/cafe/cafe-instantaneo",
                        "desayuno-y-merienda/galletitas-bizcochitos-y-tostadas",
                        "Limpieza/Articulos-de-limpieza/Esponjas",
                        "Perfumeria/Proteccion-femenina/Toallitas-femeninas",
                        "Perfumeria/Antitranspirantes-y-desodorantes/En-aerosol",
                        "Perfumeria/Cuidado-dental/Cepillos-de-dientes",
                        "Carnes-y-pescados/Carne-vacuna",
                        "Frutas-y-verduras/Verduras",
                        "bazar-y-textil/libreria/accesorios-de-libreria"]

# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat}" for cat in categorias_deseadas]