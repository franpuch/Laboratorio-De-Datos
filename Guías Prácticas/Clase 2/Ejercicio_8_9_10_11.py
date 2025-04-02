# Ejercicios Clase 2. 
# Ejercicio 8, 9, 10 y 11. 

import pandas as pd 

#* Armo DataSets con ambos archivos.

# Pero primero una cosa importante.
# Ví que luego debo mergear ambos Datasets. Pero hay un problema, los nombres de las 
# columnas son distintas en ambos DataSets. Así que, en el momento de crear el DataFrame, le
# voy a pasar nuevos nombres para cada una de las columnas. De forma que luego me sea mas sensillo
# identificar las columnas que voy a necesitar, porque no voy a utilizar todas (y facilitar el
# merge).

# OBS -> Las columnas con nombre 'Null' son columnas con datos que no me interesan, y que luego 
# (seguramente) terminaré limpiando (para trabajar con DataSets mas ligeros).

columnas_parques:list[str] = ["Null 1", "Null 2", "ID Árbol", "Altura", "Diametro", "Inclinación", "ID Especie",
                              "Null 3", "Nombre Científico", "Null 4", "Parque", "Ubicación", "Null 5",
                              "Nombre Genérico", "Origen", "Null 6", "Null 7"]

lectura_parques:pd.DataFrame = pd.read_csv("/home/fran-puch/Documentos/Documentos Francisco/Summer Code/Labo de Datos /Ejercicios Clase 2/Datos_Parques.csv", 
                                      names=columnas_parques, 
                                      skiprows=1) 

columnas_vereda:list[str] = ["Null 1", "Null 2", "Nro Registro", "Null 3", "Comuna", "Null 4", "Null 5", 
                             "Null 6", "Null 7", "Dirección", "Null 8", "Nombre Científico", "Ancho Vereda",
                             "Null 9", "Null 10", "Nivel Plantera", "Diametro", "Altura"] 

lectura_veredas = pd.read_csv("/home/fran-puch/Documentos/Documentos Francisco/Summer Code/Labo de Datos /Ejercicios Clase 2/Datos_Veredas_2017_2018.csv", 
                         names=columnas_vereda, 
                         skiprows=1)


#* Armo un nuevo DataFrame de 'df_veredas', que contenga solamente las columnas de: 
# Nombre Científico, Ancho Vereda, Diametro, Altura.

veredas_elegidas:list[str] = ["Nombre Científico", "Ancho Vereda", "Diametro", "Altura"]
df_vereda:pd.DataFrame = lectura_veredas[veredas_elegidas] 


#* Armo dos DataFrame (uno para las veredas y otro para los parques) para las 'tipas' (supongo son las "Tipuana tipu"), 
#* usando las columnas 'Diametro' y 'Altura'.

df_tipas_veredas:pd.DataFrame = df_vereda.loc[df_vereda["Nombre Científico"] == "Tipuana tipu", ["Diametro", "Altura"]].copy()
df_tipas_parques:pd.DataFrame = lectura_parques.loc[lectura_parques["Nombre Científico"] == "Tipuana Tipu", ["Diametro", "Altura"]].copy()

# Le hice '.copy()' para no quedar pegado al DataFrame original (y modificarlo accidentalmente).


#* A cada DataFrame le añado una columna llamada 'Ambiente', la cual dice 'Parque' y 'Vereda' respectivamente.

df_tipas_veredas["Ambiente"] = "Vereda"
df_tipas_parques["Ambiente"] = "Parque"


#* Concateno los DataFrames en uno solo.

df_final_tipas:pd.DataFrame = pd.concat([df_tipas_parques, df_tipas_veredas], ignore_index=True) 


#* Ahora, de la misma forma que arriba, armo DataFrames (con la misma información) para las especies
#* "Tilia x moltkei" y "Jacaranda mimosifolia".

df_tilia_veredas:pd.DataFrame = df_vereda.loc[df_vereda["Nombre Científico"] == "Tilia x moltkei", ["Diametro", "Altura"]].copy() 
df_tilia_parques:pd.DataFrame = lectura_parques.loc[lectura_parques["Nombre Científico"] == "Tilia viridis subsp. x moltkei", ["Diametro", "Altura"]].copy()

#! En 'Parques': "Tilia x moltkei" -> "Tilia viridis subsp. x moltkei"

df_tilia_veredas["Ambiente"] = "Vereda"
df_tilia_parques["Ambiente"] = "Parque"

df_final_tilia:pd.DataFrame = pd.concat([df_tilia_parques, df_tilia_veredas], ignore_index=True) 


df_jacaranda_veredas:pd.DataFrame = df_vereda.loc[df_vereda["Nombre Científico"] == "Jacaranda mimosifolia", ["Diametro", "Altura"]].copy() 
df_jacaranda_parques:pd.DataFrame = lectura_parques.loc[lectura_parques["Nombre Científico"] == "Jacarandá mimosifolia", ["Diametro", "Altura"]].copy() 

