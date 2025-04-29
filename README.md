# 📈 Análisis de Búsquedas en Google con Pytrends

Este proyecto explora las tendencias de búsqueda en Google utilizando la API no oficial de Google Trends: **Pytrends**. Se centra en el término **"Machine Learning"**, con un análisis por región, evolución temporal y comparación con otros términos en países específicos.

## 🔧 Requisitos

Antes de comenzar, asegúrate de tener Python instalado y ejecuta:

```bash
pip install pytrends pandas matplotlib
````

## 📊 ¿Qué se analiza?
1. Top 10 países con más búsquedas de "Machine Learning"
Usamos pytrends.interest_by_region() para obtener los datos y visualizar los resultados en un gráfico de barras.

2. Evolución de búsquedas en Estados Unidos
Se analiza la popularidad de "Machine Learning" en EE.UU. a lo largo del tiempo.

3. Comparación por años
Se comparan los años con mayor volumen de búsquedas en EE.UU. y en España.

4. Comparación de términos en España
Se comparan las búsquedas de "aprendizaje automático" y "redes neuronales" en los últimos 5 años.

## 🧪 Librerías utilizadas
  . pytrends: conexión con la API de Google Trends

  . pandas: manejo de dataframes

  . matplotlib: visualización de datos

## 📍 Conclusiones
  . Región con más búsquedas: China

  . Mayor volumen en EE.UU.: 2024

  . Mayor volumen en España: 2024

  . Término más buscado en España: redes neuronales

## 📁 Estructura del proyecto
| Carpeta/Archivo               | Descripción                       |
|------------------------------|-----------------------------------|
| `google_trends_analysis.py`  | Código principal del análisis     |
| `README.md`                  | Documentación del proyecto        |
| `.gitignore`                 | Archivos/directorios ignorados   |
| `requirements.txt`           | Dependencias del proyecto         |

## 📚 Referencias
  . Pytrends en GitHub

  . Google Trends


## ✅ Proyecto educativo para la exploración de datos y visualización usando tendencias de búsqueda reales.
