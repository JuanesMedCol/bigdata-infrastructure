# ⚙️ Automatización con GitHub Actions

Este proyecto integra un flujo de CI/CD automatizado mediante **GitHub Actions** para asegurar que cada push o actualización valide el proyecto y reconstruya la documentación automáticamente.

---

## 📄 Archivo YAML del Workflow

``` yaml linenums="1"
name: Ingestión, Limpieza, Enrequicimiento, Auditoria y Documentación

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 * * * *'

jobs:
  ingest_data:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install requests pandas openpyxl

      - name: Run ingestion script
        run: python src/ingestion.py

      - name: Upload ingestion results
        uses: actions/upload-artifact@v4
        with:
          name: ingestion-results
          path: |
            src/static/auditoria/ingestion_report.txt
            src/static/db/ingestion.db
            src/static/csv/ingestion.csv
            src/static/xlsx/ingestion.xlsx

  clean_data:
    needs: ingest_data
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install pandas openpyxl

      - name: Download ingestion results
        uses: actions/download-artifact@v4
        with:
          name: ingestion-results
          path: src/static/

      - name: Run cleaning script
        run: python src/cleaning.py

      - name: Upload cleaning results
        uses: actions/upload-artifact@v4
        with:
          name: cleaning-results
          path: |
            src/static/db/ingestion.db
            src/static/auditoria/cleaning_report.txt
            src/static/xlsx/cleaning.xlsx

  enrich_data:
      needs: clean_data
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v3
  
        - name: Set up Python
          uses: actions/setup-python@v4
          with:
            python-version: '3.9'
  
        - name: Install dependencies
          run: |
            pip install pandas openpyxl requests tqdm
  
        - name: Export secret to env
          run: echo "OPENCAGE_API_KEY=${{ secrets.OPENCAGE_API_KEY }}" >> $GITHUB_ENV
  
        - name: Run enrichment script
          run: python src/enrichment.py
 
        - name: Upload enrichment results
          uses: actions/upload-artifact@v4
          with:
            name: enrichment-results
            path: |
              src/static/db/ingestion.db
              src/static/auditoria/enriched_report.txt
              src/static/xlsx/enriched_data.xlsx       

  generate_report:
    needs: enrich_data
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Run report generation script
        run: python src/report.py

      - name: report audit markdown
        uses: actions/upload-artifact@v4
        with:
          name: report-md
          path: docs/report.md

  build_docs:
    needs: generate_report
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install MkDocs and theme
        run: |
          pip install --upgrade pip
          pip install mkdocs mkdocs-material mkdocs-mermaid2-plugin mkdocs-glightbox

      - name: Copiar archivos generados a docs/resultados
        run: |
          mkdir -p docs/resultados
          cp src/static/auditoria/*.txt docs/resultados/
          cp src/static/csv/*.csv docs/resultados/
          cp src/static/xlsx/*.xlsx docs/resultados/
          cp docs/report.md docs/resultados/

      - name: Mostrar plugins activos
        run: mkdocs build --verbose

      - name: Build MkDocs site
        run: mkdocs build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          personal_token: ${{ secrets.GH_TOKEN }}
          publish_dir: ./site

      - name: Verificar contenido de site/
        run: ls -R site/
```

---

## ✅ Beneficios

- Automatiza validaciones y construcción de la documentación.
- Ayuda a detectar errores en `mkdocs.yml` o enlaces rotos.
- Ideal para integración continua de entornos educativos o de datos.

---

## 📦 Archivos relacionados

- `.github/workflows/bigdata.yml`
- `requirements.txt`
- `mkdocs.yml`
