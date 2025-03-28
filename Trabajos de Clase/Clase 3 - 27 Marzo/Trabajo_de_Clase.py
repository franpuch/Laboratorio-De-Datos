# Archivo de Trabajo  
# Clase 3 -27 Marzo. 

import pandas as pd 

#* Actividad 1 ----------------------------------------------------------------------------------------------------------- # 

df_act_1:pd.DataFrame = pd.read_csv("/home/Estudiante/Escritorio/Labo de Datos /Clase_3_Actividad_1_Datos.csv") 
print(df_act_1.head(15)) 

'''
Conclusiones:
- Muchas filas no tiene "ubicacion". 
- Las columnas no siguen un orden lógico. 
- Hay casos de "latitud" y "longitud" repetidas con '000'. 
- La columna "ubicacion" no es precisa en algunos casos (Ej: 'Plaza' en la fila 10... ¿qué plaza pa'?). 
- El "id_departamento" falta en algunas filas (Ej: línea 83). 
'''

print(df_act_1.loc[df_act_1["ubicacion"] == "Estacion Gral Lavalle" ,:] )
print(df_act_1.loc[df_act_1["municipio_id"] == "COR067" ,:] )
print(df_act_1.loc[df_act_1["ubicacion"] == "Estacion Gral lavalle" ,:])
print(df_act_1.loc[df_act_1[""] == "" ,:] )

#* Actividad 2 ----------------------------------------------------------------------------------------------------------- # 

'''
Subrayamos la importancia de especificar todo lo necesario para obtener un DataSet prolijo, no ambigüo y fácil de 
chambear. La prioridad es no tener que hacer mucho laburo al procesar los datos (eso lo logramos haciendo una recolección
específica y controlada en todas sus opciones).

Descripción de las columnas que consideramos necesarias:
- turno_alumno -> Mañana / Tarde / Noche 
- transporte -> Tren / Colectivo / Vehículo Propio / Pie 
- duracion_viaje_en_ese_transporte -> cantidad total en minutos 

Si te tomás varios transportes, haces una entrada para cada vehículo en particular.
'''

# Grafico los resultados de la Encuenta de Transportes.
df_act_2:pd.DataFrame = pd.read_csv("/home/Estudiante/Escritorio/Labo de Datos /Clase_3_Actividad_2_EncuestaDeMovilidadRespuestas.csv") 

#! Pendiente -> Graficar. 
# Ya fue, es hacer un simple gráfico de barras para comparar (de forma visual) los resultados. Lo dejo así...


#* Fin.