# -*- coding: utf-8 -*-
"""
Created on Fri May 23 11:46:54 2025

@author: franp
"""

"""
Ejercicios Clase 15.
Trabajo el Archivo por Secciones (Bloques), ya que estoy cansado de que se generen todos los gráficos mamones cada vez que 
pruebo algo en los árboles. SE ME LLENA LA RAM DE GRÁFICOS HERMANO... 
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# %%

"""
Lectura del DataFrame de árboles.
De paso reviso qué tiene y hago algunas modificaciones.
"""

data_trees:pd.DataFrame = pd.read_csv("arboles.csv") 
# print(data_trees.head()) 
# print(len(data_trees))

# Quiero ver el tipo de dato de cada columna (de paso me queda a mano el nombre de las columnas).
# print(data_trees['altura_tot'].dtype)
# print(data_trees['diametro'].dtype)
# print(data_trees['inclinacio'].dtype)
# print(data_trees['nombre_com'].dtype) 

# Le cambio el nombre a las columnas (por otros mas declarativos y cómodos)
nombres_columnas:list[str] = ["Altura", "Diametro", "Inlcinacion", "Especie"]
data_trees.columns = nombres_columnas 
# print(data_trees.head()) 


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %%

"""
Gráfico Histograma 1.
Atributos a Graficar -> 'Altura' y 'Especie'.
"""

nbins = 60 # Tiré varios tamaños y este es el que me permite visualizar mejor la clasificación.

f, s1 = plt.subplots()
plt.suptitle('Histograma de Altura Total', size = 'large')

sns.histplot(data = data_trees, x = 'Altura', hue = 'Especie', bins = nbins, palette = 'viridis', ax = s1)

# Cambiar el nombre del eje X
s1.set_xlabel('Altura Total (m)') 

# Cambiar el nombre del eje Y
s1.set_ylabel('Conteo') 


"""
Gráfico Histograma 2.
Atributos a Graficar -> 'Diametro' y 'Especie'.
"""

nbins = 50 # Tiré varios tamaños y este es el que me permite visualizar mejor la clasificación.

f, s2 = plt.subplots()
plt.suptitle('Histograma de Diametro', size = 'large')

sns.histplot(data = data_trees, x = 'Diametro', hue = 'Especie', bins = nbins, palette = 'tab10', ax = s2)

# Cambiar el nombre del eje X
s2.set_xlabel('Diametro (cm)') 

# Cambiar el nombre del eje Y
s2.set_ylabel('Conteo') 


"""
Gráfico Histograma 3.
Atributos a Graficar -> 'Inclinacion' y 'Especie'.
"""

nbins = 30 # Tiré varios tamaños y este es el que me permite visualizar mejor la clasificación.

f, s3 = plt.subplots()
plt.suptitle('Histograma de Inlcinación', size = 'large')

sns.histplot(data = data_trees, x = 'Inlcinacion', hue = 'Especie', bins = nbins, palette = 'Set2', ax = s3)

# Cambiar el nombre del eje X
s3.set_xlabel('Altura Total (metros)') 

# Cambiar el nombre del eje Y
s3.set_ylabel('Conteo') 


'''
Imprimo los gráficos. 
Descubrí que puedo poner 'plt.show()' una sola vez y se generan todos (no es necesario escribir el comando 
luego de cada gráfico). 
'''
print("Prrrmmm Prrrrmmmm PATAPIM")
print("Mostrame esos gráficos paper...")
plt.show()

'''
De hecho, no puse ningún 'plt.show()' y se generaron todos igual... SOSPECHOSO.
Pero bueno, por las dudas al menos una vez lo pongo...
'''


"""
Gráfico Scatterplot 1.
Atributos a Graficar -> Diametro // Altura , con colores por Especie.
"""

f, s4 = plt.subplots(figsize = (10,7))   # Le modifico el tamaño (para que quede mas prolijo) 
plt.suptitle("Relación Diametro // Altura por Especie (colores)", size = "large")

sns.scatterplot(data = data_trees,
                x = "Diametro", 
                y = "Altura",
                hue = "Especie", 
                palette = "Dark2",
                ax = s4,
                s = 70,   # Este parámetro sirve para manejar el tamaño de los puntos.
                alpha = 0.8)   # Este parámetro sirve para manejar la trasparencia de los puntos
                               # (y visualizar mejor si hay superposición de puntos).
                               
# Cambiar el nombre del eje X.
s4.set_xlabel('Diametro (cm)')

# Cambiar el nombre del eje Y.
s4.set_ylabel('Altura (m)') 


"""
Quiero ver si usando escala logarítmica puedo mejorar la visualización del gráfico anterior.
Probemos...
"""

f, s5 = plt.subplots(figsize = (10, 7))   # Le modifico el tamaño (para que quede mas prolijo y la Leyenda no se superponga con el gráfico).
plt.suptitle("Relación Diametro // Altura por Especie (colores)", size = "large")

sns.scatterplot(data = data_trees,
                x = "Diametro", 
                y = "Altura",
                hue = "Especie", 
                palette = "Dark2",
                ax = s5,
                s = 70, 
                alpha = 0.8)   

s5.set_xscale('log') # Aplico escala logarítmica al eje X.
s5.set_yscale('log') # Aplico escala logarítmica al eje Y.
                               
# Cambiar el nombre del eje X.
s5.set_xlabel('Diametro (cm, escala logarítmica)')

# Cambiar el nombre del eje Y.
s5.set_ylabel('Altura (m, escala logarítmica)') 

'''
Bueno... ta raro igual. Sospechoso...
Lo dejo (por las dudas...), pero no cambia mucho.
'''

"""
Ahora sí, terminaron todos los gráficos.
Los genero todos.
"""

plt.show()
print("Ya está jefe, todos los gráficos hechos.")
print("Tum Tum Tum Tum Tum SAHUR") 


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %%

"""
Vamos con el tema de los Árboles...
(...inserte sticker de soldado con recuerdos de Vietnam...)
(El sticker viene por Algo III)
"""

""" 
Primero, voy a partir mi DataFrame en dos: uno para entrenar y otro para evaluar.
En el de entrenamiento voy a poner el 80% del DataFrame original: 7667 filas.
En el de evaluación de performance voy a poner el 20% del DataFrame restante: 1916 filas.
"""
data_training = data_trees.iloc[:7667] 
data_supervition = data_trees.iloc[7668:]
# print(len(data_training))
# print(len(data_supervition))

'''
Esto último que hice no está mal, seguramente funcionará bien.
Sin embargo, 'sklearn' tiene herramientsa para manejar esto en forma automática. Así que voy a manejarlo con eso, de paso voy aprendiendo a utilizar 
la herramienta.
'''


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %%

"""
Ahora sí, empecemos con la forestada...
"""

'''
Primero separo los atributos.
'''

atributos = ["Altura", "Diametro"]   # Atributos que voy a usar para Entrenar.
X = data_trees[atributos] 
Y = data_trees["Especie"]   # Atributo con la clasificación.

'''
Ahora preparo los Sets de Entrenamiento y los Sets de Evaluación.
Importo 'from sklearn.model_selection import train_test_split'. Esta es la clase que me permite obtener las herramientas para armar, en forma 
automática, ambos conjuntos.
'''

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,                # Variables de Clasificación.
    test_size = 0.2, 
    stratify = Y,
    random_state = 42) 

'''
¿Qué hace cada parámetro dentro de este método?

'test_size=0.2'
    - Define el porcentaje de los datos que se usará para el conjunto de prueba.
    - En este caso: 0.2 significa 20% para prueba y 80% para entrenamiento.
    - También puede ser un número entero (cantidad de filas), por ejemplo: 'test_size = 100'.

'stratify = Y'
    - Este parámetro mantiene la misma proporción de clases en los datos de entrenamiento y prueba.
    - Es útil cuando tenés clases desbalanceadas (por ejemplo, muchas filas de una especie y pocas de otra).
    - Sin esto, podría pasar que una especie no aparezca en el conjunto de prueba por error.
    
'random_state = 42'
    - Define una semilla aleatoria que asegura que la división siempre sea la misma cada vez que ejecutes el código.
    - Si no ponés este parámetro, el resultado cambia cada vez que corras el programa (porque el muestreo es aleatorio).
    - Podés usar cualquier número entero (42 es muy usado por convención, justo coincide con mi bondi :) )
'''


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %%

'''
Vamos con el Árbol 1.
'''

modelo_1 = tree.DecisionTreeClassifier(criterion = 'entropy', 
                                       max_depth = 4,
                                       random_state = 42)

modelo_1 = modelo_1.fit(X_train, Y_train) 

'''
Quiero ponerlo a prueba, voy a utilizar los Sets que preparé. 
Quiero obtener la Exactitud del árbol luego de pasarle el Sets de Evaluación. Puedo generar esta infomarción automáticamente.
'''

exactitud:int = modelo_1.score(X_test, Y_test)
print("Exactitud del Modelo 1: ", exactitud) 

'''
También existe una herramienta que me permite tener mas información sobre la performance de mi árbol. 
Importo 'from sklearn.metrics import classification_report' 
'''

test_1 = modelo_1.predict(X_test) 
reporte_1 = classification_report(test_1, Y_test)
print("Reporte de Desempeño - Árbol 1: ") 
print(reporte_1) 

''' 
Análisis de Resultados: 

Primero me especifico qué representa cada variable calculada: 
- precision -> De todas las veces que el modelo predijo una clase, ¿cuántas veces acertó?
- recall -> De todos los verdaderos casos de esa clase, ¿cuántos detectó correctamente?
- f1-score -> Promedio entre 'precision' y 'recall'. Un buen resumen si querés una sola métrica.
- support -> Cantidad real de ejemplos de esa clase en el conjunto de prueba.

Ahora analizo especie por especie.

Ceibo
- precision -> Cuando el modelo predice "Ceibo", acierta un 41% de las veces.
- recall -> El 75% de los verdaderos Ceibos fueron detectados correctamente.
- support -> Había 125 Ceibos reales en los datos de prueba.
El modelo detecta muchos Ceibos (alto recall), pero también se confunde bastante al predecir (baja precision). 

Eucalipto
Excelente rendimiento. Detecta bien los Eucaliptos y rara vez se equivoca al predecirlo.

Jacarandá
- precision -> 87%, muy preciso cuando predice Jacarandá.
- recall -> Detecta solo el 57% de los verdaderos Jacarandás.
El modelo es conservador: sólo predice Jacarandá cuando está bastante seguro, pero se le escapan muchos casos reales (bajo recall).

Pindó
- precision -> 14%, cuando predice Pindó, casi siempre se equivoca.
- recall -> 51%, detecta la mitad de los Pindós reales.
- f1-score -> 21%, muy bajo.
- support -> 57, clase poco representada.
El modelo tiene muchas dificultades para reconocer Pindó. Posiblemente porque hay pocos ejemplos (solo 57).

Conclusión general
- El modelo funciona muy bien con Eucalipto y bastante bien con Jacarandá.
- Tiene dificultades con Ceibo y especialmente con Pindó (que además es una clase minoritaria).
  Esto puede deberse a que:
      - Hay pocos ejemplos de esas clases.
      - Las clases están desbalanceadas.
      - El árbol está sobreajustado a las clases grandes.
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %%

'''
Gráfico del Árbol 1.
'''

plt.figure(figsize=(15, 10))
tree.plot_tree(modelo_1,
               feature_names = X.columns,
               class_names = modelo_1.classes_,
               filled = True,
               rounded = True,
               fontsize = 10)
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %%

'''
Vamos con el Árbol 2.
'''

modelo_2 = tree.DecisionTreeClassifier(criterion = 'gini', max_depth = 4)

modelo_2 = modelo_2.fit(X_train, Y_train)

test_2 = modelo_2.predict(X_test) 
reporte_2 = classification_report(test_2, Y_test)
print("Reporte de Desempeño - Árbol 2: ")
print(reporte_2) 

'''
Análisis de Resultados: 

Tiene básicamente la misma Exactitud que el modelo anterior (que usaba como Medida de Impureza a Entropía).

Analizo especie por especie. 

Ceibo
- precision -> Cuando el modelo predice Ceibo, acierta el 44% de las veces.
- recall -> El 65% de los Ceibos fueron acertados correctamente.
- support -> Teniendo en cuenta el número total de la muestra (1917 árboles), la proporción de Ceibo es baja.
El modelo detecta más de la mitad de los Ceibos, pero se equivoca bastante al predecir (tiene baja precisión).

Eucalipto 
- precision -> El modelo acierta en un 82% al predecir Eucaliptos.
- recall -> El 90% de los Eucaliptos fueron detectados correctamente.
- support -> La cantidad total de ejemplares de Eucalipto (en la muestra) es considerablemente buena.
El modelo tiene un excelente rendimiento a la hora de predecir y detectar Eucaliptos, se equivoca poco.

Jacarandá 
- precision -> El modelo acierta en un 83% de las veces al predecir Jacarandá.
- recall -> Sólo el 57% de los Jacarandá fueron detectados correctamente.
- support -> La cantidad total de ejemplares en la muestra es la más alta de todas. 
(No sé cómo concluir el análisis de esta especie)

Pindó
- precision -> El modelo acierta en un 13% de las veces. Muy bajo.
- recall -> Sólo fueron clasificados correctamente el 48% de los Pindó.
- support -> Además de ser la especie con menor cantidad de ejemplares en la muestra, comparando su cantidad con 
             la cantidad total de ejemplares registrados, no llega a ser ni el 10%
El modelo tiene muchas dificultades para predecir el Pindó. Muy seguramente se debe a que no logra aprender sus características bien 
(no logra caracterizarlo lo suficiente) debido a la poca cantidad de casos que se le otorgan.

Conclusión General: 
- El modelo funciona muy bien con Eucalipto y bastante bien con Jacarandá.
- Tiene dificultades con Ceibo y especialmente con Pindó (que además es una clase minoritaria).
  Esto puede deberse a que:
      - Hay pocos ejemplos de esas clases.
      - Las clases están desbalanceadas.
      - El árbol está sobreajustado a las clases grandes.

Comparandolo con el 'modelo_1', en este caso modificar la medida de impureza no me cambia (en lineas generales) la potencia predictiva del modelo.
Mantiene una performance similar.
'''


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %% 

'''
Gráfico del Árbol 2.
'''

plt.figure(figsize = (15, 10))
tree.plot_tree(modelo_2, 
               feature_names = X.columns,
               class_names = modelo_2.classes_,
               filled = True, 
               rounded = True, 
               fontsize = 10)
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# %% 

'''
Consultas:

- Para calcular la Exactitud (y demás) de cada árbol, utilicé las herramientas propias del Módulo sklearn.
  ¿Puedo hacerlo así? Sino ¿cómo puedo acceder a algún "DataFrame resultado" de las predicciones del árbol (cuando le paso datos para que prediga)?

- ¿Hay alguna forma de elegir la profundidad correcta? Digo, que no sea probando y buscando hacer el grafico de la (Exactitud x Profundidad del Árbol).
  O si no le paso el parámetro 'max_depth' lo hace automático (prueba varios y se queda el mejor).
  
- Mostrar mi análisis de los reportes de los Árboles.
  Cómo puedo explicar esos casos donde la 'precision' da considerablemente buena, pero el 'recall' es bajo (Ej: el Jacarandá en ambos Árboles).
  Es raro que prediga bien, pero en realidad le pegó a un número bajo de casos correctamente.
  
- Pedir ayuda con el gráfico -> En los nodos del final se superpone todo y no se entiende nada jejeje. Y no sé cómo arreglarlo.

'''


# Fin.
