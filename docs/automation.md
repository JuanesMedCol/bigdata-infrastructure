# ⚙️ Automatización del Proyecto con GitHub Actions

Este proyecto utiliza un pipeline de integración y despliegue continuo dividido en **6 etapas automáticas**, ejecutadas cuando hay un `push` a la rama `main` o cada hora (`cron: '0 * * * *'`).

---

## 🔁 Flujo del Pipeline

### 1. Ingesta de Datos
- Clona el repositorio.
- Configura Python 3.9 e instala dependencias (`requests`, `pandas`, `openpyxl`).
- Ejecuta el script `src/ingestion.py`.
- Guarda resultados (`ingestion.db`, CSV, Excel y reporte de auditoría).

### 2. Limpieza de Datos
- Espera los resultados del paso anterior.
- Descarga los artefactos de ingesta.
- Ejecuta `src/cleaning.py` para limpiar datos.
- Guarda archivo limpio (`cleaning.xlsx`) y nuevo reporte.

### 3. Enriquecimiento Geográfico
- Usa los datos limpios como entrada.
- Consulta la API de OpenCage (requiere `OPENCAGE_API_KEY`).
- Ejecuta `src/enrichment.py` y agrega latitud/longitud.
- Guarda `enriched_data.xlsx` y su reporte de auditoría.

### 4. Generación de Informe
- Ejecuta `src/report.py` para consolidar los reportes y generar `report.md`.
- Muestra una vista previa de la tabla enriquecida (requiere `tabulate`).

### 5. Construcción de la Documentación
- Usa MkDocs con el tema Material.
- Copia todos los resultados generados (auditorías, Excel, CSV) a `docs/resultados/`.
- Compila la documentación (`mkdocs build`).

### 6. Despliegue en GitHub Pages
- Publica el sitio en la rama `gh-pages` mediante `peaceiris/actions-gh-pages@v3`.

---

## ✅ Requisitos Clave

- Archivo `requirements.txt` con:

```txt
pandas
openpyxl
requests
tqdm
tabulate
mkdocs
mkdocs-material
mkdocs-mermaid2-plugin
mkdocs-glightbox
```

## ✨ Variables de Ambiente

- Secreto `OPENCAGE_API_KEY` en el repositorio para la API de enriquecimiento.
- Secreto `GH_TOKEN` para despliegue en GitHub Pages.
