import pandas as pd
import os
import requests
import sqlite3
import logging
import time
from tqdm import tqdm

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Rutas
BASE_PATH = "src/static"
BASE_DATA = os.path.join(BASE_PATH, "xlsx", "cleaning.xlsx")
ENRICHED_OUTPUT = os.path.join(BASE_PATH, "xlsx", "enriched_data.xlsx")
AUDIT_OUTPUT = os.path.join(BASE_PATH, "auditoria", "enriched_report.txt")
DB_PATH = os.path.join(BASE_PATH, "db", "ingestion.db")

# Cargar dataset limpio
df_base = pd.read_excel(BASE_DATA)
original_count = len(df_base)
logging.info(f"📥 Dataset base cargado: {original_count} registros.")

# API de geolocalización
API_KEY = os.getenv("OPENCAGE_API_KEY", "")
if not API_KEY:
    raise ValueError("❌ No se encontró la variable de entorno 'OPENCAGE_API_KEY'")


def geolocalizar_ciudad(ciudad):
    if not ciudad:
        return None, None
    url = 'https://api.opencagedata.com/geocode/v1/json'
    params = {
        'q': ciudad,
        'key': API_KEY,
        'language': 'es',
        'limit': 1
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data['results']:
            coords = data['results'][0]['geometry']
            return coords['lat'], coords['lng']
        else:
            return None, None
    except Exception as e:
        logging.warning(f"❌ Error geolocalizando {ciudad}: {e}")
        return None, None

# Auditoría
audit_lines = []
audit_lines.append("📋 **Informe de Enriquecimiento de Datos**\n")
audit_lines.append(f"🔢 Registros base: {original_count}")

# Enriquecer si hay columna 'capital'
latitudes = []
longitudes = []

if 'capital' in df_base.columns:
    for idx, row in tqdm(df_base.iterrows(), total=len(df_base), desc="Enriqueciendo capitales"):
        ciudad = row['capital']
        lat, lng = geolocalizar_ciudad(ciudad)
        latitudes.append(lat)
        longitudes.append(lng)
        time.sleep(1)  # <-- delay de 1 segundo entre llamadas

    df_base['latitud'] = latitudes
    df_base['longitud'] = longitudes
    audit_lines.append("🌍 Enriquecimiento con coordenadas geográficas aplicado.")
else:
    logging.warning("⚠️ No se encontró la columna 'capital' para enriquecer con coordenadas.")
    audit_lines.append("⚠️ Enriquecimiento geográfico no aplicado (columna 'capital' no encontrada).")

# Exportar a Excel
df_base.to_excel(ENRICHED_OUTPUT, index=False)
logging.info(f"✅ Dataset enriquecido exportado a: {ENRICHED_OUTPUT}")

# Exportar a SQLite
conn = sqlite3.connect(DB_PATH)
df_base.to_sql("countries_enriched", conn, if_exists="replace", index=False)
conn.close()
logging.info("🗃️ Datos enriquecidos exportados a la tabla 'countries_enriched' en SQLite.")

# Guardar informe
audit_lines.append(f"🔢 Registros finales: {len(df_base)}")
with open(AUDIT_OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(audit_lines))
logging.info(f"📝 Informe de auditoría generado en: {AUDIT_OUTPUT}")