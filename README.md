# Scraping de precios
## Canasta Básica Estudiantil

- [Estructura del proyecto y avances](https://gitmind.com/app/docs/mss9thvm)

- [Sitios web y direcciones de mail a utilizar](https://docs.google.com/document/d/13MpGGDrN_KKaTUKt0wFvzooiDy8hsn8pJkmCBJO5_9s/edit?usp=sharing)

## Ejecución del scraping

1. Descargar código
   
> Andá al repositorio en GitHub. 
>Hacé clic en el botón verde que dice Code.
>Elegí la opción "Download ZIP".
>Descomprimí el archivo ZIP en tu computadora.

2. Ejecutar el archivo `run_scraping.bat`
> Abrí la carpeta del proyecto y hacer doble click en el archivo `run_scraping.bat`

## (OPCIONAL) Configuración de credenciales

Este proyecto utiliza la API de Google Drive para subir la carpeta data a la carpeta de drive del proyecto. 

**⚠️ Si no lo querés usar, tenés que comentar la linea que lo ejecuta en el archivo `run_all.py` en la carpeta `scripts`. Tiene que quedar así:**

```
# Lista de paths a cada main.py
scripts = [
    "alquileres/alquileres_argenprop/main.py",
    "alquileres/alquileres_lavoz/main.py",
    "libreria/libreria_ferniplast/main.py",
    "libreria/libreria_grafitti/main.py",
    "libreria/libreria_pencilbag/main.py",
    "supermercados/supermercados_carrefour/main.py",
    "supermercados/supermercados_cordiez/main.py",  
    "supermercados/supermercados_disco/main.py",
    "supermercados/supermercados_vea/main.py",
    "internet/main.py",
    "telefonia/main.py"
]
```

Para poder usarlo, tenés que

1. Ir a [Drive Sync](https://expertbeacon.com/how-to-upload-files-to-google-drive-with-python-in-2023/#google_vignette)
2. Seguir los pasos 1 y 2

