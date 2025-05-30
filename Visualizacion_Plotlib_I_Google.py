# -*- coding: utf-8 -*-
"""

# **Análisis de búsquedas en Google**

Cada día se realizan aproximadamente 3.500 millones de búsquedas en Google, lo que significa que cada segundo se realizan aproximadamente 40.000 búsquedas en Google.

Así que la búsqueda en Google es un gran caso de uso para el análisis de datos basados en las consultas de búsqueda.

Con esto en mente, en este proyecto,haremos un análisis de las búsquedas de Google con lo aprendido hasta ahora.

Google Trends es una herramienta de Goole que puede utilizarse para la analizar las búsquedas en Google.

Google Trends proporciona una API que se puede utilizar para analizar las búsquedas diarias en Google.

Esta API es conocida como **pytrends**, puedes instalarla fácilmente en tus sistemas utilizando el comando pip;

`pip install pytrends`

Una vez instalada, vamos a comenzar a analizar las búsquedas de Google:
"""

!pip install pytrends

"""Importamos las librerías necesarias"""

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

"""Vamos a crear un dataframe con el top de países con más búsquedas de "Machine Learning":"""

# usamos la librería trends para buscar por las keywords dadas
trends.build_payload(kw_list=["Machine Learning"])
# nos quedamos con los datos por región
data = trends.interest_by_region()

"""# 1. Muestra el top 10

Dado el dataframe anterior, ordénalo por la columna Machine Learning y muestra los 10 primeros valores.

Guarda estos 10 valores en un df que se llame data_10.
"""

# escribe tu código
data.sort_values(by='Machine Learning',ascending=False,inplace=True)
data_10 = data.head(10)
data_10

"""# 2. Crea un gráfico de barras

Con los datos anteriores, ahora puedes crear un gráfico de barras.

En el eje X deberán aparecer los países, mientras que en el eje Y deberán aparecer las búsquedas.
"""

# crea tu gráfico
x = data_10.index
y = data_10['Machine Learning']
plt.figure(figsize=(12, 6))
plt.bar(x, y, width=0.8)
plt.show()

"""# 3. Búsquedas en USA por años

Como todos sabemos, el machine learning ha sido el centro de atención de muchas empresas y estudiantes durante los últimos 3-4 años, así que echemos un vistazo a la tendencia de las búsquedas para ver cómo el total de consultas de búsqueda basadas en "Machine Learning" aumentó o disminuyó en Google:
"""

# obtenemos los datos con la API
data = TrendReq(hl='en-US', tz=360) # idioma y país
data.build_payload(kw_list=['Machine Learning']) # keyword Machine Learning
data = data.interest_over_time() # con tiempo

data.head(10)

"""Crea un gráfico en el que muestres los años en el eje X y las búsquedas en el eje Y."""

# Escribe aquí tu código
x = data.index
y = data['Machine Learning']
plt.figure(figsize=(12, 6))
plt.plot(x, y, marker='o')
plt.show()

"""# 4. Análisis

Teniendo en cuenta los gráficos anteriores:

a) ¿Cuál es la región con más búsquedas de Machine Learning?

b) ¿En qué años se ha obtenido más búsquedas de esa palabra en EEUU?

c) ¿Y para España? Utiliza el código para EEUU como pista y modifica lo necesario para España.

d) Representa en un mismo gráfico las búsquedas "aprendizaje automático" y "redes neuronales" para España. ¿Cuál tiene más búsquedas a lo largo de los últimos 5 años?

Respuesta a)
"""

sol_a ='China' # escribe la solución como string según lo saque el df

"""Respuesta b)"""

sol_b = 2024 # escribe el año como string. Ej: '1980'

"""Respuesta c)"""

sol_c = 2024 # escribe el año como string. Ej: '1980'

"""Respuesta d)"""

sol_d = 'redes neuronales' # escribe la búsqueda como string


  print('¡Felicidades! puedes avanzar al siguiente modulo \n El token es: ',pwd.hexdigest())
else:
  print('Hay algún error en el código o tu forma es diferente a la planteada, pregunta por el foro si no lo ves claro.')
