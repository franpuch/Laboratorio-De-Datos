# Laboratorio de Datos - TP 1. 
'''
Integrantes -> Dorogov Cristina 
            -> Pucciarelli Francisco Lautaro 
            -> Salto Julian 
               
Limpieza y Formateo de DataSet -> Establecimientos Educativos.
'''

'''
Si aún no leyó el 'ReadMe', por favor leerlo.
'''

import pandas as pd 
import duckdb as dk
from pathlib import Path

'''
Preparación de los Path a los diferentes archivos y carpeta de destino.
'''

base_path = Path(__file__).resolve().parent        # Obtener la ruta base del script actual.
originales_path = base_path / 'TablasOriginales'   # Ruta a la carpeta donde se encuentran los DataSets originales.
modelo_path = base_path / 'TablasModelo'           # Ruta a la carpeta donde se van a guardar los DataSets limpios.
modelo_path.mkdir(exist_ok=True)                   # Si no existe la carpeta de salida, crearla.


# ------------------------------------------------------------------------------------------------------------------------------- #

'''
Lectura del DataFrame original.
Excluyo las primeras 5 filas, que tienen el rótulo (dedicadas al título y otros datos propios del Dataset).
La columna 'Código de localidad' quiero que la lea originalmente como 'string', porque luego quiero trabajar esa 
columna en forma particular: hay valores que empiezan en cero, Pandas los lee como 'int' y elimina estos ceros; pero luego los 
necesito (en los ultimos pasos toma sentido).
'''

establecimientos_educativos = pd.read_excel(originales_path / 'Padron_Oficial_Establecimientos_Educativos_2022.xlsx', 
                                            skiprows=6,
                                            dtype={'Código de localidad': str})


'''
ACLARACIÓN IMPORTANTE.
Todas las lineas con la instrucción 'print()' las dejo comentadas, porque es algo intermedio que usé para ver 
si funcionaba bien (lo que iba haciendo).
'''


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

columnas_categoricas:list[str] = ["Nivel inicial - Jardín maternal",
                                  "Nivel inicial - Jardín de infantes",
                                  "Primario",
                                  "Secundario",
                                  "Secundario - INET",
                                  "SNU",
                                  "SNU - INET"]

establecimientos_comunes[columnas_categoricas] = establecimientos_comunes[columnas_categoricas].replace(r'^\s*$', pd.NA, regex=True)
'''
Ejecutando el código, en las dos líneas siguientes me saltó un error porque muchas columnas tienen espacios vacíos o 
strings vacíos. Con las líneas de abajo busco reemplazar esas columnas por 0, pero primero las transformo a 'Nan' de pandas. 
Las rastreo usando una expresión regular.
'''

establecimientos_comunes[columnas_categoricas] = establecimientos_comunes[columnas_categoricas].fillna(0)
'''
El 'fillna()' creo que convierte todo a 'floats'. Me interesa que todo sea 'int', para evitar posibles problemas
luego (uno nunca sabe... a veces esos detalles te hacen perder toda una tarde buscando ese error pavo). Así que, 
por las dudas, lo typeo de nuevo.
'''
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

'''
Cambio los nombres de las columnas.
'''

establecimientos_comunes.columns = ["id_establecimiento",
                                    "jardin_maternal",
                                    "jardin_infantes",
                                    "primario",
                                    "secundario",
                                    "terciario"]


'''
Los demás DataFrames (de los otros tipos de establecimientos educativos) los dejo así como están, porque creemos no los 
vamos a usar. Si llegamos a necesitarlos, les hago un tratamiento parecido; pero por ahora, no.
'''


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Para poder relacional este DataSet con los demás (a través de consultas SQL y demás), necesito que la columna 'id_localidad' 
tenga los primeros 5 dígitos del número que aparece. 
Observamos que los primeros 5 dígitos corresponden al id del departamento. Como cada departamento tiene sus propias localidades, 
los próximos digitos diferencian las localidades. Pero a nosotros nos basta con los departamentos.
Aquellos valores que empiezan con cero, voy a eliminar ese primer cero y luego tomar cinco dígitos a partir de allí.
'''

establecimientos_educativos_clean['id_localidad'] = establecimientos_educativos_clean['id_localidad'].str[:5].astype(int)
'''
Esta línea, a cada elemento de la columna 'id_localidad', lo transforma a string, toma 5 caracteres y lo vuelve a parsear a 
'int' (eliminando ceros que puedan quedar por delante). Los únicos valores que tienen ceros delante son los correspondientes a 
las provincias de Buenos Aires y los correspondientes a CABA. Pero, en el caso de los de Buenos Aires, en el DataSet de Bibliotecas
Populares tienen también 4 dígitos; y los de CABA por ahora no importan (les voy a hacer otro tratamiento después).
'''


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Hay un último tema a solucionar. En el DataSet de Bibliotecas Populares, aquellas bibliotecas que pertenecen a la Ciudad Autónoma
de Buenos Aires no están clasificadas por departamento. Es decir, tanto su localidad (provincia) como su departamento son 'Ciudad 
Autónoma de Buenos Aires'. Y en 'id_departamento' tienen el id de la Ciudad Autónoma de Buenos Aires (como provincia, que es 
'02').
Por lo tanto, vamos a tener que trabajar 'Ciudad Autónoma de Buenos Aires' sin la división en departamentos. Por lo tanto, todos
los Establecimientos Educativos que pertenecen a la 'Ciudad de Buenos Aires' voy a ponerles como 'id_departamento' el código de 
la provincia; para luego poder machear establecimientos educativos con bibliotecas populares que pertenecen a CABA.
Es una lástima, pero bueno... los datos son los datos y nos obligar a trabajrlos así (para poder mantener un orden y más coherencia
en el filtrado y limpieza de datos).
'''

