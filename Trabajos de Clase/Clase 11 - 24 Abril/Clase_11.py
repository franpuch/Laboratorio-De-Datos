# Clase 11 - 24 Abril.

import pandas as pd

df_dengue_zika:pd.DataFrame = pd.read_csv("datos_dengue-sika.csv") 
print(df_dengue_zika.loc) 

'''
#* Consigna Diapo 18.

- Estandarizar el 'Null'.

- Mergear los que pertenecen al mismo grupo etario (y que comparten todo los demás atributos).
    - Re-organizar los grupos etarios (unir grupos que estén incluidos en otros).
    - Esto es parte de las suposiciones/decisiones que tomo a la hora de analizar.
      Debo documentar siempre esto, forma parte de mi análisis particular. 

- Cambiar el nombre de la tabla (sólo hay casos de Dengue).

- Corregir las columnas que se swapearon en cierto punto.

- Tomar alguna decisión (y documentar) sobre qué hacer con los registros que aparecen do veces
(pero con distinta cantidad de casos reportados).

#* Comentarios: 
- Medio que uno modifica los datos en función de la pregunta que queres responder. 
''' 

''' 
#* Consigna Diapo 22. 

- Los que hacen la recolección son bobos. 
    - Que la persona que se encarga de recopilar informacion no conoce del tema y por ende, no sabe que informacion 
      recopilar. 

- No es claro el formato para cada entrada (del medio de recolección). 

- Que la especificación sobre qué se quiere recolectar sea clara (corte Algo II). 
'''

'''
#* Consigna Diapo 45.

Atributo a Analizar -> Consistencia.

- Goal -> Revisar si la 'cantidad de casos' con respecto al 'grupo etario' es consistente con la semana epidemiologica. 
- Question -> Para una misma semana (y misma provincia y depto) ¿hay grupos etarios iguales con distinta cantidad?  
- Metrics -> (cantidad de grupos etarios presentes en el dataset por semana epidemiologica)
             ------------------------------------------------------------------------------
                     (cantidad de grupos etarios establecidos de una provincia)

Las sumas todas y las comparas con la cantidad total de semanas epidemiológicas. Si te da mayor, tener información repetida, si te
da igual, todo bien; si te da menos, quiere decir que 
'''
