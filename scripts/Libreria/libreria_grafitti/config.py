# Definir la URL base y las categorías
base_url = "https://www.graffittilibreria.com/"
order = "?sort_by=price-ascending"
categorias_deseadas = ["libreria-escolar/escritura1/lapiceras-y-boligrafos/",
                        "libreria-escolar/escritura1/fibras-y-marcadores/",
                        "libreria-escolar/gomas1/",
                        "artistica/lapices/",
                        "libreria-escolar/cuadernos1/"]
# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat}{order}" for cat in categorias_deseadas]
