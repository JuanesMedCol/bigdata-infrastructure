
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
├── README.md
├── .github
│   └── workflows
│       └── bigdata.yml
└── src
    ├── static
    │   ├── auditoria
    │   │   ├── ingestion_report.txt
    │   │   └── cleaning_report.txt
    │   ├── db
    │   │   └── ingestion.db
    │   ├── csv
    │   │   └── ingestion.csv
    │   ├── xlsx
    │   │   ├── ingestion.xlsx
    │   │   └── cleaning.xlsx
    ├── ingestion.py
    └── cleaning.py
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

### 👉 **1. Ingestión de Datos**

Este script extrae datos desde la API y los almacena en la base de datos:

```bash
python src/ingestion.py
```

* Guarda los datos en `src/static/db/ingestion.db`
* Genera archivos CSV y Excel en `src/static/csv/` y `src/static/xlsx/`
* Genera un informe de auditoría en `src/static/auditoria/ingestion_report.txt`

---

### 🧹 **2. Limpieza de Datos**

Este script limpia los datos previamente almacenados en la base de datos:

```bash
python src/cleaning.py
```

* Limpia duplicados y valores nulos
* Normaliza columnas numéricas
* Guarda resultados en formato Excel
* Genera un informe detallado en `src/static/auditoria/cleaning_report.txt`

---

## ⚙️ **Automatización con GitHub Actions**

El proceso de ingestión y limpieza está automatizado mediante GitHub Actions. El flujo de trabajo está definido en:

```
.github/workflows/bigdata.yml
```

* La ingestión de datos se ejecuta automáticamente al realizar un **push** a la rama `main` o cada hora mediante una programación `cron`.
* Si la ingestión es exitosa, se ejecutará automáticamente el proceso de limpieza.

---

## ✅ **Resultados**

📊 **Datos de la ingestión:**

* `ingestion.db` – Base de datos SQLite con los datos ingeridos
* `ingestion.csv` – Datos exportados en formato CSV
* `ingestion.xlsx` – Datos exportados en formato Excel

🧽 **Resultados de la limpieza:**

* `cleaning.xlsx` – Datos limpios exportados en formato Excel
* `cleaning_report.txt` – Informe detallado de la limpieza

---

## 🚨 **Posibles Errores y Soluciones**

| Error                        | Causa                                              | Solución                                                                                    |
| ---------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `Error 404`                | La API no está disponible                         | Verifica la URL y la disponibilidad de la API                                                |
| `sqlite3.OperationalError` | Problema de permisos o bloqueo de la base de datos | Asegúrate de que no haya otra conexión activa a la base de datos                           |
| `ImportError`              | Módulo no encontrado                              | Asegúrate de haber instalado todas las dependencias con `pip install -r requirements.txt` |

---

## 👨‍💻 **Contribuciones**

¡Las contribuciones son bienvenidas! Si deseas colaborar, sigue estos pasos:

1. Haz un fork del repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz un commit (`git commit -m "Descripción de cambios"`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un **pull request**

---

## 📃 **Licencia**

Este proyecto está bajo la licencia  **MIT** . Consulta el archivo `LICENSE` para más información.

---

## 🌟 **Autor**

**[Juan Esteban Atehortua Sanchez]**
