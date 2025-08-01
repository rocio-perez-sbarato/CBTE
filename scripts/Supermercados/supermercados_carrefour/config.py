# Definir la URL base y las categorías
base_url = "https://www.carrefour.com.ar/"
categorias_deseadas = ["almacen/aceites-y-vinagres/vinagres-acetos-y-limon",

                        "Almacen/Pastas-secas/Fideos-largos",


                        "Almacen/Harinas/Harinas-comunes-y-leudantes",


                        "almacen/harinas/polentas",


                        "almacen/aceites-y-vinagres/aceites-comunes",


                        "lacteos-y-productos-frescos/dulce-de-membrillo-y-otros-dulces/dulce-de-batata",


                        "Lacteos-y-productos-frescos/Dulce-de-leche",


                        "lacteos-y-productos-frescos/huevos",


                        "Lacteos-y-productos-frescos/Leches",


                        "Lacteos-y-productos-frescos/Quesos",


                        "panaderia/panificados/panes-lacteados-y-de-mesa",


                        "Bebidas/Jugos/Jugos-en-polvo",


                        "soda",

                        "desayuno-y-merienda/cafe/cafe-instantaneo",


                        "desayuno-y-merienda/azucar-y-endulzantes/azucar",


                        "Desayuno-y-merienda/Infusiones/Te",


                        "Desayuno-y-merienda/Yerba",

                        "desayuno-y-merienda/galletitas-bizcochitos-y-tostadas",


                        "Desayuno-y-merienda/Mermeladas-y-otros-dulces/Mermeladas-dulces-y-jaleas",


                        "Limpieza/Lavandinas",


                        "Limpieza/Limpieza-de-cocina/Detergentes",

                        "Limpieza/Articulos-de-limpieza/Esponjas",


                        "Limpieza/Desodorantes-de-ambiente/Desodorantes-y-desinfectantes",


                        "Limpieza/Limpieza-de-pisos-y-muebles/Limpiadores-de-piso",


                        "Limpieza/Limpieza-de-la-ropa/Jabones-para-la-ropa",


                        "Limpieza/Limpieza-de-la-ropa/Suavizantes-para-la-ropa",


                        "Limpieza/Articulos-de-limpieza/Trapos-y-panos",


                        "Limpieza/Articulos-de-limpieza/Esponjas",


                        "limpieza/limpieza-de-cocina/limpiadores-cremosos",


                        "Limpieza/Papeles-higienicos",

                        "Perfumeria/Proteccion-femenina/Toallitas-femeninas",


                        "Perfumeria/Jabones/Jabones-en-barra",


                        "Perfumeria/Cuidado-dental/Pasta-dental",


                        "Perfumeria/Cuidado-del-cabello/Shampoos",


                        "Perfumeria/Cuidado-corporal/Afeitado",


                        "Perfumeria/Cuidado-del-cabello/Acondicionadores",

                        "Perfumeria/Antitranspirantes-y-desodorantes/En-aerosol",

                        "Perfumeria/Cuidado-dental/Cepillos-de-dientes",

                        "Carnes-y-pescados/Carne-vacuna",


                        "Carnes-y-pescados/Pollo-y-granja",

                        "Frutas-y-verduras/Verduras",


                        "Frutas-y-verduras/Frutas",


                        "bazar-y-textil/libreria/resmas-y-articulos-de-oficina",


                        "Bazar-y-textil/Libreria/Lapiceras-y-lapices",

                        "bazar-y-textil/libreria/accesorios-de-libreria"]

# Obtener los links de las categorías
links_categorias = [f"{base_url}{cat}" for cat in categorias_deseadas]