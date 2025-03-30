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

# Crear carpeta docs si no existe
Path("docs").mkdir(parents=True, exist_ok=True)

# Guardar como archivo markdown
auditoria_md_path = Path("docs/report.md")
auditoria_md_path.write_text(auditoria_md.strip(), encoding="utf-8")

print(f"✅ Informe generado en: {auditoria_md_path}")
