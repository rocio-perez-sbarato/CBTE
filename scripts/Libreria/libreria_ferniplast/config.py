# Definir la URL base y las categorías
base_url = "https://www.ferniplast.com/"
categorias_deseadas = ["libreria/marcadores-y-resaltadores/",
                        "libreria/escritura/boligrafos/",
                        "libreria/escritura/gomas-de-borrar/",
                        "libreria/escritura/lapices-negros/",
                        "libreria/cuadernos/"]
# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat}" for cat in categorias_deseadas]
