## 🧼 Limpieza de Datos

Este módulo toma los datos generados en la fase de ingesta y aplica un proceso de **limpieza y transformación** para prepararlos para análisis posteriores.

---

### 📁 Archivos de Entrada y Salida

* **Entrada**: Base de datos `ingestion.db`, tabla `countries`
* **Salida**:
  - `cleaning.xlsx`: archivo Excel con los datos limpios
  - `ingestion.db`, tabla `countries_clean`: versión limpia en SQLite
  - `cleaning_report.txt`: informe de auditoría

---

### 🧠 ¿Qué hace este script?

✅ Elimina registros duplicados.

✅ Llena valores nulos:
- Números: con la media de la columna
- Textos: con el valor anterior no nulo (`ffill`)

✅ Convierte tipos de datos (`poblacion`, `area`) a numéricos.

✅ Exporta los resultados a Excel y también los guarda como una nueva tabla en la base de datos (`countries_clean`).

✅ Genera un reporte de auditoría con:
- Cantidad de registros antes y después de limpieza
- Columnas con valores nulos
- Cantidad de duplicados

---

### 📋 Estructura de la Tabla `countries_clean`

Es idéntica a `countries` pero con datos procesados y sin inconsistencias.

---

### 📝 Ejemplo del Informe `cleaning_report.txt`

```
📋 Informe de Limpieza de Datos

Número total de registros: 250
Número de valores nulos por columna:
pais         0
capital     12
region       0
subregion    5
poblacion    1
area         0
dtype: int64
Número de registros duplicados: 0

✅ Número de registros después de limpieza: 250
```

---

### 🧪 Diagrama Mermaid – Flujo de Limpieza

``` mermaid
flowchart TD
    A[Leer datos de countries en SQLite] --> B[Eliminar duplicados]
    B --> C[Imputar valores nulos]
    C --> D[Convertir tipos: poblacion y area]
    D --> E[Guardar como cleaning.xlsx]
    D --> F[Guardar en tabla countries_clean]
    F --> G[Generar cleaning_report.txt]
```

---

### ✅ Resultado

Los datos ahora están preparados para ser enriquecidos o analizados, sin problemas de duplicación ni valores faltantes críticos.