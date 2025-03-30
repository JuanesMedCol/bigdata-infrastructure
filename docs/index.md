# Proyecto Integrador de Infraestructura y Arquitectura para Big Data

Este proyecto está diseñado para realizar la **ingesta** de datos desde una API pública global, almacenarlos en una base de datos SQLite, permitir su posterior **limpieza**, **enriquecimiento geográfico** y análisis mediante scripts automatizados en Python.

## 🚀 **Descripción**

Este proyecto obtiene datos de la API [RESTCountries](https://restcountries.com/v3.1/all), que proporciona información sobre todos los países del mundo. Los datos extraídos se almacenan en una base de datos SQLite local, permitiendo su análisis, limpieza, enriquecimiento con coordenadas geográficas y manipulación posterior.

### 🔥 **Funcionalidades:**

✅ Realiza una solicitud `GET` para obtener datos de todos los países del mundo.

✅ Almacena los datos en una base de datos SQLite.

✅ Exporta los datos a formatos **CSV** y **Excel** para su análisis.

✅ Limpia los datos, manejando valores nulos y datos duplicados.

✅ Enriquecer cada país con su latitud y longitud usando la API de OpenCage.

✅ Genera informes de auditoría detallados con el estado de cada proceso.

---

## 📂 **Estructura del Proyecto**

```
[bigdata-infrastructure]
│   README.md
│   requirements.txt
│   run.py
│
├───docs
│       index.md
│       ingesta.md
│       limpieza.md
│       enrichment.md
│
└───src
    │   ingestion.py
    │   cleaning.py
    │   enrichment.py
    │
    └───static
        ├───auditoria
        │       ingestion_report.txt
        │       cleaning_report.txt
        │       enriched_report.txt
        ├───csv
        │       ingestion.csv
        ├───db
        │       ingestion.db
        └───xlsx
                ingestion.xlsx
                cleaning.xlsx
                enriched_data.xlsx
```

---

## 🛠️ **Requisitos**

Para ejecutar este proyecto necesitas tener instalado:

* **Python 3.x**
* **SQLite3**
* Bibliotecas de Python (ver `requirements.txt`) que incluyen:
  - `pandas`
  - `requests`
  - `openpyxl`
  - `tqdm`

---

## 🚀 **Ejecución del Proyecto**

Este script ejecuta en orden toda la rutina del programa:

```bash
python run.py
```

---

## 📊 Modelo de Base de Datos

### 🧩 Estructura de las tablas

#### Tabla `countries`

Contiene la información original obtenida desde la API.

#### Tabla `countries_clean`

Contiene los datos luego de ser limpiados.

#### Tabla `countries_enriched`

Contiene los datos enriquecidos con latitud y longitud.

```sql
CREATE TABLE IF NOT EXISTS countries (
    pais TEXT,
    capital TEXT,
    region TEXT,
    subregion TEXT,
    poblacion INTEGER,
    area REAL
)
```

---

## 🧠 Diagrama Mermaid – Flujo General

``` mermaid
flowchart TD
    A[Ingesta API RESTCountries] --> B[Guardar en SQLite y Excel]
    B --> C[Limpieza de Datos]
    C --> D[Guardar limpio en cleaning.xlsx y countries_clean]
    D --> E[Enriquecimiento con OpenCage]
    E --> F[Guardar enriquecido en enriched_data.xlsx y countries_enriched]
```