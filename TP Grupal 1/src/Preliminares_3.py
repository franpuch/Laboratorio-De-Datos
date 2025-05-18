# Laboratorio de Datos - TP 1.
# Trabajos Preliminares 3 - Limpieza y Formateo de DataSet -> Bibliotecas Populares.

import pandas as pd 
import os 

''' LEER ANTES DE EJECUTAR. 
Por favor, en la línea 15 completar con la ruta (path absoluto) donde se encuentre el archivo correspondiente a el Dataset 
original de 'Bibliotecas Populares' en formato '.csv'.
También completar en la línea 61 con la ruta (path absoluto) donde en encuentre la carpeta "DataSets Limpios" creada al 
ejecutar el archivo 'Preliminares_2.py' (para que el dataset limpio se almacene en la misma carpeta que los demás).
'''

# Lectura del DataSet original.
bibliotecas = pd.read_csv("")


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

# Utilizo la librería 'os' para buscar (crear si no existe) la carpeta donde estoy almacenando los archivos limpios.
carpeta = ""
nombre_archivo = "bibliotecas_populares.csv"
ruta_completa = os.path.join(carpeta, nombre_archivo)

biblioteca_2.to_csv(ruta_completa, index=False)
print("Archivo guardado como 'bibliotecas_populares.csv'")


# Fin. 
