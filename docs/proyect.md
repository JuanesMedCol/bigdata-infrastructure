## 📘 Documento de Arquitectura del Proyecto Integrador de Big Data

### 1. Introducción y Descripción Global de la Arquitectura

El proyecto integra tres fases principales en un entorno simulado de Big Data en la nube: **ingesta**, **limpieza** y **enriquecimiento** de datos. Utiliza `SQLite` como base de datos local simulando un almacén analítico, y `Python` como lenguaje principal para el procesamiento de datos. El flujo de trabajo se automatiza mediante `GitHub Actions` y se documenta con `MkDocs`.

---

### 2. Diagramas de Flujo y Arquitectura

**Diagrama 1: Flujo General del Proyecto**

- Desde la API pública `restcountries.com`, se extrae la información de países.
- Los datos son almacenados en SQLite (`countries`).
- Luego se realiza la limpieza y se guarda en `countries_clean`.
- Finalmente, se enriquecen con coordenadas geográficas usando la API de OpenCage y se guarda en `countries_enriched`.

**Diagrama 2: Proceso de Enriquecimiento**

- Entrada: `cleaning.xlsx` → Proceso de geolocalización por capital → Salida: `enriched_data.xlsx` y `countries_enriched`.

✅ *Puedo ayudarte a generar estos diagramas con base en esta estructura si lo deseas.*

---

### 3. Explicación Detallada de Componentes

#### 🔹 Ingesta

-**Fuente**: API `https://restcountries.com/v3.1/all`

-**Herramientas**: `requests`, `pandas`, `sqlite3`

-**Salida**: `ingestion.db`, `ingestion.csv`, `ingestion.xlsx`, `ingestion_report.txt`

#### 🔹 Limpieza

- Elimina duplicados y rellena nulos según el tipo de dato.
- Guarda resultados en `cleaning.xlsx` y tabla `countries_clean`.

#### 🔹 Enriquecimiento

- Uso de API `OpenCageData` para agregar latitud y longitud por capital.
- Resultado: tabla `countries_enriched` y Excel `enriched_data.xlsx`.

---

### 4. Modelo de Datos

**Tablas:**

-`countries`: datos en crudo.

-`countries_clean`: después de limpieza.

-`countries_enriched`: con latitud y longitud.

**Relaciones:**

- Todas las tablas comparten el campo clave `pais`.

✅ *Te puedo generar un diagrama ER (Entidad-Relación) que muestre esta evolución de los datos.*

---

### 5. Justificación de Herramientas

-**SQLite**: ligero, ideal para simulación local y consultas analíticas.

-**Pandas**: procesamiento flexible y potente de datos.

-**Requests**: extracción directa desde APIs REST.

-**GitHub Actions**: permite automatización continua del flujo ETL.

-**MkDocs**: ideal para documentación estructurada del proyecto.

---

### 6. Simulación del Entorno en la Nube

Aunque no se ejecuta en una nube real como AWS o GCP, el entorno simulado replica sus fases:

- Almacenamiento en SQLite como si fuera un almacén analítico.
- Automatización y despliegue mediante GitHub Actions.
- Visualización estructurada con MkDocs como portal web de documentación.

---

### 7. Flujo de Datos y Automatización

Desde `main.py` o `run.py`, puede ejecutarse el pipeline completo:

1.`ingestion.py` → genera `countries`

2.`cleaning.py` → transforma en `countries_clean`

3.`enrichment.py` → finaliza en `countries_enriched`

Cada script genera reportes de auditoría para trazabilidad.

---

### 8. Conclusiones y Recomendaciones

**Beneficios:**

- Flujo estructurado y automatizado.
- Datos enriquecidos para análisis geográfico.
- Documentación reproducible y clara.

**Limitaciones:**

- No hay paralelización ni procesamiento distribuido (sin Spark en producción).
- Simulación local, no cloud-native real.

**Recomendaciones:**

- Implementar el mismo flujo en AWS con S3 + Glue + Athena.
- Agregar validaciones más complejas.
- Considerar Spark para procesamiento a gran escala.