#! En 'Parques': "Jacaranda mimosifolia" -> "Jacarandá mimosifolia"

df_jacaranda_veredas["Ambiente"] = "Vereda"
df_jacaranda_parques["Ambiente"] = "Parque"

df_final_jacaranda:pd.DataFrame = pd.concat([df_jacaranda_parques, df_jacaranda_veredas], ignore_index=True) 


#* Para el análisis de diferencias, voy a calcular el promedio de "Altura" y "Diametro" para comparar la diferencia entre 
#* aquellos ejemplares plantados en Parques y aquellos ejemplares plantados en Veredas.

mean_altura_tipas_veredas:float = df_final_tipas.loc[df_final_tipas["Ambiente"] == "Vereda", "Altura"].mean() 
mean_altura_tipas_parques:float = df_final_tipas.loc[df_final_tipas["Ambiente"] == "Parque", "Altura"].mean() 

mean_diametro_tipas_veredas:float = df_final_tipas.loc[df_final_tipas["Ambiente"] == "Vereda", "Diametro"].mean() 
mean_diametro_tipas_parques:float = df_final_tipas.loc[df_final_tipas["Ambiente"] == "Parque", "Diametro"].mean() 

mean_altura_tilia_veredas:float = df_final_tilia.loc[df_final_tilia["Ambiente"] == "Vereda", "Altura"].mean() 
mean_altura_tilia_parques:float = df_final_tilia.loc[df_final_tilia["Ambiente"] == "Parque", "Altura"].mean()

mean_diametro_tilia_veredas:float = df_final_tilia.loc[df_final_tilia["Ambiente"] == "Vereda", "Diametro"].mean()
mean_diametro_tilia_parques:float = df_final_tilia.loc[df_final_tilia["Ambiente"] == "Parque", "Diametro"].mean()

mean_altura_jacaranda_veredas:float = df_final_jacaranda.loc[df_final_jacaranda["Ambiente"] == "Vereda", "Altura"].mean()
mean_altura_jacaranda_parques:float = df_final_jacaranda.loc[df_final_jacaranda["Ambiente"] == "Parque", "Altura"].mean() 

mean_diametro_jacaranda_veredas:float = df_final_jacaranda.loc[df_final_jacaranda["Ambiente"] == "Vereda", "Diametro"].mean() 
mean_diametro_jacaranda_parques:float = df_final_jacaranda.loc[df_final_jacaranda["Ambiente"] == "Parque", "Diametro"].mean() 


# Banco de Pruebas ------------------------------------------------------------------------------------------ #

# print(lectura_parques.head()) 
# print(df_vereda.head())  

# print(df_vereda.head()) 

# print(df_tipas_veredas.head(10))
# print(df_tipas_parques.head(10)) 

# print(df_final_tipas.head(10))
# print(df_final_tipas.tail(10)) 

# print(df_tilia_veredas.head(10))
# print(df_tilia_parques.head(10)) 

# print(df_final_tilia.head(10))
# print(df_final_tilia.tail(10)) 

# print(df_jacaranda_parques.head(10))
# print(df_jacaranda_veredas.head(10)) 

# print(df_final_jacaranda.head(10))
# print(df_final_jacaranda.tail(10)) 

# print("Promedio Altura - Tipas Parques: ", mean_altura_tipas_parques)
# print("Promedio Altura - Tipas Veredas: ", mean_altura_tipas_veredas) 

# print("Promedio Diametro - Tipas Parques: ", mean_diametro_tipas_parques) 
# print("Promedio Diametro - Tipas Veredas: ", mean_diametro_tipas_veredas) 

# print("Promedio Altura - Tilia Parques: ", mean_altura_tilia_parques) 
# print("Promedio Altura - Tilia Veredas: ", mean_altura_tilia_veredas) 

# print("Promedio Diametro - Tilia Parques: ", mean_diametro_tilia_parques)
# print("Promedio Diametro - Tilia Veredas: ", mean_diametro_tilia_veredas) 

# print("Promedio Altura - Jacaranda Veredas: ", mean_altura_jacaranda_veredas) 
# print("Promedio Altura - Jacaranda Parques: ", mean_altura_jacaranda_parques) 

# print("Promedio Diametro - Jacaranda Parques: ", mean_diametro_jacaranda_parques)
# print("Promedio Diametro - Jacaranda Veredas: ", mean_diametro_jacaranda_veredas)


# Consultas ------------------------------------------------------------------------------------------------- #

#? En el DataFrame 'df_tipas_parques' noté que hay al menos una (desconozco si hay más) fila cuya columna
#? es un 'NaN'. Fui al DataSet original a buscar esa columna en específico, y sí tiene valores numéricos.
#? Además, intenté filtrar todas las filas que tengan 'NaN' pero no encontré la forma de hacerlo andar.
#? No sé como decirle que busque 'NaN' porque no se si 'NaN' es un string o qué "tipo de datos" es... 

# Fin. 