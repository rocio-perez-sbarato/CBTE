from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import re
import datetime

# TODO: modularizar

def iniciar_driver():
    """Configura y devuelve un WebDriver en modo headless."""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)

def obtener_primer_plan_telefonia_personal():
    """
    Extrae la oferta de megas y el precio mensual de la página de Personal.
    """
    driver = iniciar_driver()
    
    # Abrir la página
    driver.get('https://www.personal.com.ar/planes-internet-movil?icn=planes&ici=homeperso_quicklinks') 

    wait = WebDriverWait(driver, 10)

    # Buscar el div con data-index="0"
    div_data_index_0 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-index="0"]'))
    )

    # Inicializar valores
    oferta = None
    precio = None

    # Buscar la oferta
    try:
        # En Telefonía, la oferta está en un <p class="title">
        title_element = div_data_index_0.find_element(By.CSS_SELECTOR, 'p.title')
        oferta = title_element.text.strip()
    except Exception:
        oferta = None

    # Buscar el precio
    try:
        price_container = div_data_index_0.find_element(By.CSS_SELECTOR, '.priceRichText span')
        precio = price_container.text.strip()
    except Exception:
        precio = None

    # Retornar todo como un diccionario
    return {
        'Compañía': 'Personal',
        'oferta': oferta,
        'precio': precio
    }

def obtener_primer_plan_telefonia_movistar(): 
    """
    Extrae la oferta de gigas y el precio mensual de la página de Movistar.
    """
    driver = iniciar_driver()
    
    try:
        # Abrir la página
        driver.get("https://tienda.movistar.com.ar/cambiodeplan/migra")

        # Esperar que carguen los elementos de telefonía
        gigas_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card-total-gigas"))
        )
        precio_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price-product"))
        )
        
        return {"Compañía": "Movistar", "oferta": gigas_element.text.strip(), "precio": precio_element.text.strip()}

    except Exception as e:
        print(f"Error Movistar: {e}")
        return None

    finally:
        driver.quit()

def obtener_primer_plan_telefonia_claro():
    """
    Extrae la primera oferta de gigas y el precio de la página de Claro.
    """
    driver = iniciar_driver()

    try:
        driver.get("https://www.claro.com.ar/personas/planes-prepago-pospago")
        
        # Buscar todas las ofertas que son <strong>
        oferta_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'strong[tacc="headingMarkdown-strong"]'))
        )

        # Buscar el primer texto que tenga "Gigas" o algún número
        primera_oferta = "No encontrado"
        for elem in oferta_elements:
            texto = elem.text.strip()
            if "Gigas" in texto or any(char.isdigit() for char in texto):
                primera_oferta = texto
                break

        # Buscar el precio normalmente
        precio_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[tacc="planCard-body-price-text"]'))
        )
        precio = precio_element.text.strip() if precio_element else "No encontrado"

        return {"Compañía": "Claro", "oferta": primera_oferta, "precio": precio}

    except Exception as e:
        print(f"Error Claro: {e}")
        return None

    finally:
        driver.quit()

def limpiar_precio(texto_precio):
    """
    Limpia el precio y lo convierte en número flotante (formato inglés).
    """
    if not texto_precio:
        return None
    # Eliminar signos de pesos, espacios, y reemplazar puntos de miles por nada
    precio_limpio = texto_precio.replace("$", "")
    return precio_limpio

def limpiar_oferta(oferta):
    """Elimina todas las letras y deja solo los números en la oferta."""
    numeros = re.findall(r"\d+(?:\.\d+)?", oferta) 
    return "".join(numeros) if numeros else ""  # Unir números separados por espacios

def agregar_fecha(nombre_base):
    """Agrega la fecha actual al nombre del archivo, respetando la extensión."""
    fecha_hoy = datetime.datetime.today().strftime("%d-%m-%Y")
    
    # Separar la extensión
    nombre, extension = os.path.splitext(nombre_base)
    
    return f"{nombre}_{fecha_hoy}{extension}"

def guardar_en_excel(datos):
    """Guarda los datos en un archivo xlsx dentro de la carpeta 'data'."""
    if datos:
        datos["oferta"] = limpiar_oferta(datos["oferta"])  # Unificar MB
        datos["precio"] = limpiar_precio(datos["precio"])  # Unificar formato de precio
        
        # Crear la carpeta si no existe
        carpeta = "data/telefonia"
        os.makedirs(carpeta, exist_ok=True)

        # Generar el nombre del archivo con la fecha
        archivo = os.path.join(carpeta, agregar_fecha("servicios_telefonia.xlsx"))

        # Guardar los datos en Excel
        df_nuevo = pd.DataFrame([datos], dtype=str)

        if os.path.exists(archivo):
            df_existente = pd.read_excel(archivo, dtype=str)
            df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
        else:
            df_final = df_nuevo

        df_final.to_excel(archivo, index=False)
        print(f"Datos guardados en {archivo}")
    else:
        print("No se guardaron datos, ocurrió un error.")


# Ejecutar y guardar los datos
plan_personal = obtener_primer_plan_telefonia_personal()
print(plan_personal)
guardar_en_excel(plan_personal)

plan_movistar = obtener_primer_plan_telefonia_movistar()
print(plan_movistar)
guardar_en_excel(plan_movistar)

plan_claro = obtener_primer_plan_telefonia_claro()
print(plan_claro)
guardar_en_excel(plan_claro)
