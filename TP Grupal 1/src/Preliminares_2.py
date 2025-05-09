# Laboratorio de Datos - TP 1.
# Trabajos Preliminares 2 - Limpieza y Formateo de DataSet -> Establecimientos Educativos.

import pandas as pd 
import os 

''' LEER ANTES DE EJECUTAR. 
Por favor, en la línea 19 completar con la ruta (path) donde se encuentre el archivo correspondiente a el Dataset original de 
Establecimientos Educativos.

Este script crea una carpeta con dos archivos CSV, correspondientes a la limpieza de datos hecha sobre ese DataSet.
'''

'''
Lectura del DataFrame original.
Excluyo las primeras 5 filas (dedicadas al título y otros datos propios del Dataset).
'''

establecimientos_educativos = pd.read_excel("", skiprows=6)


# ------------------------------------------------------------------------------------------------------------------------------- # 
'''
Me molestan mucho esas columnas categóricas agrupadas bajo "Modalidad". 
Quiero eliminarlas todas y dejar su información en una sola columna llamada "Modalidad".
'''

modalidades:list[str] = ['Común', 'Especial', 'Adultos', 'Artística', 'Hospitalaria', 'Intercultural', 'Encierro']
establecimientos_educativos['Modalidad'] = establecimientos_educativos[modalidades].apply(lambda row: ', '.join([col for col in modalidades if row[col] == 1]), axis=1) 
# print(establecimientos_educativos['Modalidad']) 

'''
Elimino todas las columnas que simplifiqué.
'''

establecimientos_educativos.drop(columns=modalidades, inplace=True) 


# ------------------------------------------------------------------------------------------------------------------------------- # 
'''
Para las sub-categorías (dentro de cada modalidad específica), me gustaría tener esa información en DataFrames separados. 
Para cada modalidad, voy a crear un DataFrame con las columnas 'Cueanexo' (clave de identificación de los distintos establecimientos) 
y las columnas categóricas de la sub-catgoría a la que pertenecen. 
Todo esto con el objetivo de modularizar la información y alivianar el DataSet principal.
'''

establecimientos_comunes = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Común"][["Cueanexo", 
                                                                                                             "Nivel inicial - Jardín maternal", 
                                                                                                             "Nivel inicial - Jardín de infantes", 
                                                                                                             "Primario", 
                                                                                                             "Secundario", 
                                                                                                             "Secundario - INET", 
                                                                                                             "SNU", 
                                                                                                             "SNU - INET"]] 
# print(establecimientos_comunes) 
# print(establecimientos_comunes.columns) 

establecimientos_especiales = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Especial"][["Cueanexo", 
                                                                                                                   "Nivel inicial - Educación temprana", 
                                                                                                                   "Nivel inicial - Jardín de infantes", 
                                                                                                                   "Primario", 
                                                                                                                   "Secundario", 
                                                                                                                   "Integración a la modalidad común/ adultos"]]
# print(establecimientos_especiales) 
# print(establecimientos_especiales.columns) 

establecimientos_adultos = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Adultos"][["Cueanexo", 
                                                                                                               "Primario", 
                                                                                                               "Secundario", 
                                                                                                               "Alfabetización", 
                                                                                                               "Formación Profesional", 
                                                                                                               "Formación Profesional - INET"]]
# print(establecimientos_adultos) 
# print(establecimientos_adultos.columns)

establecimientos_artisticas = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Artística"][["Cueanexo", 
                                                                                                                    "Secundario", 
                                                                                                                    "SNU", 
                                                                                                                    "Talleres"]]
# print(establecimientos_artisticas) 
# print(establecimientos_artisticas.columns)

establecimientos_hospitalarias = establecimientos_educativos[establecimientos_educativos["Modalidad"] == "Hospitalaria"][["Cueanexo", 
                                                                                                                          "Inicial",
                                                                                                                          "Primario", 
                                                                                                                          "Secundario"]]
# print(establecimientos_hospitalarias)
# print(establecimientos_hospitalarias.columns)

'''
Es verdad que solamente vamos a trabajar con los Establecimientos Educativos de Modalidad Común, pero por las dudas tengo esta
informacion también limpia y disponible. 

La columna llamada "Servicios Complementarios" no la vamos a tomar en cuenta para nuestro análisis. Luego la excluyo.
'''

# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Ahora armo un DataFrame aparte que contenga la información que vamos a utilizar (según el DER planteado) de cada una de los
Establecimientos Educativos.
'''

atributos_de_interes_1:list[str] = ["Cueanexo",
                                    "Nombre", 
                                    "Jurisdicción", 
                                    "Código de localidad", 
                                    "Localidad", 
                                    "Departamento",
                                    "Sector", 
                                    "Ámbito"]

establecimientos_educativos_clean = establecimientos_educativos[atributos_de_interes_1]
establecimientos_educativos_clean.columns = ["id_establecimiento",
                                             "nombre",
                                             "nombre_provincia",
                                             "id_localidad",
                                             "nombre_localidad",
                                             "nombre_departamento",
                                             "sector",
                                             "ambito"]


'''
La información de las que llamo "columnas categóricas" lo voy a guardar aparte.
Lo voy a hacer sólo con la Modalidad Común (que es la que vamos a usar, a priori). 
Pero antes, las columnas con valores 'vacíos' (que son muchas) quiero que tengan cero en vez de "vacío". Sobre todo para prevenir 
problemas con "Nulls" cuando vayamos a hacer consultas SQL (y para que quede más prolijo).
'''

columnas_categoricas = ["Nivel inicial - Jardín maternal",
                        "Nivel inicial - Jardín de infantes",
                        "Primario",
                        "Secundario",
                        "Secundario - INET",
                        "SNU",
                        "SNU - INET"]

establecimientos_comunes[columnas_categoricas] = establecimientos_comunes[columnas_categoricas].replace(r'^\s*$', pd.NA, regex=True)
# Ejecutando el código, en las dos líneas siguientes me saltó un error porque muchas columnas tienen espacios vacíos o 
# strings vacíos. Con las líneas de abajo busco reemplazar esas columnas por 0, pero primero las transformo a 'Nan' de pandas. 
# las rastreo usando una expresión regular.

establecimientos_comunes[columnas_categoricas] = establecimientos_comunes[columnas_categoricas].fillna(0)
# El 'fillna()' creo que convierte todo a 'floats'. Me interesa que todo sea 'int', para evitar posibles problemas
# luego (uno nunca sabe... a veces esos detalles te hacen perder toda una tarde buscando ese eror pavo). Así que, 
# por las dudas, lo typeo de nuevo.
establecimientos_comunes[columnas_categoricas] = establecimientos_comunes[columnas_categoricas].astype(int) 

'''
Como especificamos en nuestro DER, las columnas 'Secundario' y 'Secundario - INET' las vamos a centralizar en una sola columna 
llamada 'Secundario'. Esto porque no nos interesa la sub-categoría 'INET', sólo nos interesa que sea modalidad Secundario.
Ahora, para ser prolijo, no voy a crear una nueva columna sino voy a modificar la columna "Secundario" (porque no me interesa 
preservar exactamente la información que tenía).
'''
establecimientos_comunes["Secundario"] = ((establecimientos_comunes["Secundario"] == 1) | (establecimientos_comunes["Secundario - INET"] == 1)).astype(int)

'''
Hago lo mismo que antes, pero ahora combino 'SNU' y 'SNU - INET' en la columna 'Terciario'.
Luego, elimino las columnas que combiné.
'''
establecimientos_comunes["Terciario"] = ((establecimientos_comunes['SNU'] == 1) | (establecimientos_comunes['SNU - INET'] == 1)).astype(int) 
establecimientos_comunes = establecimientos_comunes.drop(columns=["Secundario - INET", "SNU", "SNU - INET"]) 

# Cambio los nombres de las columnas.
establecimientos_comunes.columns = ["id_establecimiento",
                                    "nivel inicial - jardín maternal",
                                    "nivel inicial - jardín de infantes",
                                    "primario",
                                    "secundario",
                                    "terciario"]

'''
Los demás DataFrames (de los otros tipos de establecimientos educativos) los dejo así como están, porque creemos no los 
vamos a usar. Si llegamos a necesitarlos, les hago un tratamiento parecido; pero por ahora, no.
'''


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Finalmente, paso todos los DataFrames (que vamos a usar) a archivos csv.
Voy a utilizar la librería 'os' para crear una carpeta donde almacenar esos archivos.
'''

carpeta_output = "DataSets Limpios"
os.makedirs(carpeta_output, exist_ok=True) 

ruta_csv_1 = os.path.join(carpeta_output, "establecimientos_educativos.csv") 
establecimientos_educativos_clean.to_csv(ruta_csv_1, index=False, encoding='utf-8')

ruta_csv_2 = os.path.join(carpeta_output, "establecimientos_educativos_comunes.csv")
establecimientos_comunes.to_csv(ruta_csv_2, index=False, encoding='utf-8')


# Fin. 

