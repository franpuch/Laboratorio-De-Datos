# Laboratorio de Datos - TP 1.
# Trabajos Preliminares 2 - Limpieza y Formateo de DataSets.

import pandas as pd 

# Lectura de DataFrames originales.
# bibliotecas_populares = pd.read_csv("C:/Users/franp/OneDrive/Documentos/Codes/Labo de Datos - TP 1/DataSets_Originales/Bibliotecas_Populares.csv")
establecimientos_educativos = pd.read_excel("C:/Users/franp/OneDrive/Documentos/Pendientes/Labo de Datos - TP 1/DataSets_Originales/Padron_Oficial_Establecimientos_Educativos_2022.xlsx", skiprows=6)

# ------------------------------------------------------------------------------------------------------------------------------- # 
# Me molestan mucho esas columnas categóricas agrupadas bajo "Modalidad". 
# Quiero eliminarlas todas y dejar su información en una sola columna llamada "Modalidad".

modalidades:list[str] = ['Común', 'Especial', 'Adultos', 'Artística', 'Hospitalaria', 'Intercultural', 'Encierro']
establecimientos_educativos['Modalidad'] = establecimientos_educativos[modalidades].apply(lambda row: ', '.join([col for col in modalidades if row[col] == 1]), axis=1) 
print(establecimientos_educativos['Modalidad']) 

# Elimino todas las columnas que simplifiqué.
establecimientos_educativos.drop(columns=modalidades, inplace=True) 

# ------------------------------------------------------------------------------------------------------------------------------- # 
# Para las sub-categorías (dentro de cada modalidad específica), me gustaría tener esa información en DataFrames separados. 
# Para cada modalidad, voy a crear un DataFrame con las columnas 'Cueanexo' (clave de identificación de los distintos establecimientos) 
# y las columnas categóricas de la sub-catgoría a la que pertenecen. 
# Todo esto con el objetivo de modularizar la información y alivianar el DataSet principal.

establecimientos_comunes = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Común"][["Cueanexo", 
                                                                                                             "Nivel inicial - Jardín maternal", 
                                                                                                             "Nivel inicial - Jardín de infantes", 
                                                                                                             "Primario", 
                                                                                                             "Secundario", 
                                                                                                             "Secundario - INET", 
                                                                                                             "SNU", 
                                                                                                             "SNU - INET"]] 
print(establecimientos_comunes) 

establecimientos_especiales = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Especial"][["Cueanexo", 
                                                                                                                   "Nivel inicial - Educación temprana", 
                                                                                                                   "Nivel inicial - Jardín de infantes", 
                                                                                                                   "Primario", 
                                                                                                                   "Secundario", 
                                                                                                                   "Integración a la modalidad común/ adultos"]]
print(establecimientos_especiales) 

establecimientos_adultos = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Adultos"][["Cueanexo", 
                                                                                                               "Primario", 
                                                                                                               "Secundario", 
                                                                                                               "Alfabetización", 
                                                                                                               "Formación Profesional", 
                                                                                                               "Formación Profesional - INET"]]
print(establecimientos_adultos) 

# Continuar con los que faltan. 
# Luego, en un Dataframe nuevo quedarme con las columnas que tienen toda la información restante (común a todas las escuelas). 


