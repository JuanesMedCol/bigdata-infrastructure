import subprocess
import os

# Definir las rutas a los scripts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')

# Scripts a ejecutar en orden
scripts = ['ingestion.py', 'cleaning.py']

for script in scripts:
    script_path = os.path.join(SRC_DIR, script)
    print(f"Ejecutando {script_path}...")
    try:
        subprocess.run(['python', script_path], check=True)
        print(f"{script} ejecutado correctamente ✅")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {script}: {e}")
        break
