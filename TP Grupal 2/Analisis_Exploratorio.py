# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 23:19:27 2025

@author: franp
"""

"""
TP 2 - Laboratorio de Datos.

Etapa 1 - Análisis Exploratorio.
"""


# --------------------------------------------------------------------------------------------------------------------------------------- #
# %%
"""
Imports de Módulos.
"""

import numpy as np
import pandas as pd
import duckdb as dk
import matplotlib.pyplot as plt
import seaborn as sns 


# --------------------------------------------------------------------------------------------------------------------------------------- #
# %% 
""" 
Carga del DataSet.
"""

data_fashion:pd.DataFrame = pd.read_csv("C:/Users/franp/OneDrive/Documentos/Codes/TP Grupal 2/DataSets_Original.csv")
# COMPLETAR CON EL PATH AL DATASET ORIGINAL.


"""
Aclaración Importante: 
Todas las instrucciones 'print()' las dejo comentadas, son verificaciones rápidas que fuí haciendo para ver si lo que iba haciendo 
era correcto o no. Lo único que hacen es imprimir mensajes o resultados intermedios.
"""


# --------------------------------------------------------------------------------------------------------------------------------------- #
# %% 
"""
Exploración Inicial: entendiendo qué tiene el DataSet.
"""

"""
Quiero ver cuáles son todas las clasificaciones de prendas distintas.
OBS -> De paso le hago 'sort', ya que si las imprimo así nomas, no me quedan ordenadas y es mas dificil saber qué numeros hay y cuáles no.
"""

clasificacion_prendas = data_fashion["label"].unique()
clasificacion_prendas = sorted(clasificacion_prendas) 
# print("Clasificaciones de Prendas: " , clasificacion_prendas)


"""
Características básicas:
    
- Imágenes de 28x28 pixeles.
- Cada columna es el valor del color que debe tener cada pixel -> Hay 28x28 = 784 columnas.
- Hay 70.000 filas; es decir, 70.000 imágenes.

- La última columna, llamada 'label', es el tipo de prenda al que representa esa imágen.
- Tenemos 10 clasificaciones de prendas distintas: 0 a 9.
"""


# --------------------------------------------------------------------------------------------------------------------------------------- #
# %%
"""
Necesito buscar patrones que me permitan identificar qué píxeles tienen información importante y qué píxeles no.

Mi primera idea es ver si ciertos píxeles tienen valores distintivos en cada tipo de prenda (para cada clasificación).
"""

"""
Voy a realizarlo con una consulta SQL. 
Lo que busco hacer es una consulta que le calcule el AVG (promedio) a cada pixel de cada tipo de prenda. Hay 784 píxeles, es inviable escribir
'AGV(columna)' para cada columna dentro de la consulta. Así que primero voy a hacer una función que me genere automaticamente esas sentencias.
"""

columnas_pixeles:list[str] = [f"pixel{i}" for i in range(0, 784)]   # Aquí tengo todos los nombres de las columnas.
# print(columnas_pixeles[0])   # A ver cómo quedó el primero.
# print(columnas_pixeles[15])  # A ver cómo quedó uno del medio.
# print(columnas_pixeles[-1])  # A ver cómo quedó el último.

"""
La sentencia la armo como un solo string, le pongo un salto de línea para que sea entendible cuando la imprima para verificar cómo quedó.
"""
sentencias_AVG:str = ", \n".join([f"AVG({col}) AS avg_{col}" for col in columnas_pixeles])

"""
Ahora sí, hago la consulta.
"""
consulta_1:str = f"""
                 SELECT label, 
                        {sentencias_AVG}
                 FROM data_fashion 
                 GROUP BY label 
                 ORDER BY label
                 """
promedio_pixel_por_clase:pd.DataFrame = dk.query(consulta_1).df()  
# print(promedio_pixel_por_clase.head(10))  

"""
Ok, ahora me gustaría graficar lo que me quedó del promedio de cada clase.
Aquí lo que voy a estar haciendo es visualizando cuál es la "imágen promedio" de cada una de las imágenes que pertenecen a cada clase.
Es decir, para cada clase, obtendé la imágen promedio.
"""
for i in range(10):
    imagen = np.array(promedio_pixel_por_clase.iloc[i, 1:]).reshape(28, 28)

    plt.figure()                
    plt.imshow(imagen, cmap="gray")
    plt.title(f"Imagen Promedio - Clase {i}")
    plt.axis('off')   # En estos gráficos, los ejes no me aportan nada. Los saco.
    

"""
Análisis de los gráficos. 

