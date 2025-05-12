# Canasta Básica Social Estudiantil

- [Estructura del proyecto y avances](https://gitmind.com/app/docs/mss9thvm)

- [Sitios web y direcciones de mail a utilizar](https://docs.google.com/document/d/13MpGGDrN_KKaTUKt0wFvzooiDy8hsn8pJkmCBJO5_9s/edit?usp=sharing)

## Ejecución del scraping

Desde la raíz del directorio, escribir en la terminal 

```
python scripts/run_all.py
```
y esperar aproximadamente 4 horas.

En caso de que se busque realizar el scraping de uno de los módulos, escribir en la terminal

```
python scripts/<categoria>/<subcategoria>/main.py
```
Por ejemplo, `python scripts/alquileres/alquileres_argenprop/main.py`

## (OPCIONAL) Configuración de credenciales

Este proyecto utiliza la API de Google Drive para subir la carpeta data a la carpeta de drive del proyecto. Para poder usarlo, tenés que

1. Ir a [Drive Sync](https://expertbeacon.com/how-to-upload-files-to-google-drive-with-python-in-2023/#google_vignette)
2. Seguir los pasos 1 y 2

**Si no lo querés usar, podés comentar la linea que lo ejecuta en el archivo `run_all.py` en la carpeta `scripts`**

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
    "telefonia/main.py",
    "upload_to_drive.py"
]
```