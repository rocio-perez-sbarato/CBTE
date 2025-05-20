import subprocess
import os

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
    "upload_to_drive.py", # Comentar línea si no lo querés subir a drive
    #"erase_data.py", # Comentar esta línea si no lo vas a subir a drive 
    #"erase_log.py" # Comentar esta línea si no lo vas a subir a drive
]

def run_all():
    for script in scripts:
        path = os.path.join(os.path.dirname(__file__), script)
        print(f"\nEjecutando {script}...")
        subprocess.run(["python", path])

if __name__ == "__main__":
    run_all()
