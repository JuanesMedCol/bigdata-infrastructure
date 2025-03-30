import logging
import subprocess
import os
import threading
import time
from tqdm import tqdm

# Definir rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def barra_progreso(flag):
    with tqdm(desc="⏳ Enriqueciendo datos", total=100, bar_format='{l_bar}{bar}| {elapsed} {postfix}') as pbar:
        while not flag["done"]:
            pbar.update(1)
            time.sleep(0.1)
            if pbar.n >= 100:
                pbar.n = 0
                pbar.last_print_n = 0
                pbar.refresh()

def ejecutar_script(nombre_script, mostrar_barra=False):
    ruta_script = os.path.join(SRC_DIR, nombre_script)
    logging.info(f"🚀 Ejecutando: {ruta_script}")

    if mostrar_barra:
        estado = {"done": False}
        hilo_barra = threading.Thread(target=barra_progreso, args=(estado,))
        hilo_barra.start()

        result = subprocess.run(["python", ruta_script], capture_output=True, text=True)
        estado["done"] = True
        hilo_barra.join()
    else:
        result = subprocess.run(["python", ruta_script], capture_output=True, text=True)

    if result.returncode == 0:
        logging.info(f"✅ {nombre_script} completado con éxito.")
    else:
        logging.error(f"❌ Error en {nombre_script}:\n{result.stderr}")

def main():
    scripts = [
        ("ingestion.py", False),
        ("cleaning.py", False),
        ("enrichment.py", True)  # Solo aquí se activa la barra
    ]

    for script, usar_barra in scripts:
        ejecutar_script(script, mostrar_barra=usar_barra)

    logging.info("🎉 Proceso de integración completo.")

if __name__ == "__main__":
    main()
