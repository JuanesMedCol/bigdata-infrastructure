# Proyecto Integrador de Infraestructura y Arquitectura para Big Data

Este proyecto está diseñado para realizar la **ingesta** de datos desde una API pública, almacenarlos en una base de datos SQLite y permitir su posterior **limpieza y análisis** mediante scripts automatizados en Python.

## 🚀 **Descripción**

Este proyecto obtiene datos de la API [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts), que es un servicio de pruebas para desarrolladores. Los datos extraídos se almacenan en una base de datos SQLite local, permitiendo su análisis, limpieza y manipulación posterior.

### 🔥 **Funcionalidades:**

✅ Realiza una solicitud `GET` a la API para obtener datos.

✅ Almacena los datos en una base de datos SQLite.

✅ Evita duplicados en la base de datos mediante restricciones únicas.

✅ Exporta los datos a formatos **CSV** y **Excel** para su análisis.

✅ Limpia los datos, manejando valores nulos y datos duplicados.

✅ Genera un informe de auditoría detallado con el estado de los datos.

---

## 📂 **Estructura del Proyecto**

```
[bigdata-infrastructure]
│   .gitattributes
│   .gitignore
│   mkdocs.yml
│   README.md
│   requirements.txt
│   run.py
│   setup.py
│
├───.github
│   └───workflows
│           bigdata.yml
│
├───.qodo
│       history.sqlite
│
├───bigdata_infrastructure.egg-info
│       dependency_links.txt
│       PKG-INFO
│       requires.txt
│       SOURCES.txt
│       top_level.txt
│
├───build
│   └───bdist.win-amd64
├───docs
│       index.md
│       ingesta.md
│       limpieza.md
│
└───src
    │   cleaning.py
    │   ingestion.py
    │
    └───static
        ├───auditoria
        │       cleaning_report.txt
        │       ingestion_report.txt
        │
        ├───csv
        │       ingestion.csv
        │
        ├───db
        │       ingestion.db
        │
        └───xlsx
                cleaning.xlsx
                ingestion.xlsx
```

---

## 🛠️ **Requisitos**

Para ejecutar este proyecto, necesitas tener instalados los siguientes paquetes y herramientas:

* **Python 3.x**
* **SQLite3** (ya viene incluido con Python)
* Bibliotecas adicionales de Python que puedes instalar fácilmente usando `pip`

---

## 📥 **Instalación de las dependencias**

1. Clona el repositorio desde GitHub:

```bash
git clone https://github.com/JuanesMedCol/bigdata-infrastructure.git
```

2. Accede al directorio del proyecto:

```bash
cd bigdata-infrastructure
```

3. Instala las dependencias desde el archivo `requirements.txt` o usando el setup:

```bash
Opcion 1: pip install -r requirements.txt
Opcion 2: pip install .
```

---

## 🚀 **Ejecución del Proyecto**

Este script ejecuta en orden toda la rutina del programa:

```bash
python run.py
```

---

## 📊 Modelo de Base de Datos

### 🧩 Estructura de la tabla `posts`

La base de datos `ingestion.db` contiene la tabla `posts` donde se almacenan los datos obtenidos del API.

```sql
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    body TEXT
)
```

| Campo     | Tipo    | Descripción              |
| --------- | ------- | ------------------------- |
| `id`    | INTEGER | Identificador único (PK) |
| `title` | TEXT    | Título del post          |
| `body`  | TEXT    | Contenido del post        |

---

## 🧠 Diagrama Mermaid – Modelo de Datos

``` mermaid
erDiagram
    posts {
        INTEGER id PK
        TEXT title
        TEXT body
    }
```

---
