from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import re
import datetime

def iniciar_driver():
    """Configura y devuelve un WebDriver en modo headless."""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)


def obtener_primer_plan_movistar():
    """
    Extrae la oferta de megas y el precio mensual de la página de Movistar.
    """
    
    driver = iniciar_driver()
    
    try:
        # Abrir la página
        driver.get("https://www.movistar.com.ar/productos-y-servicios/internet")

        # Esperar que carguen los elementos
        gigas_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js__nombre-plan.plan__gigas"))
        )
        precio_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price.js__precio-oferta"))
        )
        
        return {"Compañía": "Movistar", "oferta": gigas_element.text, "precio": precio_element.text}

    except Exception as e:
        print(f"Error Movistar: {e}")
        return None

    finally:
        driver.quit()

def obtener_primer_plan_claro():
    """
    Extrae la primera oferta de megas y el precio de la página de Claro.
    """
    
    driver = iniciar_driver()

    try:
        # Abrir la página
        driver.get("https://www.claro.com.ar/personas/internet-wifi-telefonia-tv")
        
        # Esperar que los elementos de ofertas estén presentes antes de buscarlos
        ofertas = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'strong[tacc="headingMarkdown-strong"]'))
        )

        # Esperar que los elementos de ofertas estén presentes antes de buscarlos
        precios = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p[tacc="planCard-body-price"]'))
        )

        # Tomar solo el primero de cada lista (si existen)
        primera_oferta = ofertas[0].text if ofertas else "No encontrado"
        primer_precio = precios[0].text if precios else "No encontrado"

        return {"Compañía": "Claro", "oferta": primera_oferta, "precio": primer_precio}

    except Exception as e:
        print(f"Error Claro: {e}")
        return None

    finally:
        driver.quit()

def limpiar_precio(precio):
    """Convierte el precio en un número uniforme eliminando símbolos y texto adicional."""
    precio = re.sub(r"[^\d]", "", precio)  # Eliminar todo excepto números
    return f"{int(precio):,}"  # Agregar separador de miles

def limpiar_oferta(oferta):
    """Elimina todas las letras y deja solo los números en la oferta."""
    numeros = re.findall(r"\d+", oferta)  # Buscar solo números
    return " ".join(numeros) if numeros else ""  # Unir números separados por espacios

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
        carpeta = "data"
        os.makedirs(carpeta, exist_ok=True)

        # Generar el nombre del archivo con la fecha
        archivo = os.path.join(carpeta, agregar_fecha("servicios_internet.xlsx"))

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
plan_movistar = obtener_primer_plan_movistar()
print(plan_movistar)
guardar_en_excel(plan_movistar)

plan_claro = obtener_primer_plan_claro()
print(plan_claro)
guardar_en_excel(plan_claro)



    