# -*- coding: utf-8 -*-
"""
Created on Thu May  1 12:45:37 2025

@author: Julia
"""

import pandas as pd
import duckdb


### GQM

## tabla BP
#nombres repetidos
#completitud: mails incompletos
#vigencia: año actualizacion: 2023 -> desactualizado

## tabla EE
#vigencia? datos del 2022
#nombres repetidos
#muchas filas con valores nulos en modalidad-submodalidad -> estructura mala 

###

#pip install openpyxl

#ee_df = pd.read_excel("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/establecimientos_educativos.xlsx", header = [0,1])

bibliotecas = pd.read_csv("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/bibliotecas-populares.csv")
#poblacion = pd.read_excel("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/padron_poblacion.xlsX", engine="openpyxl")
##escuelas = pd.read_excel("C:/Users/Julia/OneDrive/Escritorio/FACU/LaboDatos/TP1/establecimientos_educativos.xlsx", engine="openpyxl")

#escuelas = escuelas.iloc[11:]
#poblacion = poblacion.iloc[14:]

#print(bibliotecas.count())
#print("k")


#Limpieza dataset Biblioteca

bibliotecas.drop(columns=["tipo_latitud_longitud","telefono","web","domicilio","observacion","latitud","longitud","subcategoria","fuente","anio_actualizacion","cod_tel","piso","cp","informacion_adicional"], inplace=True)

### Me armo una tabla aparte q tome lo mas importante para las consultas
biblioteca_2 = bibliotecas[["nro_conabip","nombre","id_departamento","departamento","provincia","mail","fecha_fundacion"]].copy()

biblioteca_2["mail"] = biblioteca_2["mail"].str.split('@').str[1]
biblioteca_2["mail"] = biblioteca_2["mail"].str.split('.').str[0]
biblioteca_2["fecha_fundacion"] = pd.to_datetime(biblioteca_2["fecha_fundacion"])
biblioteca_2["año_fundacion"] = biblioteca_2["fecha_fundacion"].dt.year
biblioteca_2.drop(columns = ["fecha_fundacion"], inplace = True)

### CONSULTAS

#consulta ii
consultaSQL = duckdb.query(""" 
SELECT provincia, departamento, count(año_fundacion) AS cantidad_BP_fundadas_desde_1950 

FROM biblioteca_2 

WHERE año_fundacion >= 1950 

GROUP BY provincia,departamento

ORDER BY provincia, cantidad_BP_fundadas_desde_1950 DESC
""") 

df = consultaSQL.df()

#consulta iv
consultaSQL = duckdb.query(""" 

WITH tabla_temporal AS (
  SELECT 
    provincia,
    departamento,
    mail 
  FROM biblioteca_2
  WHERE mail IS NOT NULL
),
tabla_temp_conteo AS (
  SELECT 
    provincia,
    departamento,
    mail,
    COUNT(*) AS cantidad
  FROM tabla_temporal
  GROUP BY provincia, departamento, mail
)
SELECT provincia, departamento, mail, cantidad
FROM tabla_temp_conteo
ORDER BY provincia, departamento, cantidad DESC;

""") 




df = consultaSQL.df()




