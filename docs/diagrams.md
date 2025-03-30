# 📊 Diagramas del Proyecto

1. **Ingesta**:
   - Se conecta a la API pública de RESTCountries.
   - Se guarda en SQLite (`countries`) y se exporta en formatos CSV y Excel.
   - Se genera un informe (`ingestion_report.txt`).

2. **Limpieza**:
   - Se eliminan duplicados.
   - Se imputan nulos y se corrigen tipos de datos.
   - Se almacena el resultado limpio en `countries_clean` y Excel.

3. **Enriquecimiento**:
   - Usa la API de OpenCage para obtener coordenadas por capital.
   - Añade columnas de latitud y longitud.
   - Se guarda como `countries_enriched` en SQLite y Excel.

4. **Flujo Secuencial**:
   - Cada fase depende de la anterior.
   - Los reportes permiten trazabilidad del estado de los datos.
---

=== "General"

    ```mermaid
    graph TD
        A1[API RESTCountries] --> A2[Extraer datos]
        A2 --> A3[Guardar en SQLite]
        A3 --> A4[Exportar a Excel y CSV]
        A4 --> A5[Generar reporte]

        A5 --> B1[Leer countries]
        B1 --> B2[Eliminar duplicados]
        B2 --> B3[Imputar nulos]
        B3 --> B4[Convertir tipos]
        B4 --> B5[Guardar en cleaning y Excel]
        B5 --> B6[Generar reporte limpieza]

        B6 --> C1[Leer cleaning.xlsx]
        C1 --> C2[Leer capitales]
        C2 --> C3{Capital valida?}
        C3 -- Si --> C4[API OpenCage]
        C4 --> C5[Añadir coords]
        C5 --> C6[Guardar enriched]
        C6 --> C7[Reporte enriquecimiento]
        C3 -- No --> CZ[Omitir registro]
    ```

=== "Ingesta"

    ```mermaid
    flowchart TD
        A[Solicitar datos de API RESTCountries] --> B[Extraer atributos clave]
        B --> C[Guardar en archivo CSV y Excel]
        C --> D[Guardar en tabla countries de SQLite]
        D --> E[Generar archivo de auditoría]
    ```

=== "Limpieza"

    ```mermaid
    flowchart TD
        A[Leer datos de countries en SQLite] --> B[Eliminar duplicados]
        B --> C[Imputar valores nulos]
        C --> D[Convertir tipos: poblacion y area]
        D --> E[Guardar como cleaning.xlsx]
        D --> F[Guardar en tabla countries_clean]
        F --> G[Generar cleaning_report.txt]
    ```

=== "Enriquecimiento"

    ```mermaid
    flowchart TD
        A[Inicio del Proceso] --> B[Cargar archivo cleaning.xlsx]
        B --> C[Leer columna capital]
        C --> D{¿Capital existe?}
        D -- Sí --> E[Consultar API OpenCage por cada capital]
        E --> F[Añadir latitud y longitud]
        F --> G[Agregar columnas al DataFrame]
        G --> H[Exportar a enriched_data.xlsx]
        G --> I[Guardar en tabla countries_enriched de SQLite]
        G --> J[Generar enriched_report.txt]
        J --> K[Fin del proceso]
        D -- No --> Z[Abortar enriquecimiento]
    ```

=== "Entidad-Relación"

    ```mermaid
    erDiagram
        countries {
            TEXT pais
            TEXT capital
            TEXT region
            TEXT subregion
            INTEGER poblacion
            REAL area
        }

        countries_clean {
            TEXT pais
            TEXT capital
            TEXT region
            TEXT subregion
            INTEGER poblacion
            REAL area
        }

        countries_enriched {
            TEXT pais
            TEXT capital
            TEXT region
            TEXT subregion
            INTEGER poblacion
            REAL area
            REAL latitud
            REAL longitud
        }

        countries ||--|| countries_clean : limpieza
        countries_clean ||--|| countries_enriched : enriquecimiento
    ```

=== "Automatizacion"

     ```mermaid
     graph TD
         A[push o cron] --> B[ingest_data]
         B --> C[clean_data]
         C --> D[enrich_data]
         D --> E[generate_report]
         E --> F[build_docs]
    
         subgraph Job: ingest_data
             B1[Checkout code]
             B2[Setup Python 3.9]
             B3[Install dependencies]
             B4[Run ingestion.py]
             B5[Upload artifacts]
             B1 --> B2 --> B3 --> B4 --> B5
         end
    
         subgraph Job: clean_data
             C1[Checkout code]
             C2[Setup Python 3.9]
             C3[Install pandas, openpyxl]
             C4[Download ingestion-results]
             C5[Run cleaning.py]
             C6[Upload cleaning-results]
             C1 --> C2 --> C3 --> C4 --> C5 --> C6
         end
    
         subgraph Job: enrich_data
             D1[Checkout code]
             D2[Setup Python 3.9]
             D3[Install requests, pandas, tqdm]
             D4[Export API key]
             D5[Run enrichment.py]
             D6[Upload enrichment-results]
             D1 --> D2 --> D3 --> D4 --> D5 --> D6
         end
    
         subgraph Job: generate_report
             E1[Checkout code]
             E2[Setup Python 3.9]
             E3[Run report.py]
             E4[Upload report.md]
             E1 --> E2 --> E3 --> E4
         end
    
         subgraph Job: build_docs
             F1[Checkout code]
             F2[Setup Python 3.11]
             F3[Install MkDocs plugins]
             F4[Copiar archivos a docs/resultados]
             F5[Ver plugins activos]
             F6[mkdocs build]
             F7[Deploy con GH Pages]
             F8[Verificar contenido]
             F1 --> F2 --> F3 --> F4 --> F5 --> F6 --> F7 --> F8
         end
     ```

=== "Resumen"

    ```mermaid
    flowchart TD
        A[Ingesta API RESTCountries] --> B[Guardar en SQLite y Excel]
        B --> C[Limpieza de Datos]
        C --> D[Guardar limpio en cleaning.xlsx y countries_clean]
        D --> E[Enriquecimiento con OpenCage]
        E --> F[Guardar enriquecido en enriched_data.xlsx y countries_enriched]
    ```
