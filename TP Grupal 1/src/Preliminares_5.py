# Laboratorio de Datos - TP 1.
# Trabajos Preliminares 5 - Limpieza y Formateo de DataSet -> Departamentos.

import pandas as pd 
# import duckbd as db 

'''
Lectura de DataSets.
'''

data_bibliotecas_populares = pd.read_csv("C:/Users/franp/OneDrive/Documentos/Pendientes/TP Grupal 1/DataSets Limpios/bibliotecas_populares.csv")
data_establecimientos_educativos = pd.read_csv("C:/Users/franp/OneDrive/Documentos/Pendientes/TP Grupal 1/DataSets Limpios/establecimientos_educativos.csv") 
data_poblacion = pd.read_csv("C:/Users/franp/OneDrive/Documentos/Pendientes/TP Grupal 1/DataSets Limpios/nivel_educativo_por_departamento.csv")


'''
ACLARACIÓN IMPORTANTE.
Todas las lineas con la instrucción 'print()' las dejo comentadas, porque es algo intermedio que usé para ver 
si funcionaba bien (lo que iba haciendo).
'''


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Estaría bueno saber cuántos son los departamentos totales con los que cuento. 
El DataSet correspondiente al 'Nivel Educativo por Departamento' tiene una fila por cada departamento. Es decir, el total de 
departamentos es el total de filas de ese DataSet. De todas formas, ya que estoy, verifico si todos los elementos de la columna 
'id_departamento' (de ese Dataset) son todos distintos (para volver a checkear que sean claves).
'''

cantidad_de_filas_1:int = data_poblacion['id_departamento'].count() 
# print("Cantidad total de filas en la columna 'id_departamento'': ", cantidad_de_filas_1)

valores_distintos_1:int = data_poblacion["id_departamento"].nunique() 
# print("Cantidad de valores de 'id_departamento' distintos: ", valores_distintos_1) 

'''
Como el número de elementos totales es igual al número de elementos distintos es la misma, puedo decir que son todos distintos. 
Ya que si hubiese alguno repetido, la cantidad de filas sería mayor a la cantidad de elementos distintos.
En total tenemos 527 departamentos distintos.
'''


# ----------------------------------------------------------------------------------------------------------------------------------- #

'''
Una vez hecho la verificación anterior, voy a tomar todos los elementos de las columnas 'nombre_departamento' y acomodarlos a un mismo 
formato string: todo en minúsculas y sin espacios.
Los espacios, como quiero eliminarlos todos (sean al principio, final o medio), para identificarlos voy a usar una expresión regular.
'''

# data_bibliotecas_populares['nombre_departamento'] = data_bibliotecas_populares['nombre_departamento'].str.replace(r'\s+', '', regex=True).str.lower() 
# data_establecimientos_educativos['nombre_departamento'] = data_establecimientos_educativos['nombre_departamento'].str.replace(r'/s+', '', regex=True).str.lower() 

# print(data_bibliotecas_populares['nombre_departamento'])
# print(data_establecimientos_educativos['nombre_departamento']) 




