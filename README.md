## Canasta Básica Total Estudiantil
### Elaborado por y para estudiantes

- [📄 **Leer Informe julio 2025**](https://github.com/usuario/nombre-repo/archive/refs/heads/main.zip)
- [📚 **Leer informes anteriores**](https://github.com/usuario/nombre-repo/releases)
- [✉️ **Unirme a la lista de mails**](https://example.com/lista-mails)

### JULIO 2025 

## Perfiles de consumo y gastos mensuales

| 🛒 Caso | Monto estimado |
|--------|----------------|
| Estudiante que vive en un departamento alquilado | **$750k** |
| Estudiante que vive en residencia universitaria | **$500k** |
| Estudiante que vive con su grupo familiar y no es el principal aportante | **$350k** |

## Proyecto de investigación

Accedé al [proyecto](https://sociales.unc.edu.ar/) para conocer qué es y cómo medimos la canasta básica.

## Contacto

¿Querés participar o tenés alguna consulta? Mandanos un mail a **_canasta.basica@gmail.com_**.

## Equipo

Somos estudiantes de la [Facultad de Ciencias Sociales](https://sociales.unc.edu.ar/) y de la [Facultad de Matemática, Astronomía, Física y Computación](https://www.famaf.unc.edu.ar/).

## Nota 

Este README es solo un resumen técnico del proyecto.  
La versión **más visual y fácil de navegar** está disponible en nuestra página web de GitHub Pages.  

➡️ **[🌐 Ir a la página del proyecto ](https://rocio-perez-sbarato.github.io)**

## Ejecución del scraping

1. Descargar código
   
> Andá al repositorio en GitHub. 
>Hacé clic en el botón verde que dice Code.
>Elegí la opción "Download ZIP".
>Descomprimí el archivo ZIP en tu computadora.

2. Ejecutar las siguientes lineas en Windows Powershell o la terminal que sea
> ir a la carpeta CBTE con el comando cd. Ejemplo: cd ./Descargas/CBTE
> `python -m venv venv` -> `./venv/Scripts/activate` -> `pip install -r requirements.txt` -> `python scripts/supermercados/supermercados_vea/main.py`, por ejemplo. Si tu compu es buena, `python scripts/run_all.py`

## Configuración de credenciales

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