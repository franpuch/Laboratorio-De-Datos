# Laboratorio de Datos - TP 1. 
'''
Integrantes -> Dorogov Cristina 
            -> Pucciarelli Francisco Lautaro 
            -> Salto Julian 
               
Visualización y Gráficos.
'''

'''
Si aún no leyó el 'README', por favor leerlo.
'''

import duckdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
from pathlib import Path

'''
Preparación de los Path a los diferentes archivos y carpeta de destino.
'''

base_path = Path(__file__).resolve().parent                # Obtener la ruta base del script actual. 
consultas_path = base_path / 'ConsultasSQL'                # Ruta a la carpeta donde se van a guardar los DataSets limpios. 
graficos_path = base_path / 'Graficos_y_Visualizaciones'   # Ruta a la carpeta donde se guardan gráficos generados.
graficos_path.mkdir(exist_ok=True)                         # Si no existe la carpeta de salida, crearla.


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Lectura de DataSets.
'''

EE_dept = pd.read_csv(consultas_path / "dfi.csv")
BP_1950 = pd.read_csv(consultas_path / "dfii.csv")
cantidad = pd.read_csv(consultas_path / "dfiii.csv")


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Tarea Preliminar.
'''

# Tomo el promedio de CABA (agrupa las 15 comunas).

EE_dept_copia = EE_dept.copy()
cantidad_copia = cantidad.copy()

index = EE_dept[EE_dept['departamento'] == 'CIUDAD DE BUENOS AIRES'].index

EE_dept_copia.iloc[index,2] = EE_dept_copia.iloc[index,2] / 15
EE_dept_copia.iloc[index,3] = EE_dept_copia.iloc[index,3] / 15
EE_dept_copia.iloc[index,4] = EE_dept_copia.iloc[index,4] / 15
EE_dept_copia.iloc[index,5] = EE_dept_copia.iloc[index,5] / 15 
EE_dept_copia.iloc[index,6] = EE_dept_copia.iloc[index,6] / 15
EE_dept_copia.iloc[index,7] = EE_dept_copia.iloc[index,7] / 15
EE_dept_copia.iloc[index,8] = EE_dept_copia.iloc[index,8] / 15


index2 = cantidad[cantidad['Departamento'] == 'CIUDAD DE BUENOS AIRES'].index

