# Laboratorio de Datos - TP 1.
# Trabajos Preliminares 4 - Limpieza y Formateo de DataSet -> Población por Edad por Departamento.

import pandas as pd 
import os 

''' LEER ANTES DE EJECUTAR. 
Por favor, en la línea 20 completar con la ruta (path absoluto) donde se encuentre el archivo correspondiente a el Dataset 
original de 'Cantidad de Población por Departamento por Edad' en formato '.csv'.
También completar en la línea 188 con la ruta (path absoluto) donde en encuentre la carpeta "DataSets Limpios" creada al 
ejecutar el archivo 'Preliminares_2.py' (para que el dataset limpio se almacene en la misma carpeta que los demás).
'''

'''
Lectura del DataFrame original.
Le digo que lea a partir de la fila 13 (que se saltee las primeras 12 filas), ya que esas filas tienen el rótulo del DataSets (datos
como el título, la fecha, etc). No quiero esa información ahora porque me complica el trabajo de limpieza y parseo.
'''

path_archivo = ""
poblacion_por_edad_original = pd.read_excel(path_archivo,
                   skiprows=12,
                   header=None)


'''
ACLARACIÓN IMPORTANTE.
Todas las lineas con la instrucción 'print()' las dejo comentadas, porque es algo intermedio que usé para ver 
si funcionaba bien (lo que iba haciendo).
'''


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Voy a generar un Dataframe con la información que necesito.
El Dataset original está dividido en Sub-Tablas consecutivas. Eso es un problema, ya que parsear a un DataFrame que me de la 
información (de todas las filas) en columnas no es directo. 
Mi idea es ir recorriendo todas las filas, e ir completando el nuevo DataFrame con los datos de las filas que necesito. Sé de antemano
cuáles son las columnas que quiero armar, y sé cuáles son los datos de cada sub-tabla que van en cada columna.
'''


# Quito las filas completamente vacías y ajusto los índices (los reseteo).
poblacion_por_edad_aux = poblacion_por_edad_original.dropna(how='all').reset_index(drop=True)

'''
La idea es armar una lista con todas las filas del nuevo DataFrame (mi DataFrame final).
Luego, voy a armar un nuevo DataFrame a partir de esta lista.
'''
resultados = []

'''
Voy a iterar sobre todas las filas viendo qué hay en la columna dos (la columna 'B' si abro con excel el archvo original).
Depende de lo que me encuentre (un código de Area, la fila correspondiente a una edad en una sub-tabla, o cualuqier otra cosa), 
voy a hacer lo que deba hacer con la información de la columna siguiente (de esa misma fila), que es la columna que tiene: o el 
nombre del departamento, o la cantidad de habitantes de ese departamento de esa edad.
'''

i = 0
while i < len(poblacion_por_edad_aux):
    fila = poblacion_por_edad_aux.iloc[i]
    
    # Identificar inicio de una nueva sub-tabla por "AREA #".
    if isinstance(fila[1], str) and "AREA #" in fila[1]:
        # Extraigo ID y nombre del departamento.
        id_departamento = fila[1].split("AREA #")[-1].strip()
        nombre_departamento = fila[2]
        
        # Avanzar hasta encontrar la fila de encabezado de la sub-tabla ("Edad", "Casos", etc).
        i += 1
        while i < len(poblacion_por_edad_aux) and not (poblacion_por_edad_aux.iloc[i][1] == "Edad"):
            i += 1
        i += 1  # Pasar a la primera fila de datos reales (en este punto encontré el encabezado de la sub-tabla).
        
        # Inicializo los acumuladores.
        jardin_maternal = jardin_infante = primaria = secundaria = terciario = poblacion_total = 0
        
        # Leer los datos de la sub-tabla hasta llegar a la fila "Total".
        while i < len(poblacion_por_edad_aux):
            edad = poblacion_por_edad_aux.iloc[i][1]
            casos = poblacion_por_edad_aux.iloc[i][2]
            
            # Si es "Total", tomar como población total y terminar bloque.
            if isinstance(edad, str) and edad.strip().lower() == "total":
                poblacion_total = casos
                i += 1
                break
            
            # Si la edad es numérica, sumarsela al acumulador correspondiente.
            if pd.api.types.is_number(edad):
                edad = int(edad) # Si no lo parseo como 'int', a veces se vuelve loco y lo interpreta como millones.
                if edad in [0, 1, 2, 3]:
                    jardin_maternal += casos
                elif edad in [4, 5]:
                    jardin_infante += casos
                elif 6 <= edad <= 12:
                    primaria += casos
                elif 13 <= edad <= 18:
                    secundaria += casos
                elif 19 <= edad <= 50:
                    terciario += casos
            i += 1
        
        # Construyo la fila y la guardo en 'resultado'. Uso diccionarios, para poder tener bien explícito cada columna.
        resultados.append({
            "id_departamento": id_departamento,
            "nombre_departamento": nombre_departamento,
            "jardin_maternal": jardin_maternal,
            "jardin_infante": jardin_infante,
            "primaria": primaria,
            "secundaria": secundaria,
            "terciario": terciario,
            "poblacion_total": poblacion_total
        })
    else:
        i += 1  # Avanzar si no es un inicio de sub-tabla.

# Creo el DataFrame final
df_resultado = pd.DataFrame(resultados)

# Reviso a ver qué es lo que cocinó... (o sea, qué es lo que hizo).
# print(df_resultado.head())


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Como hicimos en los demás DataSets, todos los departamentos de Ciudad Autónoma de Buenos Aires vamos a trabajarlos como si fueran 
uno. Por lo tanto, voy a hacer lo siguiente. Primero, modificar 'id_departamento' de todas aquellos cuyo 'nombre_departamento' sean 
'Comuna X'; el nuevo id va a ser 2000 (id de la provincia CIUDAD DE BUENOS AIRES que usamos en los demás DataSets).
'''

