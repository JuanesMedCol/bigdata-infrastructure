## 🌍 Enriquecimiento de Datos Geográficos

Este script toma un archivo de datos previamente limpiado y lo **enriquece geográficamente** utilizando la API de OpenCage para obtener coordenadas (latitud y longitud) de la capital de cada país.

---

### 📁 Estructura de Archivos

* **Archivo de entrada (limpio)** : `src/static/xlsx/cleaning.xlsx`
* **Archivo enriquecido de salida** : `src/static/xlsx/enriched_data.xlsx`
* **Base de datos de salida** : `src/static/db/ingestion.db`
* **Reporte de auditoría** : `src/static/auditoria/enriched_report.txt`

---

### 🧠 ¿Qué hace el script?

✅ Lee los datos del archivo `cleaning.xlsx`.

✅ Consulta la API de OpenCage por cada capital del dataset (respetando un límite de 1 solicitud por segundo).

✅ Agrega dos nuevas columnas:
* `latitud`
* `longitud`

✅ Exporta el resultado enriquecido a:
* Excel (`enriched_data.xlsx`)
* Base de datos SQLite (`countries_enriched`)
* Informe de auditoría (`enriched_report.txt`)

---

### ⚙️ Uso de la API de OpenCage

Este script realiza una llamada `GET` por cada capital del mundo a:

```
https://api.opencagedata.com/geocode/v1/json
```

La solicitud se realiza con un retraso (`delay`) de **1 segundo** para cumplir con la cuota gratuita de la API.

---

### 📊 Reporte generado

**Ejemplo de contenido del `enriched_report.txt`:**

```
📋 Informe de Enriquecimiento de Datos

🔢 Registros base: 250
🌍 Enriquecimiento con coordenadas geográficas aplicado.
🔢 Registros finales: 250
```

---

### ✅ Resultado Final

El script genera logs informativos a medida que procesa los datos:

```
🌍 Enriqueciendo capitales: 30% completado...
✅ Dataset enriquecido exportado a: enriched_data.xlsx
🗃️ Datos exportados a la tabla 'countries_enriched'
```

---

### 📎 Archivos Generados

* [Excel Enriquecido](resultados/enriched_data.xlsx)
* [Base de Datos SQLite](resultados/ingestion.db)
* [Reporte de Auditoría](resultados/enriched_report.txt)

---

### 🧠 Diagrama del Proceso de Enriquecimiento

``` mermaid
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