cantidad_copia.iloc[index2,2] = cantidad_copia.iloc[index2,2] / 15 
cantidad_copia.iloc[index2,3] = cantidad_copia.iloc[index2,3] / 15 
cantidad_copia.iloc[index2,4] = cantidad_copia.iloc[index2,4] / 15 


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Gráficos.
'''

######### 1 ##########

# Cant_BP por Provincia.
consulta = duckdb.query(""" 
                        SELECT Provincia, sum(Cant_BP) as Cant_BP
                        FROM cantidad 
                        GROUP BY Provincia
                        ORDER BY Cant_BP
                        """) 
cantidad_prov = consulta.df()   # Sumo la cantidad de BP por provincia.

# Cant_EE por Provincia.
consulta2 = duckdb.query(""" 
                         SELECT Provincia, sum(Cant_EE) as Cant_EE
                         FROM cantidad 
                         GROUP BY Provincia
                         ORDER BY Cant_EE
                         """) 
cantidad_prov2 = consulta2.df()   # Sumo la cantidad de EE por provincia.

# Grafico con esas tablas.
fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_prov.plot.bar(x = 'Provincia',
                       y = 'Cant_BP',
                       ax = ax,
                       color = 'b',
                       legend = False)

# Ajustes.
ax.set_title('Cantidad Total de BP por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('BP', fontsize='medium')
ax.set_ylim(0, 550)

# Coloco los valores arriba de cada barra.
ax.bar_label(ax.containers[0], fontsize=6, padding=2)

# Roto etiquetas en 'x' para que los nombres de las provincias queden claros.
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig(graficos_path / "Grafico_A.png", dpi=300, bbox_inches='tight') 
plt.show()


## Mismo grafico que el anterior pero con EE.
fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_prov2.plot.bar(x = 'Provincia',
                        y = 'Cant_EE',
                        ax = ax,
                        color = 'b',
                        legend = False)

# Ajustes.
ax.set_title('Cantidad total de EE por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('EE', fontsize='medium')
ax.set_ylim(0, 17000)

# Coloco los valores arriba de cada barra.
ax.bar_label(ax.containers[0], fontsize=6, padding=2)

# Roto etiquetas en 'x'.
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig(graficos_path / "Grafico_B.png", dpi=300, bbox_inches='tight')
plt.show()


## Grafico extra -> Junto ambos gráficos anteriores para poder realizar una comparación mas eficiente.

merge = duckdb.query(""" 
                     SELECT cantidad_prov.Provincia, cantidad_prov.Cant_BP, cantidad_prov2.Cant_EE
                     FROM cantidad_prov
                     INNER JOIN cantidad_prov2
                     ON cantidad_prov.Provincia = cantidad_prov2.Provincia 
                     ORDER BY cantidad_prov2.Cant_EE
                     """) 
cantidad_merge = merge.df()   # Mergeo las 2 tablas que usé para los gráficos anteriores.

# Grafico.
fig, ax = plt.subplots(figsize = (12,6))
plt.rcParams['font.family'] = 'sans-serif'

# Aplico dos ejes Y, que tome cada uno un rango diferente (uno para BP y otro para EE).
cantidad_merge.set_index('Provincia')[['Cant_EE', 'Cant_BP']].plot(kind='bar',
                                                                   ax=ax,
                                                                   secondary_y='Cant_BP',   # 2do eje.
                                                                   color=['red', 'blue'])

# Ajustes.
ax.set_title('EE y BP por Provincia')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('cantidad EE', fontsize='medium')
ax.right_ax.set_ylabel('cantidad BP', fontsize='medium')
ax.set_ylim(0, 17500)

# Rotar etiquetas en 'x'.
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig(graficos_path / "Grafico_C.png", dpi=300, bbox_inches='tight')
plt.show()


### Extras -> Graficos iguales a los 2 primeros pero normalizados.

nuevo = duckdb.query(""" 
                     SELECT Provincia, sum(Cant_BP) as Cant_BP, sum(Cant_EE) as Cant_EE, sum(Poblacion) as Poblacion
                     FROM cantidad
                     GROUP BY Provincia 
                     """) 
cantidad_nuevo = nuevo.df()   # Sumo la cantidad de BP, EE y población por provincia, para luego normalizar.

cantidad_nuevo["Cant_EE"] = cantidad_nuevo["Cant_EE"]/cantidad_nuevo["Poblacion"] *1000   # Normalizo (cantidad de BP y EE cada 1000 habitantes).
cantidad_nuevo["Cant_BP"] = cantidad_nuevo["Cant_BP"]/cantidad_nuevo["Poblacion"] *1000
cantidad_nuevo = cantidad_nuevo.sort_values(by='Cant_EE')

## Grafico con EE.
fig, ax = plt.subplots(figsize=(12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_nuevo.plot.bar(x = 'Provincia',
                        y = 'Cant_EE',
                        ax = ax,
                        color = 'b',
                        legend = False)

# Ajustes.
ax.set_title('Cantidad total de EE por Provincia (Normalizado)')
ax.set_xlabel('Provincias', fontsize='medium')
ax.set_ylabel('EE', fontsize='medium')
ax.set_ylim(0, 3)

# Coloco los valores arriba de cada barra.
ax.bar_label(ax.containers[0], fmt = '%.3f', fontsize = 6, padding = 2)   # El fmt='%.3f' sirve para tomar solo 3 decimales. 

# Roto etiquetas en 'x'.
plt.xticks(rotation = 45, ha = 'right', fontsize = 8)
plt.tight_layout()
plt.savefig(graficos_path / "Grafico_D.png", dpi=300, bbox_inches='tight')
plt.show()

## Ahora grafico pero con BP.
cantidad_nuevo = cantidad_nuevo.sort_values(by = 'Cant_BP')

fig, ax = plt.subplots(figsize = (12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_nuevo.plot.bar(x = 'Provincia',
                        y = 'Cant_BP',
                        ax = ax,
                        color = 'b',
                        legend = False)

# Ajustes.
ax.set_title('Cantidad total de BP por Provincia (Normalizado)')
ax.set_xlabel('Provincias', fontsize = 'medium')
ax.set_ylabel('BP', fontsize = 'medium')
ax.set_ylim(0, 0.35)

# Coloco los valores arriba de cada barra.
ax.bar_label(ax.containers[0], fmt = '%.3f', fontsize = 6, padding = 2)

# Roto etiquetas en 'x'.
plt.xticks(rotation = 45, ha = 'right', fontsize = 8)
plt.tight_layout()
plt.savefig(graficos_path / "Grafico_E.png", dpi=300, bbox_inches='tight')
plt.show()


############# 2 ############### 

# Grafico cada nivel educativo en graficos separados para que se puedan comprender mejor (sacar mejores conclusiones).

## JARDINES.
fig, ax = plt.subplots(figsize = (12,6))
plt.rcParams['font.family'] = 'sans-serif'

EE_dept_copia.plot.scatter(x = 'poblacion_total',
                     y = 'Jardines',
                     ax = ax,
                     color = 'b',
                     legend = False)

ax.set_xscale('log')   # Aplico escala logarítmica para mayor separación entre los puntos -> Gráfico más comprensible.

# Ajustes.
ax.set_title('Cantidad de Jardines vs Población')
ax.set_xlabel('Poblacion (escala log)', fontsize = 'medium')
ax.set_ylabel('Jardines', fontsize = 'medium')
ax.set_ylim(0, 400) 
plt.savefig(graficos_path / "Grafico_F.png", dpi=300, bbox_inches='tight') 
plt.show() 

## PRIMARIAS.

fig, ax = plt.subplots(figsize = (12,6))
plt.rcParams['font.family'] = 'sans-serif'

EE_dept_copia.plot.scatter(x = 'poblacion_total',
                     y = 'primarias',
                     ax = ax,
                     color = 'b',
                     legend = False)
ax.set_xscale('log')

# Ajustes.
ax.set_title('Cantidad de Primarias vs Población')
ax.set_xlabel('Poblacion (escala log)', fontsize = 'medium')
ax.set_ylabel('Primarias', fontsize = 'medium')
ax.set_ylim(0, 450)
plt.savefig(graficos_path / "Grafico_G.png", dpi=300, bbox_inches='tight')
plt.show()


## SECUNDARIOS.

fig, ax = plt.subplots(figsize = (12,6))
plt.rcParams['font.family'] = 'sans-serif'

EE_dept_copia.plot.scatter(x = 'poblacion_total',
                     y = 'secundarios',
                     ax = ax,
                     color = 'b',
                     legend = False)
ax.set_xscale('log')

# Ajustes.
ax.set_title('Cantidad de Secundarias vs Población')
ax.set_xlabel('Poblacion (escala log)', fontsize = 'medium')
ax.set_ylabel('Secundarios', fontsize = 'medium')
ax.set_ylim(0, 500)
plt.savefig(graficos_path / "Grafico_H.png", dpi=300, bbox_inches='tight')
plt.show()


## Bibliotecas por Poblacion.
# Grafico la evolucion de la cantidad de BP a medida que aumenta la población (cada punto representa un departamento).

fig, ax = plt.subplots(figsize = (12,6))
plt.rcParams['font.family'] = 'sans-serif'

cantidad_copia.plot.scatter(x = 'Poblacion',
                      y = 'Cant_BP',
                      ax = ax,
                      color = 'b',
                      legend = False)
ax.set_xscale('log')

# Ajustes.
ax.set_title('Cantidad de Bibliotecas vs Población')
ax.set_xlabel('Poblacion (escala log)', fontsize = 'medium')
ax.set_ylabel('Bibliotecas Públicas', fontsize = 'medium')
ax.set_ylim(0, 60)
plt.savefig(graficos_path / "Grafico_I.png", dpi=300, bbox_inches='tight')
plt.show()


############## 3 ###############

medianas = cantidad.groupby('Provincia')['Cant_EE'].median().sort_values()   # Calcula la mediana de cada provincia (agrupadas) con respecto a la cantidad de EE por departamento.
orden_provincias = medianas.index.tolist()   # Ordeno la tabla segun la mediana de cada provincia.

fig, ax = plt.subplots(figsize = (10, 8))

plt.figure(figsize = (10, 8))
sns.boxplot(data = cantidad,
            x = 'Cant_EE',
            y = 'Provincia',
            order = orden_provincias,
            palette = 'Set2',
            ax = ax)

# Títulos y ejes.
ax.set_title('Cantidad de EE por Departamento segun Provincia')
ax.set_xlabel('Cantidad de EE', fontsize = 'medium')
ax.set_ylabel('Provincias', fontsize = 'medium')
ax.set_xlim(0, 1800) 

plt.tight_layout()
plt.savefig(graficos_path / "Grafico_J.png", dpi=300, bbox_inches='tight')
plt.show()


## Mismo grafico pero con BP.

medianas2 = cantidad.groupby('Provincia')['Cant_BP'].median().sort_values()   # Calcula la mediana de cada provincia (agrupadas) con respecto a la cantidad de BP por departamento.
orden_provincias2 = medianas2.index.tolist()

fig, ax = plt.subplots(figsize = (10, 8))

plt.figure(figsize = (10, 8))
sns.boxplot(data = cantidad,
            x = 'Cant_BP',
            y = 'Provincia',
            order = orden_provincias2,
            palette = 'Set2',
            ax = ax)

# Títulos y ejes.
ax.set_title('Cantidad de BP por Departamento segun Provincia')
ax.set_xlabel('Cantidad de BP', fontsize = 'medium')
ax.set_ylabel('Provincias', fontsize = 'medium')
ax.set_xlim(0, 60) 

plt.tight_layout()
plt.savefig(graficos_path / "Grafico_K.png", dpi=300, bbox_inches='tight')
plt.show()


############## 4 ###############

cantidad_copia['BP_per_1000'] = cantidad_copia['Cant_BP'] / cantidad_copia['Poblacion'] * 1000   # Calculo la cantidad de BP y EE cada 1000 habitantes, por departamento (para normalizar).
cantidad_copia['EE_per_1000'] = cantidad_copia['Cant_EE'] / cantidad_copia['Poblacion'] * 1000

plt.figure(figsize = (8, 6))
ax = sns.scatterplot(data = cantidad_copia,
                     x = 'BP_per_1000',
                     y = 'EE_per_1000',
                     hue = 'Provincia',   # Color de cada punto según a la provincia a la que pretenece ese departamento.
                     palette = 'tab10',
                     s = 60,   # Tamaño de los puntos.
                     alpha = 0.8,   # Transparencia de cada punto (para poder hacer visible la superposición de valores).
                     legend = 'brief')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylabel('Cantidad de EE (escala log)', fontsize='medium')
ax.set_xlabel('Cantidad de BP (escala log)', fontsize='medium')
ax.legend(title = 'Provincia', bbox_to_anchor = (1, 1), loc = 'upper left')   # Agrego la leyenda fuera del gráfico con las provincias y sus respectivos colores.
plt.title('Cantidad de BP y EE cada 1000 habitantes por departamento', fontsize = 13)
plt.tight_layout()
plt.savefig(graficos_path / "Grafico_L.png", dpi=300, bbox_inches='tight')
plt.show()


############# GRÁFICOS EXTRAS ###############

#### E-1.

# Grafico un HEATMAP que nos pueda ayudar a relacionar EE con BP.

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
extra2 = extra_2.df()   # Tomo la cantidad de BP y EE por provincia, y su poblacion total (para despues normalizar).

extra2["Cant_BP"] = extra2["Cant_BP"]/extra2["poblacionTot"] *1000   # Normalizo la tabla.
extra2["Cant_EE"] = extra2["Cant_EE"]/extra2["poblacionTot"] *1000
extra2 = extra2.drop(columns="poblacionTot")

# Me aseguro de tener solo columnas numericas (de cantidad de BP y EE) y a la provincia como índice (para realizar el heatmap).
extra2_clust = extra2.set_index("Provincia")[["Cant_BP", "Cant_EE"]] 

a = sns.clustermap(extra2_clust,
                   col_cluster = False,   # Para que no se agrupen las columnas, si no las filas (provincias).
                   method = "single",   # Impone un orden a las provincias (relaciona provincias para formar cadenas).      
                   cmap = "Blues",
                   standard_scale = 1   # Para comparar a las provincias entre sí.
                   )

a.fig.suptitle('Relación entre provincias\n(sobre la cantidad de EE y BP)', y = 0.90, fontsize = 16)
plt.savefig(graficos_path / "Grafico_M.png", dpi=300, bbox_inches='tight')
plt.show()


# Fin del archivo.
 