import pandas as pd
from pathlib import Path

# Leer las últimas auditorías de cada proceso desde sus archivos .txt
auditoria_paths = {
    "Ingesta": "src/static/auditoria/ingestion_report.txt",
    "Limpieza": "src/static/auditoria/cleaning_report.txt",
    "Enriquecimiento": "src/static/auditoria/enriched_report.txt"
}

auditorias = {}

for proceso, path in auditoria_paths.items():
    try:
        with open(path, encoding="utf-8") as f:
            contenido = f.read().strip()
            auditorias[proceso] = contenido
    except FileNotFoundError:
        auditorias[proceso] = "⚠️ No se encontró el archivo de auditoría."

# Crear contenido markdown
auditoria_md = "# 📋 Informe Consolidado de Auditoría\n\n"

for proceso, contenido in auditorias.items():
    auditoria_md += f"## 🔹 {proceso}\n\n"
    auditoria_md += f"```\n{contenido}\n```\n\n"

# Agregar vista previa de la tabla enriquecida
excel_path = Path("src/static/xlsx/enriched_data.xlsx")

if excel_path.exists():
    df = pd.read_excel(excel_path)
    preview_table = df.head(250).to_markdown(index=False, tablefmt="github")
else:
    preview_table = "⚠️ No se encontró el archivo enriched_data.xlsx."

preview_section = "## 🔍 Vista Previa de la Tabla Enriquecida\n\n"
preview_section += "A continuación se muestra una vista previa de los primeros registros del dataset enriquecido:\n\n"
preview_section += f"\n{preview_table}\n\n"

# Combinar todo
full_report = auditoria_md.strip() + "\n\n" + preview_section.strip()

# Crear carpeta docs si no existe
report_path = Path("docs/report.md")
report_path.parent.mkdir(parents=True, exist_ok=True)

# Guardar como archivo markdown
report_path.write_text(full_report, encoding="utf-8")

# Copiar para descarga
output_path = Path("docs/report.md")
output_path.write_text(full_report, encoding="utf-8")

output_path