df_resultado.loc[df_resultado['nombre_departamento'].str.startswith('Comuna '), 'id_departamento'] = 2000 

'''
Ahora quiero combinar esas filas en una sola, que centralice toda la información de población de Ciudad de Buenos Aires.
'''
# Tomo las filas que tienen id_departamento = 2000.
df_caba = df_resultado[df_resultado['id_departamento'] == 2000]

# Sumo todas las columnas numéricas de esas filas.
df_caba_suma_total = df_caba.drop(columns=['nombre_departamento']).sum(numeric_only=True)

# Creo una nueva fila con los valores calculados (en realidad, le añado las columnas que le faltan).
df_caba_suma_total['id_departamento'] = 2000
df_caba_suma_total['nombre_departamento'] = 'Ciudad de Buenos Aires'

# Reordeno las columnas en el orden original.
columnas_ordenadas = df_resultado.columns
df_caba_final = pd.DataFrame([df_caba_suma_total])[columnas_ordenadas]

# Elimino las filas originales (del DataFrame original) con id_departamento = 2000.
df_resultado = df_resultado[df_resultado['id_departamento'] != 2000]

# Agrego la nueva fila al DataFrame original.
df_resultado = pd.concat([df_resultado, df_caba_final], ignore_index=True) 


'''
Hay una cosa mas por solucionar aquí. Hay varios 'id_departamentos' que empiezan con cero (creo que son todos los 
'id_departamento' correspondientes a Provincia de Buenos Aires). En los otros DataSets, estos ids los dejé con cuatro dígitos
(quité el cero de delante). Aquí voy a hacer lo mismo.
Para ello, creo que parseando toda la columna a 'int' me basta para eliminar los ceros del principio.
'''
df_resultado['id_departamento'] = df_resultado['id_departamento'].astype(int)


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Hay un problema en el DataFrame resultado. La columna 'nombre_departamento' tiene el mismo valor en todos los departamentos que 
corresponden a la capital de una provincia. Es decir, todos los departamento que son capital de una provincia, su valor en la 
columna 'nombre_departamento' es "Capital" (para todos). Teniendo en cuenta que contamos con una tabla aparte donde tenemos 
cada 'id_departamento' asociado al nombre del mismo, para que no sea redundante, voy a sacar la columna 'nombre_departamento' 
del DataFrame donde clasifico la población.
'''

df_resultado = df_resultado.drop(columns=["nombre_departamento"]) 
# print(df_resultado.head())


# ------------------------------------------------------------------------------------------------------------------------------- #

'''
Con todo funcionando, estoy listo para crear el archvio CSV con los datos limpios.

Voy a utilizar la librería 'os' para buscar (crear si no existe) la carpeta donde estoy almacenando los archivos limpios.
'''

carpeta = ""
nombre_archivo_resultado = "nivel_educativo_por_departamento.csv"
ruta_completa_1 = os.path.join(carpeta, nombre_archivo_resultado)

df_resultado.to_csv(ruta_completa_1, index=False)
print("Archivo guardado como 'nivel_educativo_por_departamento.csv'")


# Fin. 