A partir de estas imágenes podemos establecer una mejor clasificación para los distintos tipos de prendas.
De forma aproximada, lo que observamos es:
    
- Clase 0 -> Prenda Superior: Mangas Cortas.
- Clase 1 -> Prenda Inferior: Pantalón Largo.
- Clase 2 -> Prenda Superior: Mangas Largas.
- Clase 3 -> Prenda Completa: Vestido Largo, Mangas Cortas.
- Clase 4 -> Prenda Superior: Mangas Largas.
- Clase 5 -> Zapato de Mujer.
- Clase 6 -> Prenda Superior: Mangas Largas.
- Clase 7 -> Zapatillas.
- Clase 8 -> Accesorio: Bolso de Mujer.
- Clase 9 -> Botas.

A partir de esto podemos suponer que cada Clase va a representar variantes del tipo de prenda que refleja su promedio.

Además de eso, notamos que hay Clases muy parecidas entre sí. Las Clases 2, 4 y 6 parecen representar variantes de la misma pieza: 
prendas de mangas largas.
Dificil diferenciar si se trata de remeras, abrigos, camisas (formales), etc; también si se trata de prendas masculinas o femeninas.
Las Clases 5, 7 y 9 queda claro que corresponden a calzados. Mas no creemos que sean lo suficientemente claras como para diferenciar 
tipos de calzados en cada clase. 

En cuanto a los píxeles con información importante, podemos notar lo siguiente.
Parece ser una constante que los píxeles de los bordes se mantienen siempre en negro, y que los píxeles del centro de cada imágen 
se mantienen siempre en blanco.
No nos parece correcto pensar en píxeles que no aportan información en todas las clases. Nos parece más apropiado ir Clase por Clase, 
diferenciando aquellos píxeles que se mantienen constantes en el promedio. Por ejemplo: En la Clase 1, podemos generalizar que los 
pixeles que aportan información relevante son aquellos que se mantienen más en el medio; los demás parecen mantener un promedio de negro.
Sin embargo, por ahora decidimos no sacar conclusiones al respecto. Vamos a esperar el análisis posterior para poder cerrar esta conclusión.
"""


# --------------------------------------------------------------------------------------------------------------------------------------- #
# %%
"""
Para poder hacer un análisis más fino sobre cuáles son aquellos píxeles que podrían descartarse (porque no aportan información), proponemos
el siguiente paso. 
Calcular la varianza de cada píxel en todo el DataSet (no separando por clase). Esto puede darnos una mejor idea de cuáles son los píxeles 
que no aportan información. Ya que podremos diferenciar más claramente cuáles son "casi siempre" negro, cuáles son "casi siempre" 
blancos y cuáles se mueven en un rango de grises (a veces más negro y a veces más blanco).
No vemos demasiado sentido separar por Clases para hacer este análisis, ya que buscamos aquellos píxeles que siempre (o casi siempre) se 
mantienen totalmente encendidos (blanco) o totalmente apagados (negro). No nos importa la Clase de la prenda que se oculta en la imágen 
(por ahora...), queremos mirar todo.
Vamos a buscar los píxeles que se mantienen siempre (o casi siempre) en blanco y aquellos que se mantienen siempre (o casi siempre) en 
negro. Estos son píxeles que, consideramos, no aportan información para diferenciar Clases (y, más adelante, buscar predecir); y que 
podríamos "descartar". 
"""


"""
Para empezar, calculo la varianza de cada píxel.
Recupero de la sección anterior 'columnas_pixeles', la lista de todos los nombres de todas las columnas de los píxeles.
"""
varianzas_pixeles = data_fashion[columnas_pixeles].var()
# print(varianzas_pixeles.head(10)) 

"""
Para poder visualizar esta informaación, construyo un histograma con la información obtenida.
La idea es ver cuáles son los valores de varianza que más cantidad de píxeles tienen.
"""
nbins = 70   # Tiré varios tamaños y este es el que me permite visualizar mejor.
f, s1 = plt.subplots()
plt.suptitle('Distribución de las Varianzas de los Pixeles', size = 'large')

sns.histplot(data = varianzas_pixeles, bins = nbins, ax = s1)
s1.set_xlabel('Varianza') 
s1.set_ylabel('Frecuencia') 

"""
A partir de este gráfico podemos visualizar mejor cómo se distribuya la variaza a lo largo de todos los píxeles.
Es fácil notar que tenemos múchos píxeles con varianza pequeña. Esto se corresponde con que el primer bin más cercano a cero,
es el que mayor altura tiene; siendo este bin el que almacena a aquellos pixeles que tienen varianza muy muy cercana a cero.
Esto se corresponde con píxeles que siempre se mantienen apagados (siempre en negro) o encendidos (siempre en blanco). 
Sin embargo, también podemos observar que en el otro extremo del histograma, también hay una buena cantidad de datos.
Aquellos bins en los valores mayores del eje horizontal, se corresponden con las varianzas de valores altos. Notamos que 
tenemos muchos bins con alturas considerables, lo que nos dice que contamos con una buena cantidad de píxeles que tienen 
varianza muy alta. Estos son los píxeles que vamos a buscar priorizar para entrenar los modelos. Consideramos que estos son 
los que van a marcar la diferencia a la hora de entrenar y mejorar la taza de acierto en las predicciones.
"""


"""
Construyo un Heatmap a partir de las varianzas. A ver si este gráfico aporta algo de 
información inetresante...
"""
heatmap_varianzas = varianzas_pixeles.values.reshape(28, 28)

plt.figure(figsize=(6, 6))
sns.heatmap(heatmap_varianzas, cmap="viridis", cbar=True)
plt.title("Mapa de Calor de la Varianza de Cada Píxel")
plt.axis('off')
plt.show()

"""
En este gráfico podemos observar mejor cuáles son aquellas zonas que, en general, menor varianza tienen. Es decir, 
cuáles son las zonas que menos cambian a lo largo de todas las imágenes. Dándonos una idea de cuáles son los
píxeles que deberíamos descartar. Podemos observar que las zonas bordes y centrales mantienen colores oscuros. 
Estos representan píxeles con varianza pequeña, candidatos a ser descartados para el entrenamiento de los modelos.

