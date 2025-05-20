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

########################################### GRAFICOS #####################################################

EE_dept = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/dfi.csv")
BP_1950 = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/dfii.csv")
cantidad = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/dfiii.csv")
mails = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/Tablas_consultas/dfiv.csv")


#1



# Agrego Cant_BP por Provincia

consulta = duckdb.query(""" 
SELECT Provincia, sum(Cant_BP) as Cant_BP

FROM cantidad 
  
GROUP BY Provincia
ORDER BY Cant_BP

""") 
cantidad_prov = consulta.df()



# Dibujo usando pandas plot.bar sobre el DF agrupado
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

# Rotar etiquetas en x
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()




### 3

medianas = cantidad.groupby('Provincia')['Cant_EE'].median().sort_values()
orden_provincias = medianas.index.tolist()

fig, ax = plt.subplots(figsize=(10, 8))

plt.figure(figsize=(10, 8))
sns.boxplot(
    data=cantidad,
    x='Cant_EE',
    y='Provincia',
    order=orden_provincias,
    palette='Pastel1',
    ax=ax
)

# Títulos y ejes
ax.set_title('Cantidad de EE por Departamento segun Provincia')
ax.set_xlabel('Departamentos', fontsize='medium')
ax.set_ylabel('EE', fontsize='medium')
ax.set_xlim(0, 1500) 

plt.tight_layout()
plt.show()





### 4
cantidad['BP_per_1000'] = cantidad['Cant_BP'] / cantidad['Poblacion'] * 1000
cantidad['EE_per_1000'] = cantidad['Cant_EE'] / cantidad['Poblacion'] * 1000


print(cantidad[['BP_per_1000','EE_per_1000']].head(5))




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

'''
ax.set_title('BP vs EE por cada 1 000 habitantes\npor Departamento')
ax.set_xlabel('Bibliotecas Públicas por 1 000 hab.')
ax.set_ylabel('Establecimientos Educativos por 1 000 hab.')
plt.tight_layout()
plt.show()
'''


