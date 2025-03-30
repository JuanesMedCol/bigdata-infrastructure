import requests
import os
import sqlite3
import pandas as pd
import logging

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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

# === Datos de todos los países desde restcountries ===
rest_url = 'https://restcountries.com/v3.1/all'
response = requests.get(rest_url)

if response.status_code == 200:
    data = response.json()
    countries = []

    for country in data:
        countries.append({
            'pais': country['name']['common'],
            'capital': country['capital'][0] if country.get('capital') else None,
            'region': country.get('region'),
            'subregion': country.get('subregion'),
            'poblacion': country.get('population'),
            'area': country.get('area')
        })

    df = pd.DataFrame(countries)

    # Guardar en base de datos
    conn = sqlite3.connect(os.path.join(folder_path_db, db_file))
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            pais TEXT,
            capital TEXT,
            region TEXT,
            subregion TEXT,
            poblacion INTEGER,
            area REAL
        )
    """)
    cursor.execute("DELETE FROM countries")  # Limpiar antes de insertar
    df.to_sql('countries', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

    # Guardar CSV y Excel
    df.to_csv(os.path.join(folder_path_csv, csv_file), index=False)
    df.to_excel(os.path.join(folder_path_xlsx, xlsx_file), index=False)

    # Informe de auditoría
    with open(os.path.join(folder_path_auditoria, auditoria_file), 'w', encoding="utf-8") as f:
        f.write("📋 Informe de Ingesta Global de Países\n\n")
        f.write(f"🌍 Total países: {len(df)}\n")
        f.write(f"📝 Columnas: {', '.join(df.columns)}\n")

    logging.info("✅ Datos globales importados y almacenados correctamente.")

else:
    logging.error("❌ No se pudo obtener la información de los países desde restcountries.")