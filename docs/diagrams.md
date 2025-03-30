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
    graph TD
        A[Solicitar API RESTCountries] --> B[Extraer campos]
        B --> C[Guardar CSV y Excel]
        C --> D[Insertar en SQLite]
        D --> E[Generar reporte ingesta]
    ```

=== "Limpieza"

    ```mermaid
    graph TD
        A[Leer tabla countries] --> B[Eliminar duplicados]
        B --> C[Imputar nulos]
        C --> D[Convertir poblacion y area]
        D --> E[Guardar cleaning.xlsx y tabla]
        E --> F[Generar reporte limpieza]
    ```

=== "Enriquecimiento"

    ```mermaid
    graph TD
        A[Cargar cleaning.xlsx] --> B[Leer columna capital]
        B --> C{Capital válida?}
        C -- Sí --> D[Consultar API OpenCage]
        D --> E[Añadir latitud y longitud]
        E --> F[Guardar en enriched_data.xlsx y countries_enriched]
        F --> G[Generar enriched_report.txt]
        C -- No --> H[Omitir enriquecimiento]
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

=== "Resumen"

    ```mermaid
    graph TD
        A[Ingesta API RESTCountries] --> B[Guardar en SQLite y Excel]
        B --> C[Limpieza de Datos]
        C --> D[Guardar en cleaning.xlsx y countries_clean]
        D --> E[Enriquecimiento geográfico]
        E --> F[Guardar en enriched_data.xlsx y countries_enriched]
    ```
