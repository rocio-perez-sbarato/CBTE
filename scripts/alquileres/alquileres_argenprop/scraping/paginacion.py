import time
from selenium.webdriver.common.by import By

# TODO: pensar como acceder al último botón

def obtener_hrefs_paginas(driver):
    """Obtiene los hrefs de los enlaces de las páginas de la paginación."""
    try:
        time.sleep(3)  # Asegurar que la página carga completamente

        # Buscar los botones de paginación
        paginas = driver.find_elements(By.CSS_SELECTOR, "ul.pagination.pagination--links li.pagination_page")

        # Extraer los hrefs de los enlaces
        hrefs = []
        for pagina in paginas:
            # Verificar si el <li> contiene un enlace <a>
            if pagina.find_elements(By.TAG_NAME, "a"):
                link = pagina.find_element(By.TAG_NAME, "a").get_attribute("href")
                hrefs.append(link)

        print(f"Enlaces de páginas detectados: {hrefs}")
        return hrefs

    except Exception as e:
        print(f"Error obteniendo los hrefs: {e}")
        return []

