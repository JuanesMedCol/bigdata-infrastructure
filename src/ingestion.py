import requests
import os
import sqlite3
import pandas as pd
import logging
from datetime import datetime

# Configurar logging para mostrar fecha, hora y nivel de registro
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# URL del API
url = 'https://jsonplaceholder.typicode.com/posts'

# Iniciar proceso
logging.info("Inicio del proceso")

# Realiza la solicitud GET al API
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    logging.info(f"Datos obtenidos correctamente ({len(data)} registros).")
else:
    logging.error(f'Error {response.status_code}: No se pudieron obtener los datos')
    exit()

# Rutas de los archivos
folder_path_db = './src/static/db'
db_file = 'ingestion.db'

folder_path_csv = './src/static/csv'
csv_file = 'ingestion.csv'

folder_path_xlsx = './src/static/xlsx'
xlsx_file = 'ingestion.xlsx'

folder_path_auditoria = './src/static/auditoria'
auditoria_file = 'ingestion_report.txt'

# Crear carpetas si no existen
for folder in [folder_path_db, folder_path_csv, folder_path_xlsx, folder_path_auditoria]:
    os.makedirs(folder, exist_ok=True)

logging.info("Directorios creados/verificados correctamente.")

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect(os.path.join(folder_path_db, db_file))
cursor = conn.cursor()

# Crear una tabla para almacenar los datos (ajustar a tu API)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        title TEXT,
        body TEXT
    )
''')

# Insertar datos extraídos del API en la base de datos
for item in data:
    cursor.execute('''INSERT OR REPLACE INTO posts (id, title, body) VALUES (?, ?, ?)''',
                   (item['id'], item['title'], item['body']))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

logging.info(f"Datos insertados correctamente en la base de datos ({len(data)} registros).")

# Conectar a la base de datos para exportar
conn = sqlite3.connect(os.path.join(folder_path_db, db_file))
df = pd.read_sql_query("SELECT * FROM posts LIMIT 10", conn)

# Exportar a CSV y Excel
df.to_csv(os.path.join(folder_path_csv, csv_file), index=False)
logging.info(f"CSV exportado a: {os.path.join(folder_path_csv, csv_file)}")

df.to_excel(os.path.join(folder_path_xlsx, xlsx_file), index=False)
logging.info(f"Excel exportado a: {os.path.join(folder_path_xlsx, xlsx_file)}")

conn.close()

# Generar archivo de auditoría
with open(os.path.join(folder_path_auditoria, auditoria_file), 'w', encoding="utf-8") as f:
    f.write("Comparación de los datos extraídos y almacenados en la base de datos:\n")

    coincidencias = 0
    no_encontrados = 0
    
    for item in data:
        conn = sqlite3.connect(os.path.join(folder_path_db, db_file))
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (item['id'],))
        db_record = cursor.fetchone()
        conn.close()

        if db_record:
            if item['title'] == db_record[1] and item['body'] == db_record[2]:
                coincidencias += 1
            else:
                f.write(f"❌ ID {item['id']}: Datos NO coinciden\n")
        else:
            no_encontrados += 1
            f.write(f"❌ ID {item['id']}: No se encuentra en la base de datos\n")

    # Resumen final
    f.write("\nResumen:\n")
    f.write(f"✔️ Registros coincidentes: {coincidencias}\n")
    f.write(f"❌ Registros no encontrados: {no_encontrados}\n")

logging.info(f"Informe de auditoría generado en: {os.path.join(folder_path_auditoria, auditoria_file)}")

# Fin del proceso
logging.info("Proceso finalizado correctamente ✅")
