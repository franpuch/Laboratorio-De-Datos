# import pandas as pd // Lo comento pues no lo estoy usando... pero DEBERÍA (si me dejase laburar tranquilo).
from inline_sql import sql 

# Lectura de DataSets.
# departamento:pd.DataFrame = pd.read_csv('DataSets/departamento.csv') 
#! Por alguna razón, al querer hacer las consultas con el DataFrame creado, no lo reconoce.
#! Solución: junto la instrucción FROM llamar directamente al Path del archivo .csv del que fabricaría el DataFrame.
#! En este caso: 'DataSets/departamento.csv'

# Esta es otra opción que probé para llamar en FROM directamente usando 'departamento'.
# Pero no funcionó :(
# departamento = sql^ "SELECT * FROM 'DataSets/departamento.csv'"

#* Item a.
consulta_SQL_A:str = '''
                    SELECT descripcion 
                    FROM 'DataSets/departamento.csv';
                    '''

dfResultado_A = sql ^ consulta_SQL_A  


#* Item b.
consulta_SQL_B:str = '''
                    SELECT DISTINCT descripcion 
                    FROM 'DataSets/departamento.csv'
                    '''

dfResultado_B = sql^ consulta_SQL_B 


#* Item c.
consulta_SQL_C:str = '''
                    SELECT id, descripcion
                    FROM 'DataSets/departamento.csv'
                    '''
#? Don´t use DISTINCT because 'id' is a key attribute (for dedfinition, they´re all different).

dfResultado_C = sql^ consulta_SQL_C


#* Item d.
consulta_SQL_D:str = '''
                    SELECT * 
                    FROM 'DataSets/departamento.csv'
                    '''

dfResultado_D = sql^ consulta_SQL_D 


#* Item e.
consulta_SQL_E:str = '''
                    SELECT id AS codigo_depto, descripcion AS nombre_depto
                    FROM "DataSets/departamento.csv"
                    '''
#? Don´t use DISTINCT because 'id' is a key attribute (for dedfinition, they´re all different).

dfResultado_E = sql^ consulta_SQL_E 


#* Item f.
consulta_SQL_F:str = '''
                    SELECT * 
                    FROM "DataSets/departamento.csv"
                    WHERE (id_provincia = 54)
                    '''
# Podría emprolijarlo un poco más pidiendo 'SELECT id AS codigo_depto, descripcion AS nombre_depto'
# Pero bueno, lo dejo así sobre todo para verificar que mi consulta es correcta.

dfResultado_F = sql^ consulta_SQL_F 


#* Item g.
consulta_SQL_G:str = '''
                    SELECT * 
                    FROM "DataSets/departamento.csv"
                    WHERE (id_provincia = 22) OR (id_provincia = 78) OR (id_provincia = 86)
                    '''

dfResultado_G = sql^ consulta_SQL_G 


#* Item h.
consulta_SQL_H:str = '''
                    SELECT *
                    FROM "DataSets/departamento.csv"
                    WHERE (id_provincia > 49) AND (id_provincia < 60) 
                    '''

dfResultado_H = sql^ consulta_SQL_H 


# Banco de Pruebas -------------------------------------------------------------------------------------------------------- #

# print(departamento.head(10)) 
# print(departamento) 

# print(dfResultado_A)
# print(dfResultado_B) 
# print(dfResultado_C)
# print(dfResultado_D) 
# print(dfResultado_E) 
# print(dfResultado_F) 
# print(dfResultado_G) 
# print(dfResultado_H) 

#* Fin. 