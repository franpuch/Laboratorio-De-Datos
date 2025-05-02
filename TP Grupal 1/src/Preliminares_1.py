# Laboratorio de Datos - TP 1.
# Trabajos Preliminares 1 - Exploración de DataSets.

import pandas as pd 

# Lectura de DataFrames.
bibliotecas_populares = pd.read_csv("C:/Users/franp/OneDrive/Documentos/Codes/Labo de Datos - TP 1/DataSets_Originales/Bibliotecas_Populares.csv")
establecimientos_educativos = pd.read_excel("C:/Users/franp/OneDrive/Documentos/Codes/Labo de Datos - TP 1/DataSets_Originales/Padron_Oficial_Establecimientos_Educativos_2022.xlsx", skiprows=6)

# ------------------------------------------------------------------------------------------------------------------------------- #
# Quiero ver si 'nro_conabip' dentro de 'bibliotecas_populares' es un valor único en cada fila.
# El objetivo es ver si podemos usarlo como clave única para identificar a cada biblioteca.

valores_distintos:int = bibliotecas_populares['nro_conabip'].nunique() 
print("Valores de 'nro_conabip' distintos: " , valores_distintos) 

cantidad_filas:int = bibliotecas_populares['nro_conabip'].count() 
print("Cantidad total de filas de 'bibliotecas_populares': " , cantidad_filas) 

# Como la cantidad de filas es igual a la cantidad de valores distintos (de 'nro_conabip'), son únicos 
# y puedo usarlos como identificador único. 

# ------------------------------------------------------------------------------------------------------------------------------- # 
# Quiero ver si 'Cueanexo' dentro de 'establecimientos_educativos' es un avlor único en cada fila.
# El objetivo es ver si podemos usarlo como clave única para identificar a cada establecimiento educativo.

valores_distintos = establecimientos_educativos['Cueanexo'].nunique() 
print("Valores de 'Cueanexo' distintos: " , valores_distintos) 

cantidad_filas = establecimientos_educativos['Cueanexo'].count() 
print("Cantidad total de filas de 'establecimientos_educativos': " , cantidad_filas) 

# Como la cantidad de filas es igual a la cantidad de valores distintos (de 'Cueanexo'), son únicos 
# y podemos usarlos como identificador único. 


# Fin. 