También notamos que aquellas zonas con colores más claros contienen a los píxeles de mayor varianza. Estos van a ser 
los que más tomemos en cuenta para la etapa de entrenamiento. Ya que son los que más varían imagen a imagen, y los que
mejor caracterizan los cambios de Clases.
"""


# --------------------------------------------------------------------------------------------------------------------------------------- #
# %%
"""
A partir del gráfico (heatmap de la sección anterior), voy a definir un umbral de varianza mínimo. Me voy a quedar con todos los píxeles 
que tienen varianza mayor a ese umbral.
Busco que el umbral sea lo mas ajustado posible a aquellas zonas con píxeles de muy poca varianza. Sin embargo, no quiero pasarme. Ya 
que los píxeles con una varianza no muy alta (pero tampoco lo suficientemente baja) van a serme útiles en el análisis posterior 
(siguiente sección). 

Visualizando el gráfico, determino el UMBRAL = 5000

Este umbral parece incluír a los píxeles que pertenecen a los bordes (de las imágenes) y al centro. Coherente con esta idea de que,
en todas las ímagenes, los bordes siempre son colores muy cercanos al negro (absoluto), y el centro son colores muy cercanos al 
blanco (absoluto). 
"""
umbral_global:int = 5000


"""
Como dijo Jack, vamos por partes...
Primero tomo el DataFrame 'varianzas_pixeles' y armo una lista donde almacene los index de las filas que tienen valor mayor a mi
umbral.
"""
columnas_utiles_global:list[str] = varianzas_pixeles[varianzas_pixeles > umbral_global].index.tolist() 

"""
Ahora voy al DataFrame con los datos originales, y me quedo sólo con las columnas que rescaté.
"""
columnas_utiles_con_label = columnas_utiles_global + ['label']
data_filtrada_1 = data_fashion[columnas_utiles_con_label]

"""
Ahora sí vamos por clase. 
Resulta que, si miramos clase por clase, aquellos píxeles más representativos de cada clase son aquellos píxeles que menor varianza tienen
(dentro de esa clase). Un ejemplo: tengo 10 remeras mangas cortas, cada una con un estampado diferente. Le calculo la varinza a los píxeles
de esa clase:
    - Los píxeles con mayor varianza van a ser aquellos donde se encuentra la estampa de cada remera.
    - Los píxeles con menor varianza van a ser aquellos que moldean la remera.
De esa forma, es fácil nota que aquellos píxeles que representan y mejor caracterizan a las remeras mangas corta, son aquellos que menos 
cambian entre una imagen y otra.

