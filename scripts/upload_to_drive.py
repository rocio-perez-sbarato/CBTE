import os
from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Inicializar servicio
def init_drive_service():
    creds = Credentials.from_service_account_file(
        'scripts/credentials.json',
        scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=creds)

# Crear carpeta en Drive
def crear_carpeta(service, nombre, parent_id=None):
    metadata = {
        'name': nombre,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        metadata['parents'] = [parent_id]
    carpeta = service.files().create(body=metadata, fields='id').execute()
    return carpeta.get('id')

# Subir archivo a Drive
def subir_archivo(service, ruta_local, nombre_archivo, parent_id):
    media = MediaFileUpload(ruta_local, resumable=True)
    metadata = {
        'name': nombre_archivo,
        'parents': [parent_id]
    }
    file = service.files().create(body=metadata, media_body=media, fields='id').execute()
    print(f"Subido: {nombre_archivo} (ID: {file.get('id')})")

# Subir estructura completa recursiva
def subir_carpeta_recursiva(service, ruta_local, parent_id_drive, fecha):
    nombre_carpeta = os.path.basename(ruta_local)
    id_drive_actual = crear_carpeta(service, nombre_carpeta, parent_id=parent_id_drive)

    for item in os.listdir(ruta_local):
        ruta_item = os.path.join(ruta_local, item)
        if os.path.isdir(ruta_item):
            subir_carpeta_recursiva(service, ruta_item, id_drive_actual, fecha)
        elif item.endswith('.xlsx'):
            nombre_con_fecha = f"{os.path.splitext(item)[0]}_{fecha}.xlsx"
            subir_archivo(service, ruta_item, nombre_con_fecha, id_drive_actual)

# Función principal
def subir_data_con_estructura(carpeta_local='data'):
    service = init_drive_service()
    fecha = datetime.today().strftime('%d-%m-%Y')

    # ID de la carpeta padre en Google Drive
    id_carpeta_padre = '12ATKgCJ0tckWVMpO2F30w2-YrXNx2110' 

    # Carpeta raíz del backup
    id_backup = crear_carpeta(service, f'scraping_{fecha}', parent_id=id_carpeta_padre)

    # Guardamos el ID de cada carpeta creada
    carpetas_drive = {carpeta_local: id_backup}

    for carpeta_raiz, carpetas_hijas, archivos in os.walk(carpeta_local):
        # Calculamos ruta relativa desde la carpeta_local
        ruta_relativa = os.path.relpath(carpeta_raiz, carpeta_local)

        # Buscamos el ID de la carpeta padre en Drive
        parent_rel = os.path.dirname(ruta_relativa)
        parent_id = carpetas_drive.get(parent_rel, id_backup)

        # Si no es la carpeta raíz, creamos carpeta en Drive
        if ruta_relativa != '.':
            nombre_carpeta = os.path.basename(carpeta_raiz)
            id_carpeta_actual = crear_carpeta(service, nombre_carpeta, parent_id=parent_id)
            carpetas_drive[ruta_relativa] = id_carpeta_actual
        else:
            id_carpeta_actual = id_backup

        for archivo in archivos:
            if archivo.endswith('.xlsx'):
                ruta_archivo = os.path.join(carpeta_raiz, archivo)
                nombre_con_fecha = f"{os.path.splitext(archivo)[0]}.xlsx"
                subir_archivo(service, ruta_archivo, nombre_con_fecha, id_carpeta_actual)

    # Subir archivo de log
    ruta_log = os.path.join('scripts', 'all_messages_conf.log')
    if os.path.exists(ruta_log):
        subir_archivo(service, ruta_log, f"registro_scraping_{fecha}.log", id_backup)  

# Ejecutar
if __name__ == "__main__":
    subir_data_con_estructura("data")
