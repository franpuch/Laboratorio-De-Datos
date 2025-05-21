# -*- coding: utf-8 -*-
"""
Created on Sun May 18 15:36:45 2025

@author: Julia
"""
import duckdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
import scipy


########################################### GRAFICOS #####################################################

EE_dept = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/dfi.csv")
BP_1950 = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/dfii.csv")
cantidad = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/ConsultasSQL/dfiii.csv")
mails = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/dfiv.csv")
EEclean = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/EEclean.csv")
Departamentos= pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/DataSets Limpios/departamentos.csv")




######### 1 ##########

# Cant_BP por Provincia

consulta = duckdb.query(""" 
SELECT Provincia, sum(Cant_BP) as Cant_BP
FROM cantidad 
GROUP BY Provincia
ORDER BY Cant_BP
""") 
cantidad_prov = consulta.df()

# Cant_EE por Provincia
consulta2 = duckdb.query(""" 
SELECT Provincia, sum(Cant_EE) as Cant_EE
FROM cantidad 
GROUP BY Provincia
ORDER BY Cant_EE
""") 
cantidad_prov2 = consulta2.df()

# Grafico con esas tablas 
fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_prov.plot.bar(
    x='Provincia',
    y='Cant_BP',
    ax=ax,
    color='b',
    legend=False
)

