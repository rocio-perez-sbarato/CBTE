# TODO: Agregar todos los links
# Definir la URL base y las categorías
base_url = "https://www.graffittilibreria.com/"
categorias_deseadas = ["libreria-escolar/escritura1/lapiceras-y-boligrafos/",
                       "libreria-escolar/escritura1/fibras-y-marcadores/",
                       "libreria-escolar/gomas1/",
                       "artistica/lapices/"]
# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat}" for cat in categorias_deseadas]
