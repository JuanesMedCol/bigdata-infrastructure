## 📄 Ingesta de Datos desde API REST

Este script realiza la ingesta de datos desde un endpoint público (`https://jsonplaceholder.typicode.com/posts`) y los procesa en diferentes formatos. A continuación, se documenta cada etapa del flujo.

---

### 🚀 Inicio del Proceso

* Se establece la configuración de `logging` para mostrar mensajes en consola.
* Se define la URL de la API.

```
url = 'https://jsonplaceholder.typicode.com/posts'
```

---

### 🌐 Consulta a la API

* Se hace una solicitud `GET` a la API.
* Si la respuesta es exitosa (`status_code == 200`), se procesa la información.
* En caso de error, el script finaliza.

---

### 📁 Rutas y Directorios

El script crea las siguientes rutas para guardar los datos:

* `src/static/db/ingestion.db`: Base de datos SQLite
* `src/static/csv/ingestion.csv`: Archivo CSV
* `src/static/xlsx/ingestion.xlsx`: Archivo Excel
* `src/static/auditoria/ingestion_report.txt`: Reporte de auditoría

Se crean las carpetas automáticamente si no existen.

---

### 🗃️ Almacenamiento en Base de Datos

Se conecta a una base de datos SQLite y crea una tabla llamada `posts` con las siguientes columnas:

| Campo | Tipo    |
| ----- | ------- |
| id    | INTEGER |
| title | TEXT    |
| body  | TEXT    |

Luego se insertan los datos obtenidos desde el API.

---

### 📤 Exportación a Formatos

Se exportan los primeros 10 registros desde la base de datos a:

* **CSV** : `src/static/csv/ingestion.csv`
* **Excel** : `src/static/xlsx/ingestion.xlsx`

---

### 🕵️ Auditoría de Datos

El script verifica que los datos guardados coincidan con los datos obtenidos del API. Para cada registro:

* ✔️ Si el `title` y `body` coinciden con la base de datos → se cuenta como "coincidente".
* ❌ Si no hay coincidencia → se escribe en el archivo `ingestion_report.txt`.

#### 📊 Resumen generado:

```
✔️ Registros coincidentes: X
❌ Registros no encontrados: Y
```

---

### ✅ Fin del Proceso

El proceso termina con un mensaje de éxito:

```
Proceso finalizado correctamente ✅
```

---

### 📎 Archivos descargables

- [CSV de Ingesta](resultados/ingestion.csv)
- [Excel de Ingesta](resultados/ingestion.xlsx)
- [Reporte de Auditoría](resultados/ingestion_report.txt)

---

## 🧠 Diagrama del Proceso de Ingesta

```diagram
flowchart TD
    A[Inicio del proceso] --> B[Llamada a API externa - GET /posts]
    B --> C{Respuesta 200 OK}
    C -- Si --> D[Extraer datos en formato JSON]
    C -- No --> Z[Terminar con error]

    D --> E[Crear carpetas de salida]
    E --> F[Conectar a BD SQLite]
    F --> G[Crear tabla posts si no existe]
    G --> H[Insertar o reemplazar registros]

    H --> I[Cerrar conexion y confirmar]
    I --> J[Leer 10 registros con Pandas]
    J --> K[Exportar a CSV]
    J --> L[Exportar a Excel]

    K --> M[Generar informe de auditoria]
    L --> M

    M --> N[Comparar datos con BD]
    N --> O[Contar coincidencias y errores]
    O --> P[Escribir ingestion_report.txt]

    P --> Q[Fin del proceso]
```
