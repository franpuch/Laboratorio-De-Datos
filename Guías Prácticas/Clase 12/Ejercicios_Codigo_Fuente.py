# Ejercicios Clase 12 - Visualización de Datos (Parte 1).

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

data_ping:pd.DataFrame = sns.load_dataset('penguins') 

# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Ejercicio 2.
'''

# Chusmeo qué forma tiene y qué datos tiene.
# print(data_ping.head()) 

columnas_dataframe:list[str] = data_ping.columns
# print("Columnas del Dataframe: ", columnas_dataframe) 

cantidad_total_de_filas:int = len(data_ping) 
# print("Cantidad de filas en total: ", cantidad_total_de_filas) 

# Cuáles son las especies de pinguinos (distintas) consideradas.
especies_registradas:list[str] = data_ping['species'].unique() 
# print("Especies de pingüinos registradas: ", especies_registradas)

# Cuáles son las islas (distintas) consideradas.
islas_exploradas:list[str] = data_ping['island'].unique() 
# print("Islas exploradas: ", islas_exploradas) 


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Ejercicio 3.
'''

# Población de islas por especie.
poblacion_islas_especies = data_ping.groupby(['island', 'species']).size().unstack(fill_value=0) 
# print(poblacion_islas_especies)  

# Población total de cada isla.
poblacion_islas_total = data_ping.groupby('island').size()
# print(poblacion_islas_total)  

# Proporsiones de especies por cada isla.
proporciones_por_especie = poblacion_islas_especies.div(poblacion_islas_total, axis=0).round(2) 
proporciones_por_especie = (proporciones_por_especie * 100).round(1) 
# print(proporsiones_por_especie) 

# Antes de graficarlo, transformo 'proporciones_por_especie' a un dataframe de formato 'largo' (actualmente es 
# formato 'ancho')
proporciones_long = proporciones_por_especie.reset_index().melt(id_vars = 'island', 
                                                                var_name = 'species',
                                                                value_name = 'proporcion')
# print(proporciones_long) 
# Clave los métodos 'reset_index()' y 'melt(parametros)'. Repasarlos preguntando a GPT para qué se usan.

# Ahora sí, grafico en un gráfico de barras.
plt.figure()
sns.barplot(data = proporciones_long, x = 'island', y = 'proporcion', hue = 'species') # Importantísimo el parámetro 'hue'
                                                                                       # Consultarle a GPT detalles (para recordar).
plt.title('Proporción de Especies por Isla')
plt.xlabel('Islas')
plt.ylabel('Proporción (%)')
plt.legend(title = 'Especie')
plt.show()

# El gráfico de tortas no está incluído en SeaBorn, así que lo salteo. De igual forma, nunca es recomendable usar 
# gráficos de tortas (a menos que sea la forma más visual de representar, que por lo general nunca lo es).


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Ejercicio 4.
'''


