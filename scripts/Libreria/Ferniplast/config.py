# TODO: Agregar todos los links
# Definir la URL base y las categorías
base_url = "https://www.ferniplast.com/"
categorias_deseadas = ["libreria/marcadores-y-resaltadores?initialMap=c,c&initialQuery=libreria/marcadores-y-resaltadores&map=category-1,category-2,category-3&page=1&query=/libreria/marcadores-y-resaltadores/resaltadores-escolares&searchState",
                       "libreria/escritura/boligrafos",
                       "libreria/escritura/gomas-de-borrar",
                       "libreria/escritura/lapices-negros"]
# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat}" for cat in categorias_deseadas]
