import os
import pandas as pd
import sqlite3
import logging

# Configurar logging para incluir fecha y hora
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 1. Configuración de rutas
DB_PATH = "./src/static/db/ingestion.db"
OUTPUT_CSV = "./src/static/xlsx/cleaning.xlsx"
AUDIT_FILE = "./src/static/auditoria/cleaning_report.txt"

def load_data():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"La base de datos '{DB_PATH}' no existe.")
    
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM posts"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# 2. Análisis Exploratorio
def explore_data(df):
    report = []
    report.append(f"Número total de registros: {len(df)}")
    report.append(f"Número de valores nulos por columna:\n{df.isnull().sum()}")
    report.append(f"Número de registros duplicados: {df.duplicated().sum()}")
    return report

# 3. Limpieza y Transformación
def clean_data(df):
    # Eliminar duplicados
    df = df.drop_duplicates()

    # Manejo de valores nulos basado en tipo de datos
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(df[col].mean())  # ✅ Sin `inplace=True`
        else:
            df[col] = df[col].ffill()  # ✅ Uso directo de `ffill()` en lugar de `fillna(method='ffill')`

    # Corrección de tipos de datos
    if 'fecha' in df.columns:
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    if 'monto' in df.columns:
        df['monto'] = pd.to_numeric(df['monto'], errors='coerce')

        # Normalización
        df['monto'] = (df['monto'] - df['monto'].mean()) / df['monto'].std()

    return df

# 4. Guardar resultados
def save_results(df, report):
    df.to_excel(OUTPUT_CSV, index=False)
    logging.info(f"📄 Archivo Excel exportado a: {OUTPUT_CSV}")

    # ✅ Forzar codificación UTF-8 para el archivo de auditoría
    with open(AUDIT_FILE, "w", encoding="utf-8") as f:
        f.write("📋 **Informe de Limpieza de Datos**\n\n")

        for line in report:
            f.write(line + "\n")
        
        f.write(f"\n✅ Número de registros después de limpieza: {len(df)}\n")

    logging.info(f"📝 Informe de auditoría generado en: {AUDIT_FILE}")

def main():
    logging.info("🚀 Inicio del proceso de limpieza de datos")

    try:
        df = load_data()
        logging.info(f"📥 Datos cargados correctamente con {len(df)} registros.")

        report = explore_data(df)
        df_cleaned = clean_data(df)

        # Verificación post-limpieza
        if df_cleaned.isnull().sum().sum() > 0:
            logging.warning("⚠️ Existen valores nulos después de la limpieza.")
        else:
            logging.info("✅ No hay valores nulos después de la limpieza.")

        save_results(df_cleaned, report)
        logging.info("✅ Proceso completado con éxito.")
    
    except Exception as e:
        logging.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
