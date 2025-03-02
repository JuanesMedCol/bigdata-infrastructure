import requests
import os
import sqlite3
import pandas as pd

# URL del API
url = 'https://jsonplaceholder.typicode.com/posts'

# Realiza la solicitud GET al API
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()  # Convierte la respuesta JSON en un diccionario de Python
    print(data)  # Imprime los datos obtenidos
else:
    print(f'Error {response.status_code}: No se pudieron obtener los datos')

# Rutas de los archivos
folder_path_db = './static/db'
db_file = 'ingestion.db'

folder_path_csv = './static/csv'
csv_file = 'ingestion.csv'

folder_path_xlsx = './static/xlsx'
xlsx_file = 'ingestion.xlsx'

folder_path_auditoria = './static/auditoria'
auditoria_file = 'auditoria.txt'

# Verifica si la carpeta existe, si no, la crea
if not os.path.exists(folder_path_db):
    os.makedirs(folder_path_db)

if not os.path.exists(folder_path_csv): 
    os.makedirs(folder_path_csv)

if not os.path.exists(folder_path_xlsx):  
    os.makedirs(folder_path_xlsx)
    
if not os.path.exists(folder_path_auditoria):  
    os.makedirs(folder_path_auditoria)

# Verifica si la carpeta existe, si no, la crea
if not os.path.exists(folder_path_db):
    os.makedirs(folder_path_db)

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

# Conectar a la base de datos
conn = sqlite3.connect(os.path.join(folder_path_db, db_file))

# Cargar datos desde la base de datos
df = pd.read_sql_query("SELECT * FROM posts LIMIT 10", conn)

# Exportar a CSV
df.to_csv(os.path.join(folder_path_csv, csv_file), index=False)

# También puedes exportar a Excel
df.to_excel(os.path.join(folder_path_xlsx, xlsx_file), index=False)

conn.close()

# Generar archivo de auditoría
with open(os.path.join(folder_path_auditoria, auditoria_file), 'w') as f:
    # Comparar y escribir resultados
    f.write("Comparación de los datos extraídos y almacenados en la base de datos:\n")

    for item in data:
        # Recuperar registros de la base de datos
        conn = sqlite3.connect(os.path.join(folder_path_db, db_file))
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (item['id'],))
        db_record = cursor.fetchone()
        conn.close()

        # Comparar y escribir en el archivo de auditoría
        if db_record:
            f.write(f"ID {item['id']} - Coinciden los datos: {item['title'] == db_record[1] and item['body'] == db_record[2]}\n")
        else:
            f.write(f"ID {item['id']} - No se encuentra en la base de datos\n")