# Ajustes
ax.set_title('Cantidad total de BP por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('BP', fontsize='medium')
ax.set_ylim(0, 550)

# Numeros arriba de cada barra
ax.bar_label(ax.containers[0], fontsize=6, padding=2)

# Roto etiquetas en x para que los nombres de las provincias queden claros
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()


## Mismo grafico q el anterior pero con EE

fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_prov2.plot.bar(
    x='Provincia',
    y='Cant_EE',
    ax=ax,
    color='b',
    legend=False
)

# Ajustes
ax.set_title('Cantidad total de EE por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('EE', fontsize='medium')
ax.set_ylim(0, 17000)

# Numeros arriba de cada barra
ax.bar_label(ax.containers[0], fontsize=6, padding=2)

# Roto etiquetas en x
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()


############## se me ocurrio hacer este grafico para poder comparar mejor, pero no se si se puede -> REVISAR

## Junto ambos gráficos para poder realizar una comparación mas eficiente

merge = duckdb.query(""" 
SELECT cantidad_prov.Provincia, cantidad_prov.Cant_BP, cantidad_prov2.Cant_EE
FROM cantidad_prov
INNER JOIN cantidad_prov2
ON cantidad_prov.Provincia = cantidad_prov2.Provincia 
ORDER BY cantidad_prov2.Cant_EE
""") 
cantidad_merge = merge.df()

cantidad_merge["Cant_BP"] = cantidad_merge["Cant_BP"]

# Dibujo usando pandas plot.bar sobre el DF agrupado
fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_merge.plot(
    kind='bar',
    x='Provincia',
    ax=ax
)

# Ajustes
ax.set_title('EE y BP por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('cantidad_EE', fontsize='medium')
ax.set_ylim(0, 17500)


# Rotar etiquetas en x
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()

#######################################


############# 2 ###############

# Grafico cada nivel educativo en graficos separados para que se puedan comprender mejor -> sacar mejores conclusiones

## JARDINES

fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

EE_dept.plot.scatter(
    x='poblacion_total',
    y='Jardines',
    ax=ax,
    color='b',
    legend=False
)
# Ajustes
ax.set_title('Cantidad total de Jardines por Provincia según población')
ax.set_xlabel('Poblacion (en millones)', fontsize='medium')
ax.set_ylabel('Jardines', fontsize='medium')
ax.set_ylim(0, 400)
ax.set_xlim(0,2500000)

## PRIMARIAS

fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

EE_dept.plot.scatter(
    x='poblacion_total',
    y='primarias',
    ax=ax,
    color='b',
    legend=False
)
# Ajustes
ax.set_title('Cantidad total de Primarias por Provincia según población')
ax.set_xlabel('Poblacion (en millones)', fontsize='medium')
ax.set_ylabel('Primarias', fontsize='medium')
ax.set_ylim(0, 550)


## SECUNDARIOS

fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

EE_dept.plot.scatter(
    x='poblacion_total',
    y='secundarios',
    ax=ax,
    color='b',
    legend=False
)
# Ajustes
ax.set_title('Cantidad total de Secundarias por Provincia según población')
ax.set_xlabel('Poblacion (en millones)', fontsize='medium')
ax.set_ylabel('Secundarios', fontsize='medium')
ax.set_ylim(0, 550)


## Bibliotecas por poblacion 
#Grafico la evolucion de la cantidad de BP a medida que aumenta la población (cada punto representa un departamento)

fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad.plot.scatter(
    x='Poblacion',
    y='Cant_BP',
    ax=ax,
    color='b',
    legend=False
)
# Ajustes
ax.set_title('Cantidad total de Bibliotecas por Departamento según población')
ax.set_xlabel('Poblacion (en millones)', fontsize='medium')
ax.set_ylabel('Bibliotecas Públicas', fontsize='medium')
ax.set_ylim(0, 60)


############## 3 ###############

medianas = cantidad.groupby('Provincia')['Cant_EE'].median().sort_values() #calcula la mediana de cada provincia (agrupadas) con respecto a la cantidad de EE por departamento
orden_provincias = medianas.index.tolist() #ordeno la tabla segun la mediana de cada provincia

fig, ax = plt.subplots(figsize=(10, 8))

plt.figure(figsize=(10, 8))
sns.boxplot(
    data=cantidad,
    x='Cant_EE',
    y='Provincia',
    order=orden_provincias,
    palette='Set2',
    ax=ax
)

# Títulos y ejes
ax.set_title('Cantidad de EE por Departamento segun Provincia')
ax.set_xlabel('Departamentos', fontsize='medium')
ax.set_ylabel('EE', fontsize='medium')
ax.set_xlim(0, 1800) 

plt.tight_layout()
plt.show()


## Mismo grafico pero con BP

medianas2 = cantidad.groupby('Provincia')['Cant_BP'].median().sort_values() 
orden_provincias2 = medianas2.index.tolist()

fig, ax = plt.subplots(figsize=(10, 8))

plt.figure(figsize=(10, 8))
sns.boxplot(
    data=cantidad,
    x='Cant_BP',
    y='Provincia',
    order=orden_provincias2,
    palette='Set2',
    ax=ax
)

# Títulos y ejes
ax.set_title('Cantidad de BP por Departamento segun Provincia')
ax.set_xlabel('Departamentos', fontsize='medium')
ax.set_ylabel('EE', fontsize='medium')
ax.set_xlim(0, 100) 

plt.tight_layout()
plt.show()



############## 4 ###############
cantidad['BP_per_1000'] = cantidad['Cant_BP'] / cantidad['Poblacion'] * 1000  #calculo la cantidad de BP y EE cada 1000 habitantes, por departamento
cantidad['EE_per_1000'] = cantidad['Cant_EE'] / cantidad['Poblacion'] * 1000

plt.figure(figsize=(8, 6))
ax = sns.scatterplot(
    data=cantidad,
    x='BP_per_1000',
    y='EE_per_1000',
    hue='Provincia',
    palette='tab10',
    s=60,
    alpha=0.8,
    legend='brief'
)

ax.legend(title='Provincia', bbox_to_anchor=(1, 1), loc='upper left')
plt.title('Cantidad de BP y EE cada 1000 habitantes por departamento', fontsize=13)
plt.tight_layout()
plt.show()



############# GRÁFICOS EXTRAS ###############

#### E-1

# Grafico la cantidad de EE pertenecientes a cada sector por provincia

conEx = duckdb.query(""" 
SELECT dept.nombre_provincia, dept.nombre_departamento,EEclean.id_establecimiento as id_establecimiento, EEclean.ambito AS ambito, EEclean.sector AS sector
FROM EEclean
INNER JOIN Departamentos as dept
ON dept.id_departamento = EEclean.id_localidad
""") 
extra = conEx.df()


# Agrupo y cuento por provincia y sector

extra_cons1 = duckdb.query(""" 
SELECT
  nombre_provincia,
  COUNT(CASE WHEN sector = 'Privado' THEN 1 END) AS privado,
  COUNT(CASE WHEN sector = 'Estatal' THEN 1 END) AS estatal
FROM extra
GROUP BY nombre_provincia
ORDER BY estatal
""") 
extra_conteo1 = extra_cons1.df()


# Dibujo usando pandas plot.bar sobre el DF agrupado
fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

extra_conteo1.plot(
    kind='bar',
    x = 'nombre_provincia',
    ax=ax
)

# Ajustes
ax.set_title('Sector por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('cantidad_EE', fontsize='medium')
ax.set_ylim(0, 15000)

# Rotar etiquetas en x
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()


### Mismo grafico pero con la columna 'ambito'

extra_cons = duckdb.query(""" 
SELECT
  nombre_provincia,
  COUNT(CASE WHEN ambito = 'Rural' THEN 1 END) AS rural,
  COUNT(CASE WHEN ambito = 'Urbano' THEN 1 END) AS urbano
FROM extra
GROUP BY nombre_provincia
ORDER BY urbano
""") 
extra_conteo = extra_cons.df()

fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

extra_conteo.plot(
    kind='bar',
    x='nombre_provincia',
    ax=ax
)

# Ajustes
ax.set_title('Ambito por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('cantidad_EE', fontsize='medium')
ax.set_ylim(0, 17500)

# Rotar etiquetas en x
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()



#### E-2

#Grafico un HEATMAP que nos pueda ayudar a relacionar EE con BP

extra_2 = duckdb.query(""" 
SELECT
  Provincia,
  sum(Cant_BP) as Cant_BP,
  sum(Cant_EE) as Cant_EE,
  sum(Poblacion) as poblacionTot
FROM cantidad
GROUP BY Provincia
ORDER BY Cant_EE
""") 
extra2 = extra_2.df() # Tomo la cantidad de BP y EE por provincia, y su poblacion total (para despues normalizar)

extra2["Cant_BP"] = extra2["Cant_BP"]/extra2["poblacionTot"] *1000  # Normalizo la tabla
extra2["Cant_EE"] = extra2["Cant_EE"]/extra2["poblacionTot"] *1000
extra2 = extra2.drop(columns="poblacionTot")

# Me aseguro de tener solo columnas numericas (de cantidad de BP y EE) y a la provincia como índice (para realizar el heatmap)
extra2_clust = extra2.set_index("Provincia")[["Cant_BP", "Cant_EE"]] 

a=sns.clustermap(
    extra2_clust,
    col_cluster=False,         
    method="single",           
    cmap="Blues",
    standard_scale=1           
)

a.fig.suptitle('Relación de promedios\n(sobre la cantidad de EE y BP por provincia)', y=0.90, fontsize=16)

plt.show()






