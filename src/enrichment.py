import pandas as pd
import os
import logging

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Rutas
BASE_PATH = "src/static"
BASE_DATA = os.path.join(BASE_PATH, "xlsx", "cleaning.xlsx")
ENRICH_PATH = os.path.join(BASE_PATH, "enrichment_sources")
ENRICHED_OUTPUT = os.path.join(BASE_PATH, "xlsx", "enriched_data.xlsx")
AUDIT_OUTPUT = os.path.join(BASE_PATH, "auditoria", "enriched_report.txt")

# Cargar el dataset base
df_base = pd.read_excel(BASE_DATA)
original_count = len(df_base)
logging.info(f"📥 Dataset base cargado: {original_count} registros.")

# Cargar fuentes adicionales
sources = {}

try:
    sources['json'] = pd.read_json(os.path.join(ENRICH_PATH, "data.json"))
    sources['csv'] = pd.read_csv(os.path.join(ENRICH_PATH, "data.csv"))
    sources['xlsx'] = pd.read_excel(os.path.join(ENRICH_PATH, "data.xlsx"))
    sources['xml'] = pd.read_xml(os.path.join(ENRICH_PATH, "data.xml"))
    sources['html'] = pd.read_html(os.path.join(ENRICH_PATH, "data.html"))[0]
    sources['txt'] = pd.read_csv(os.path.join(ENRICH_PATH, "data.txt"), sep="\t", encoding="utf-8")
except Exception as e:
    logging.error(f"❌ Error al leer fuentes: {e}")

# Integrar datos adicionales
df_enriched = df_base.copy()
audit_lines = []
audit_lines.append("📋 **Informe de Enriquecimiento de Datos**\n")
audit_lines.append(f"🔢 Registros base: {original_count}")

for name, df_extra in sources.items():
    if 'id' not in df_extra.columns:
        logging.warning(f"⚠️ La fuente {name} no contiene columna 'id'. Saltando.")
        audit_lines.append(f"⚠️ Fuente {name}: no contiene columna 'id', no se integró.")
        continue

    initial_cols = df_enriched.columns.tolist()
    df_enriched = df_enriched.merge(df_extra, on="id", how="left", suffixes=('', f'_{name}'))
    new_cols = [col for col in df_enriched.columns if col not in initial_cols]

    coincidencias = df_extra['id'].isin(df_base['id']).sum()
    audit_lines.append(f"✅ Fuente {name}: {coincidencias} coincidencias. Campos añadidos: {', '.join(new_cols)}")

# Exportar resultados
df_enriched.to_excel(ENRICHED_OUTPUT, index=False)
logging.info(f"✅ Dataset enriquecido exportado a: {ENRICHED_OUTPUT}")

# Generar archivo de auditoría
audit_lines.append(f"\n🔢 Registros finales: {len(df_enriched)}")
with open(AUDIT_OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(audit_lines))
logging.info(f"📝 Informe de auditoría generado en: {AUDIT_OUTPUT}")
