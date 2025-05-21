# Laboratorio de Datos - TP 1. 
'''
Integrantes -> Dorogov Cristina 
            -> Pucciarelli Francisco Lautaro 
            -> Salto Julian 
               
Verificaciones Preliminares 1 -> Exploración de DataSets Originales y Primer Contacto.
'''

import pandas as pd 
from pathlib import Path 

'''
Preparación de los Path a los diferentes archivos y carpeta de destino.
'''

base_path = Path(__file__).resolve().parent        # Obtener la ruta base del script actual.
originales_path = base_path / 'TablasOriginales'   # Ruta a la carpeta donde se encuentran los DataSets originales.
modelo_path = base_path / 'TablasModelo'           # Ruta a la carpeta donde se encuentran los Dataset limpios.


# ----------------------------------------------------------------------------------------------------------------------------------- #
# Lectura de DataSets originales.
bibliotecas_populares_original = pd.read_csv(originales_path / 'Bibliotecas_Populares.csv')
establecimientos_educativos_original = pd.read_excel(originales_path / 'Padron_Oficial_Establecimientos_Educativos_2022.xlsx', 
                                            skiprows=6)     # Quiero que Pandas ignore las primera 6 filas, que contienen
                                                            # el rótulo del DataSet.
                                                            
# Lectura de DataSets limpios. 
bibliotecas_populares_limpio = pd.read_csv(modelo_path / "bibliotecas_populares.csv")
establecimientos_educativos_limpio = pd.read_csv(modelo_path / "establecimientos_educativos.csv")
departamentos = pd.read_csv(modelo_path / "departamentos.csv")
nivel_educ_dept = pd.read_csv(modelo_path / "nivel_educativo_por_departamento.csv")


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Quiero ver si 'nro_conabip' dentro de 'bibliotecas_populares' es un valor único en cada fila.
El objetivo es ver si podemos usarlo como clave única para identificar a cada biblioteca.
'''

valores_distintos:int = bibliotecas_populares_original['nro_conabip'].nunique() 
print("Valores de 'nro_conabip' distintos: " , valores_distintos) 

cantidad_filas:int = bibliotecas_populares_original['nro_conabip'].count() 
print("Cantidad total de filas de 'bibliotecas_populares': " , cantidad_filas) 

'''
Como la cantidad de filas es igual a la cantidad de valores distintos (de 'nro_conabip'), son únicos 
y puedo usarlos como identificador único. 
'''


# ----------------------------------------------------------------------------------------------------------------------------------- # 
'''
Quiero ver si 'Cueanexo' dentro de 'establecimientos_educativos' es un valor único en cada fila.
El objetivo es ver si podemos usarlo como clave única para identificar a cada establecimiento educativo.
'''

valores_distintos = establecimientos_educativos_original['Cueanexo'].nunique() 
print("Valores de 'Cueanexo' distintos: " , valores_distintos) 

cantidad_filas = establecimientos_educativos_original['Cueanexo'].count() 
print("Cantidad total de filas de 'establecimientos_educativos': " , cantidad_filas) 

'''
Como la cantidad de filas es igual a la cantidad de valores distintos (de 'Cueanexo'), son únicos 
y podemos usarlos como identificador único. 
'''


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Luego del proceso de limpieza de DataSets, quiero ver si me quedaron cantidades coherentes de departamentos en todos los DataSets. 
A qué me refiero... Voy a tomar la cantidad de filas del DataSets 'departamentos' como la cantidad total de departamentos del país
(al menos es la mejor aproximación con los datos que tenemos). Tomo la cantidad de filas ya que este DataSet tiene una fila por cada
departamento distinto. De los DataSets de 'bibliotecas_populares' y 'establecimientos_educativos' voy a contar la cantidad de elementos 
distintos que hay en la columna 'id_departamento'. Esas cantidades deberían ser menor/igual a la cantidad de departamentos obtenida 
anterioremente. "Menor/igual" ya que puede suceder que exitan departamentos son establecimientos educativos o bibliotecas populares. 
Por eso, con que sea menor, me basta.
'''

cantidad_total_departamentos = departamentos["id_departamento"].count() 
print("Cantidad Total de Departamentos: ", cantidad_total_departamentos) 

cantidad_deptos_bibliotecas = bibliotecas_populares_limpio["id_departamento"].nunique() 
print("Cantidad de Departamentos distintos en el DataSet de Bibliotecas: ", cantidad_deptos_bibliotecas) 

cantidad_deptos_establecimientos = establecimientos_educativos_limpio["id_departamento"].nunique() 
print("Cantidad de Departamentos distintos en el DataSet de Establecimientos Educativos: ", cantidad_deptos_establecimientos)


# Fin. 
