# ProyectoSprint7
Este repositorio es el utilizado para el proyecto del sprint 7 del curso de Data Analysis de TripleTen.


---

Análisis Interactivo de Datos de Vehículos

Descripción del Proyecto

Esta aplicación web interactiva, desarrollada con Streamlit, permite analizar un conjunto de datos de anuncios de venta de vehículos. Proporciona herramientas para la visualización dinámica e intuitiva de información clave relacionada con el kilometraje, el precio y la condición de los vehículos.

Funcionalidades

Histograma Interactivo: Permite visualizar la distribución del kilometraje (`odometer`) de los vehículos en el conjunto de datos.

Gráfico de Dispersión: Explora la relación entre el kilometraje (`odometer`) y el precio (`price`) de los vehículos, con puntos coloreados según su condición (`condition`).

Interactividad: Los gráficos se generan dinámicamente al hacer clic en botones dedicados, ofreciendo una experiencia de usuario fluida y práctica.

Requisitos Previos
Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- Streamlit
- Pandas
- Plotly

Instalación
1. Clona este repositorio o descarga el código fuente.
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv vehicles_env
   source vehicles_env/bin/activate  # En macOS/Linux
   .\vehicles_env\Scripts\activate  # En Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install streamlit pandas plotly
   ```

Uso

1. Coloca el archivo de datos `vehicles_us.csv` en la misma carpeta que el script principal.
2. Ejecuta la aplicación con el siguiente comando:
   ```bash
   streamlit run nombre_del_archivo.py
   ```
3. Abre la aplicación en tu navegador y explora las visualizaciones interactivas.

Contribución

Si deseas contribuir a este proyecto, crea un *fork* del repositorio, realiza tus cambios en una rama separada y envía un *pull request*. ¡Todas las contribuciones son bienvenidas!

