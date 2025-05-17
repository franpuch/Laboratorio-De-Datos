# -*- coding: utf-8 -*-
"""
Created on Fri May 16 13:38:36 2025

@author: franp
"""

import duckdb 

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