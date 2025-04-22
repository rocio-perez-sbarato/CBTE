import time
import psutil
from contextlib import contextmanager

@contextmanager
def medir_recursos():
    start_time = time.time()
    cpu_start = psutil.cpu_percent()
    mem_start = psutil.virtual_memory().used / (1024 ** 2)

    yield

    end_time = time.time()
    cpu_end = psutil.cpu_percent()
    mem_end = psutil.virtual_memory().used / (1024 ** 2)

    print(f"Tiempo de ejecución: {(end_time - start_time) / 60:.2f} minutos")
    print(f"Uso de CPU: {cpu_end - cpu_start:.2f}%")
    print(f"Memoria utilizada: {mem_end - mem_start:.2f} MB")
