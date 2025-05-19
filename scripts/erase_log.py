import os

file_path = 'scripts/all_messages_conf.log'

try:
    os.remove(file_path)  
    print(f'Se eliminó: {file_path}')
except FileNotFoundError:
    print('El archivo no existe.')
except Exception as e:
    print(f'No se pudo eliminar {file_path}. Motivo: {e}')
