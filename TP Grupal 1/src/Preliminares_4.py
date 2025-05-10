# Laboratorio de Datos - TP 1.
# Trabajos Preliminares 4 - Limpieza y Formateo de DataSet -> Nivel Educativo por Departamento.

import pandas as pd 

'''
Lectura del DataFrame original.
Le digo que lea a partir de la fila 2, ya que el fila 1 tiene columnas que no quiero que tome como nombre (de las columnas del 
DataFrame con el que voy a trabajar).
'''

nivel_educativo_original = pd.read_excel("C:/Users/franp/OneDrive/Documentos/Pendientes/TP Grupal 1/DataSets_Originales/Nivel_Educativo_por_Departamento_2022.xlsx", 
                                         header=2)

# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Voy a generar un Dataframe con la información que necesito.
El Dataset original está dividido en Sub-Tablas consecutivas. Eso es un problema, ya que parsear a un DataFrame que me de la 
información (de todas las filas) en columnas no es directo. 
Mi idea es ir recorriendo todas las filas, e ir completando el nuevo DataFrame con los datos de las filas que necesito. Sé de antemano
cuáles son las columnas que quiero armar, y sé cuáles son los datos de cada sub-tabla que van en cada columna.
'''

# Defino el mapeo de las distintas "filas etiqueta" (de cada sub-tabla) con la columna que voy a querer que machee.
niveles = {"Jardín maternal, guardería, centro de cuidado, salas de 0 a 3": "nivel_inicial_maternal",
           "Sala de 4 o 5 (jardín de infantes o preescolar)": "nivel_inicial_infante",
           "Primario": "nivel_primario",
           "Secundario": "nivel_secundario",
           "Terciario no universitario": "nivel_terciario",
           "Universitario de grado": "nivel_universitario",
           "Posgrado (especialización, maestría o doctorado)": "nivel_posgrado",
           "No Aplica": "fuera_del_sist_educativo"}

# Esto hay que comentarlo para que sea más claro.
data = []
current_area = None
current_row = {}

# Procesar el DataFrame original por bloques.
# Esto también hay que comentarlo un poco mejor (para, de paso entenderlo bien).
for _, row in nivel_educativo_original.iterrows():
    primera_col = str(row[nivel_educativo_original.columns[0]]).strip()

    if primera_col.startswith("AREA #"):
        if current_area and current_row:
            data.append(current_row)
        current_area = primera_col.replace("AREA #", "").strip()
        current_row = {"id_departamento": current_area}
    
    elif primera_col in niveles:
        col_destino = niveles[primera_col]
        current_row[col_destino] = row["Casos"]

# Agregar último departamento procesado.
if current_row:
    data.append(current_row)

# Crear DataFrame final y guardar.
df_resultado_1 = pd.DataFrame(data).fillna(0)

# Mostrar (para ver si quedó lo que quería)
print(df_resultado_1.head())


'''
Funciona a partir de la segunda sub-tabla, a primera no la vé. Esto se debe a que estoy leyendo el DataSet original desde la 
segunda fila, por lo que no lee la primera fila que tiene el código de área de la primera sub-tabla.
Pero al ser solo 1 la faltante, la agrego a mano.
'''

info_primera_subtabla = {'id_departamento' : '02007', 
                         'nivel_inicial_maternal' : 4170,
                         'nivel_inicial_infante' : 4010, 
                         'nivel_primario' : 18572, 
                         'nivel_secundario' : 16424, 
                         'nivel_terciario' : 7155, 
                         'nivel_universitario' : 21847, 
                         'nivel_posgrado' : 4205} 

df_resultado_2 = pd.DataFrame([info_primera_subtabla])
df_resultado_final = pd.concat([df_resultado_2, df_resultado_1.iloc[1:]],
                               ignore_index=True)

print(df_resultado_final.head()) 


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Quiero saber si realmente sólo es la 1er sub-tabla la que está salteando.
Para ello, voy al DataSet original y cuento las filas que tienen "Area #". La idea es saber cuántos departamento hay en el original 
y compararlo con el DataFrame que construye mi función (junto con la primera fila agregada). 
'''

primera_columna_original = nivel_educativo_original.columns[0]   # La que siempre tiene el "Area # ..."
total_areas = nivel_educativo_original[primera_columna_original].astype(str).str.startswith("AREA #").sum()

print(f"Total de áreas encontradas: {total_areas}") 

cantidad_filas:int = df_resultado_final['id_departamento'].count() 
print(f"Valores distintos de 'id_departamentos' de mi Dataframe: {cantidad_filas}")


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Con todo funcionando, estoy listo para crear el archvio CSV con los datos limpios.
'''

df_resultado_final.to_csv("nivel_educativo_por_departamento.csv", index=False)
print("Archivo guardado como 'nivel_educativo_por_departamento.csv'")


# Fin.
