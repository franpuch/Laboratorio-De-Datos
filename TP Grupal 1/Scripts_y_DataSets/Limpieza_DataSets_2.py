# Laboratorio de Datos - TP 1. 
'''
Integrantes -> Dorogov Cristina 
            -> Pucciarelli Francisco Lautaro 
            -> Salto Julian 
               
Limpieza y Formateo de DataSet -> Bibliotecas Populares.
'''

'''
Si aún no leyó el 'README', por favor leerlo.
'''

import pandas as pd 
from pathlib import Path 

'''
Preparación de los Path a los diferentes archivos y carpeta de destino.
'''

base_path = Path(__file__).resolve().parent        # Obtener la ruta base del script actual.
originales_path = base_path / 'TablasOriginales'   # Ruta a la carpeta donde se encuentran los DataSets originales.
modelo_path = base_path / 'TablasModelo'           # Ruta a la carpeta donde se van a guardar los DataSets limpios.
modelo_path.mkdir(exist_ok=True)                   # Si no existe la carpeta ded salida, crearla.


# ------------------------------------------------------------------------------------------------------------------------------- #

# Lectura del DataSet original.
bibliotecas = pd.read_csv(originales_path / 'Bibliotecas_Populares.csv')


#Limpieza dataset Biblioteca
bibliotecas.drop(columns=["tipo_latitud_longitud", 
                          "telefono", 
                          "web", 
                          "domicilio", 
                          "observacion", 
                          "latitud", 
                          "longitud", 
                          "subcategoria", 
                          "fuente", 
                          "anio_actualizacion", 
                          "cod_tel", 
                          "piso", 
                          "cp", 
                          "informacion_adicional"], 
                 inplace=True)


# Me armo una tabla aparte q tome lo mas importante para las consultas.
biblioteca_2 = bibliotecas[["nro_conabip","nombre","id_departamento","departamento","provincia","mail","fecha_fundacion"]].copy()

biblioteca_2["mail"] = biblioteca_2["mail"].str.split('@').str[1]
biblioteca_2["mail"] = biblioteca_2["mail"].str.split('.').str[0]
biblioteca_2["fecha_fundacion"] = pd.to_datetime(biblioteca_2["fecha_fundacion"])
biblioteca_2["año_fundacion"] = biblioteca_2["fecha_fundacion"].dt.year
biblioteca_2.drop(columns = ["fecha_fundacion"], inplace = True) 


# Cambio el nombre de las columnas.
biblioteca_2.columns = ["id_biblioteca", 
                        "nombre_biblioteca",
                        "id_departamento",
                        "nombre_departamento",
                        "nombre_provincia",
                        "dominio_email",
                        "año_fundacion"] 


# Para respetar el MR, tomo solo las columnas que explicitamos allí. 
columnas_MR:list[str] = ["id_biblioteca", "nombre_biblioteca", "id_departamento", "año_fundacion", "dominio_email"]
biblioteca_clean = biblioteca_2[columnas_MR]

# Exporto a csv el DataSet limpio (en su carpeta correspondiente).

biblioteca_clean.to_csv(modelo_path / 'bibliotecas_populares.csv', index=False)
print("Archivo guardado como 'bibliotecas_populares.csv'")


# Fin. 
