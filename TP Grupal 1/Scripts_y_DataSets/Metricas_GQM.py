# Laboratorio de Datos - TP 1. 
'''
Integrantes -> Dorogov Cristina 
            -> Pucciarelli Francisco Lautaro 
            -> Salto Julian 
               
Análisis de Calidad de Datos -> Goal Questions Metrics
'''

'''
Si aún no leyó el 'README', por favor leerlo.
'''

import pandas as pd
from pathlib import Path

'''
Preparación de los Path a los diferentes archivos.
'''

base_path = Path(__file__).resolve().parent        # Obtener la ruta base del script actual.
originales_path = base_path / 'TablasOriginales'   # Ruta a la carpeta donde se encuentran los DataSets originales.


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
Lectura del DataFrame originales.
'''

establecimientos_educativos = pd.read_excel(originales_path / "Padron_Oficial_Establecimientos_Educativos_2022.xlsx", 
                                            skiprows=6,
                                            dtype={'Código de localidad': str})

bibliotecas = pd.read_csv(originales_path / "Bibliotecas_Populares.csv")


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
GQM 1 -> Bibliotecas Populares.

- Objetivo: revisar bibliotecas sin email.

- Pregunta: ¿Qué porcentaje de Bibliotecas Populares no cuentan con email de contacto en la base de datos?

- Métrica: (100 x cantidad_de_bibliotecas_sin_email) / (cantidad_total_de_bibliotecas)
'''

contadorNulos = 0
contadorFilas = 0

for i,fila in bibliotecas.iterrows():
    if pd.isnull(fila["mail"]):
        contadorNulos += 1
    contadorFilas += 1
    
print("Cantidad Total de Bibliotecas: ", contadorFilas)
print("Cantidad de Bibliotecas con campo 'email' vacío (null): ", contadorNulos)
print("Métrica 1: " , (contadorNulos/contadorFilas)*100) 
print('\n') 
    

'''
Atributos de calidad afectados: Completitud y Vigencia.
- No estan presentes todos los valores para representar la realidad. Esto puede ser debido a que el dataset lleva 2 años sin actualizarse.

Problema de: Error de Software.
- El email podría ser un dato obligatorio, que no se asumió como tal y por lo tanto no se cargo (en algunos casos).
'''


# ------------------------------------------------------------------------------------------------------------------------------- #
'''
GQM 2 -> Establecimientos Educativos.

- Objetivo: Analizar los teléfonos de los distintos establecimientos educativos.

- Pregunta: ¿Qué porcentaje de establecimientos educativos presenta mas de un teléfono?

- Métrica: (100 x cantidad_de_establecimientos_educativos_que_tienen_mas_de_un_teléfono) / (cantidad_total_de_establecimientos_educativos)


Atributo de calidad afectado: Consistencia.
- No se sabe cuál es el teléfono vigente actualmente (de entre todos los que hay). O peor aún, hay télefonos con distinta longitud (no se 
especifica cuáles son celulares y cáles son teléfonos fijos, por ejemplo).

Problema de: Error de Software.
- No se pone como obligatorio la cantidad maxima de digitos que pueden ingresar, y por ende, las personas pueden cargar tantos como quieran.
Básicamente, no está estandarizado el formato del campo. Cosa que se solucionaría si se separase número de característica del resto del número
(por ejemplo).
'''

# print(establecimientos_educativos.dtypes) 
# Antes de meterme en la columna de Teléfonos, verifiqué con qué tipo de datos están cargados.

contadorTelDoble = 0
contadorFil=0
for i,fila in establecimientos_educativos.iterrows():
    if '/' in str(fila["Teléfono"]):
        contadorTelDoble += 1
    contadorFil += 1    

print("Mética 2: ", (contadorTelDoble / contadorFil) * 100)


# Fin. 
