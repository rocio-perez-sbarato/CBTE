# Definir la URL base y las categorías
base_url = "https://www.carrefour.com.ar/"
categorias_deseadas = ["Bazar-y-textil/Libreria/Lapiceras-y-lapices?initialMap=c,c,c&initialQuery=bazar-y-textil/libreria/lapiceras-y-lapices&map=category-1,category-2,category-3,tipo-de-producto,tipo-de-producto,tipo-de-producto&priceRange=881%20TO%2011951&query=/bazar-y-textil/libreria/lapiceras-y-lapices/lapicera/lapiz-de-grafito/resaltador&searchState",
                       "bazar-y-textil/libreria/accesorios-de-libreria/goma-de-borrar?map=category-1,category-2,category-3,tipo-de-producto"]
# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat.replace(' ', '-')}" for cat in categorias_deseadas]