Generalizando esto para todas las clases, nos vamos a estar quedando con los píxeles que mejor caracterizan la figura de cada clase.
"""

grupo_por_clase = data_filtrada_1.groupby('label')   # Agrupo por clase.

varianzas_por_clase = grupo_por_clase.var()   # Varianza de cada píxel dentro de cada clase.
# print(varianzas_por_clase.head())


# --------------------------------------------------------------------------------------------------------------------------------------- #
# %% 
"""
A partir de ahora, defino dos clasificaciónes.

Varianza Intra-Clase: ¿Cuánto varía un píxel dentro de una clase?
- Me va a permitir identificar píxeles estables para una clase dada.

Varianza Inter-Clase: ¿Cuánto varía el valor promedio de un píxel entre las diferentes clases?
- Esta varianza me va a permitir encontrar píxeles que separan bien las clases: píxeles donde el valor medio cambia significativamente de 
una clase a otra.

Un buen píxel predictivo es aquel que:
- Tiene baja Varianza Intra-Clase (es estable dentro de cada clase).
- Tiene alta Varianza Inter-Clase (distingue entre clases).

Así que, a partir de ahora, el objetivo va a ser buscar píxeles que cumplan estas dos condiciones (sobre el conjunto de píxeles filtrados
en el paso anterior).
"""

# Necesito el promedio de cada píxel dentro de cada clase.
promedio_pixel_por_clase_1 = grupo_por_clase.mean()

# Para la Varianza Inter-Clase, calculo la varianza al promedio de cada píxel dentro de cada clase.
varianza_entre_clases = promedio_pixel_por_clase_1.var(axis=0)

# Para la Varianza Intra-Clase, calculo el promedio de las varianzas dentro de cada clase.
varianza_intra_clase = varianzas_por_clase.mean(axis=0)

"""
Grafico Histogramas para poder tener la información en forma visual.
A partir de estos gráficos voy a buscar umbrales para luego filtrar píxeles.
"""

plt.figure(figsize=(14, 5))

# Histograma 1: Varianza entre Clases.
plt.subplot(1, 2, 1)
plt.hist(varianza_entre_clases, bins=50, color='skyblue', edgecolor='black')
plt.title("Varianza entre Clases por Píxel")
plt.xlabel("Varianza entre Clases")
plt.ylabel("Cantidad de Píxeles")
plt.grid(True)

# Histograma 2: Varianza Intra-Clase Promedio.
plt.subplot(1, 2, 2)
plt.hist(varianza_intra_clase, bins=50, color='lightcoral', edgecolor='black')
plt.title("Varianza Intra-Clase Promedio por Píxel")
plt.xlabel("Varianza Intra-Clase")
plt.ylabel("Cantidad de Píxeles")
plt.grid(True)

plt.tight_layout()   # Hago un solo gráfico con ambas figuras.
plt.show()


"""
Análisis de Figuras:

Como especificamos antes, buscamos:
    - Gráfico Varianza entre clases por Píxel -> Umbral alto.
    - Gráfico Varianza Intra-Clase Promedio por Píxel -> Umbral bajo.
    - Tener un volumen de datos considerado.

A partir ded estos requisitos, definimos:
    - Umbral Entre Clases -> 4000 (y tomo todos los píxeles posteriores)
    - Umbral Intra Clases -> 4500 (y tomo todos los píxeles anteriores)
"""

umbral_entre_clases:int = 4000 
umbral_intra_clase:int = 4500


"""
Contruyo la condición que van a tener que cumplir los píxeles que quiero capturar.
   - Varianza entre Clases superior a 4000.
   - Varianza Intra-Clase inferior a 4500.
"""

pixeles_utiles = (varianza_entre_clases > umbral_entre_clases) & (varianza_intra_clase < umbral_intra_clase)

# Filtro los píxeles (en este caso, me quedo con el nombre de las columnas).
columnas_utiles = varianza_entre_clases.index[pixeles_utiles]

# Ahora sí, capturo aquellos píxeles que quiero (conservando también la columna 'label' con la clasificación).
columnas_finales = ['label'] + list(columnas_utiles) if 'label' in data_fashion.columns else list(columnas_utiles)
data_filtrado_final = data_fashion[columnas_finales]

# Lo paso a CSV para poder tener un DataSet para entrenar los modelos.
# data_filtrado_final.to_csv("Limpieza_General.csv")


# Fin.