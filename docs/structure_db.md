# 🗃️ Estructura de la Base de Datos `ingestion.db`

La base de datos contiene tres tablas principales que representan el flujo completo: desde los datos crudos hasta su versión enriquecida con coordenadas geográficas.

---

## 🔹 Tablas

=== "Ingestion"

    Tabla `countries` (datos crudos desde la API RESTCountries)

    | Campo       | Tipo     | Descripción                          |
    |-------------|----------|--------------------------------------|
    | pais        | TEXT     | Nombre común del país                |
    | capital     | TEXT     | Capital del país                     |
    | region      | TEXT     | Región general (ej: Americas)        |
    | subregion   | TEXT     | Subregión más específica             |
    | poblacion   | INTEGER  | Número de habitantes                 |
    | area        | REAL     | Área total del país (km²)            |

=== "Limpieza"

    Tabla `countries_clean` (después de limpieza)

    | Campo       | Tipo     | Descripción                          |
    |-------------|----------|--------------------------------------|
    | pais        | TEXT     | Nombre común del país (limpio)       |
    | capital     | TEXT     | Capital (rellenada si estaba vacía)  |
    | region      | TEXT     | Región                               |
    | subregion   | TEXT     | Subregión                            |
    | poblacion   | INTEGER  | Población con valores corregidos     |
    | area        | REAL     | Área con datos numéricos válidos     |

=== "Enriquecimiento"

    Tabla `countries_enriched` (con coordenadas geográficas)

    | Campo       | Tipo     | Descripción                          |
    |-------------|----------|--------------------------------------|
    | pais        | TEXT     | Nombre común del país                |
    | capital     | TEXT     | Capital                              |
    | region      | TEXT     | Región                               |
    | subregion   | TEXT     | Subregión                            |
    | poblacion   | INTEGER  | Población                            |
    | area        | REAL     | Área (km²)                           |
    | latitud     | REAL     | Coordenada geográfica: latitud       |
    | longitud    | REAL     | Coordenada geográfica: longitud      |

---

## Diagramas

=== "🧠 Clases y Flujo de Proceso"

    ```mermaid
    classDiagram
        class Countries {
            +TEXT pais
            +TEXT capital
            +TEXT region
            +TEXT subregion
            +INTEGER poblacion
            +REAL area
        }

        class CountriesClean {
            +TEXT pais
            +TEXT capital
            +TEXT region
            +TEXT subregion
            +INTEGER poblacion
            +REAL area
        }

        class CountriesEnriched {
            +TEXT pais
            +TEXT capital
            +TEXT region
            +TEXT subregion
            +INTEGER poblacion
            +REAL area
            +REAL latitud
            +REAL longitud
        }

        Countries --> CountriesClean : Limpieza
        CountriesClean --> CountriesEnriched : Enriquecimiento
    ```
=== "🔄 Flujo del Proceso"

    ```mermaid
    flowchart TD
        A[Ingesta desde RESTCountries API] --> B[Guardar en tabla countries]
        B --> C[Limpieza de datos]
        C --> D[Guardar en tabla countries_clean]
        D --> E[Consultar API OpenCage por capital]
        E --> F[Guardar coordenadas en countries_enriched]
    ```