establecimientos_educativos_clean.loc[establecimientos_educativos_clean['nombre_localidad'] == 'CIUDAD DE BUENOS AIRES', 'id_localidad'] = 2000
'''
El 'id_departamento' que usa el Dataset para identificar a las bibliotecas que pertenecen a la Ciudad de Buenos Aires es 2000.
'''

'''
Ahora cambio el nombre a todas las filas cuyo departamento se corresponde con alguno de CIudad Autónoma de Buenos Aires. 
Ahora todos estos establecimientos pertenece a "CIUDAD DE BUENOS AIRES".
'''

departamentos_caba = ["Comuna 1", "Comuna 2", "Comuna 3", "Comuna 4", "Comuna 5", 
                      "Comuna 6", "Comuna 7", "Comuna 8", "Comuna 9", "Comuna 10", 
                      "Comuna 11", "Comuna 12", "Comuna 13", "Comuna 14", "Comuna 15"]

for i, fila in establecimientos_educativos_clean.iterrows():
    if fila["nombre_departamento"] in departamentos_caba:
        establecimientos_educativos_clean.at[i, "nombre_departamento"] = "CIUDAD DE BUENOS AIRES"
        
        
# ------------------------------------------------------------------------------------------------------------------------------- # 
'''
Siguiendo nuestro Modelo Relacional, en el DataSet correspondiente a los Establecimientos Educativos sólo vamos a mantener la 
columna 'id_establecimiento'. Así que las columnas de 'nombre_provincia', 'nombre_departamento' y 'nombre_localidad' debo 
sacarlas. Pero primero, voy a aprovechar que tengo bastante información para poder armar la otra relación que aparece en 
nuestro DER: 'departamentos'. La construyo con SQL (para aumentar la diversidad de herramientas).
'''

consultaAux = dk.query(''' 
                       SELECT id_localidad AS id_departamento, ANY_VALUE(nombre_departamento) AS nombre_departamento, ANY_VALUE(nombre_provincia) AS nombre_provincia
                       FROM establecimientos_educativos_clean
                       GROUP BY id_departamento
                       ORDER BY id_departamento
                       ''')
departamentos = consultaAux.df() 

'''
Pero hay un último detalle. Hay muchos 'nombre_departamento' que dicen 'CAPITAL', sin el nombre de la provincia no queda claro 
capital de qué provincia se refiere. Para que quede mas explícito y fácil de interpretar, voy a cambiar esos valores y juntar 
'CAPITAL' con 'nombre_provincia' (para que, por ejemplo, en vez de 'CAPITAL' diga 'CATAMARCA CAPITAL').
'''
departamentos.loc[departamentos['nombre_departamento'] == 'CAPITAL', 'nombre_departamento'] = departamentos['nombre_provincia'].str.upper() + ' CAPITAL'

'''
Ahora sí, termino de acomodar 'establecimientos_educativos_clean'
'''
establecimientos_educativos_clean = establecimientos_educativos_clean.drop(columns=['nombre_provincia','nombre_departamento','nombre_localidad'])
establecimientos_educativos_clean.columns = ["id_establecimiento",
                                             "nombre_establecimiento",
                                             "id_departamento",
                                             "sector",
                                             "ambito"]


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Finalmente, paso todos los DataFrames (que vamos a usar) a archivos csv.
'''

establecimientos_educativos_clean.to_csv(modelo_path / 'establecimientos_educativos.csv', index=False)
print("Archivo guardado como 'establecimientos_educativos.csv', en la carpeta 'TablasModelo'")

establecimientos_comunes.to_csv(modelo_path / 'establecimientos_educativos_comunes.csv', index=False)
print("Archivo guardado como 'establecimientos_educativos_comunes.csv', en la carpeta 'TablasModelo'")

departamentos.to_csv(modelo_path / 'departamentos.csv', index=False)
print("Archivo guardado como 'departamentos.csv', en la carpeta 'TablasModelo'")


# Fin del archivo.
# Saludos.
