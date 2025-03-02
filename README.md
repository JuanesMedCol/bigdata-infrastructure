# Proyecto Integrador de Infraestructura y arquitectura para Big Data 

Este proyecto está diseñado para realizar la ingesta de datos desde una API pública, almacenarlos en una base de datos SQLite y permitir su manipulación posterior. 

## Descripción

Este proyecto obtiene datos de la API [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts), que es un servicio de pruebas para desarrolladores. Los datos extraídos son almacenados en una base de datos SQLite local, permitiendo su análisis y manejo.

### Funcionalidades:
- Realiza una solicitud GET a la API para obtener datos.
- Almacena los datos en una base de datos SQLite.
- Evita duplicados en la base de datos mediante restricciones únicas.
- El archivo de base de datos se guarda en una carpeta específica dentro del proyecto.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes paquetes:

- Python 3.x
- SQLite3 (generalmente ya está incluido con Python)
- Bibliotecas adicionales de Python que puedes instalar con pip:

## Estructura del Proyecto en GitHub
```
[bigdata-infrastructure]
├── README.md
├── .github
│   └── workflows
│       └── bigdata.yml
└── src
    ├── static
    │   ├── auditoria
    │   │   └── ingestion.txt
    │   ├── db
    │   │   └── ingestion.db
    │   ├── csv
    │   │   └── ingestion.csv
    │   └── xlsx
    │       └── ingestion.xlsx
    └── ingestion.py
```
##  Instalación de las dependencias:
Una vez que tengas el archivo requirements.txt, puedes instalar todas las dependencias con:
```
pip install -r requirements.txt
```

## Uso
Ejecuta el script principal:
```
python ingestion.py
```

