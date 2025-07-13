@echo off
REM ======================================
REM Script para crear/activar el entorno virtual y ejecutar el scraper
REM ======================================

REM Verificar si la carpeta "venv" existe
if not exist "venv\Scripts\activate.bat" (
    echo ======================================
    echo Creando entorno virtual...
    echo ======================================
    python -m venv venv
)

echo ======================================
echo Activando entorno virtual...
echo ======================================
call venv\Scripts\activate.bat

echo ======================================
echo Instalando dependencias...
echo ======================================
pip install -r requirements.txt

echo ======================================
echo Ejecutando el pipeline (scripts\run_all.py)...
echo ======================================
python scripts\run_all.py

echo ======================================
echo Proceso finalizado.
echo Presioná una tecla para cerrar.
pause
