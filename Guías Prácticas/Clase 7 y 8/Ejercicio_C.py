import pandas as pd 
from inline_sql import sql 

# Lectura de DataSets.
# departamento:pd.DataFrame = pd.read_csv('DataSets/departamento.csv') 
# casos:pd.DataFrame = pd.read_csv('DataSets/casos.csv')
# eventos:pd.DataFrame = pd.read_csv('DataSets/tipoevento.csv')
#! Por alguna razón, al querer hacer las consultas con el DataFrame creado, no lo reconoce.
#! Solución: junto la instrucción FROM llamar directamente al Path del archivo .csv del que fabricaría el DataFrame.
#! En este caso: 'DataSets/departamento.csv', 'DataSets/casos.csv' y 'DataSets/tipoevento.csv'

# Esta es otra opción que probé para llamar en FROM directamente usando 'departamento'.
# Pero no funcionó :(
# departamento = sql^ "SELECT * FROM 'DataSets/departamento.csv'"

#* Item a.
consulta_SQL_A_Aux1:str = '''
                        SELECT id AS id_depto, descripcion AS nombre_depto
                        FROM "DataSets/departamento.csv"
                        '''
dfResultado_A_Aux1 = sql^ consulta_SQL_A_Aux1 

consulta_SQL_A_Aux2:str = '''
                        SELECT id_depto, nombre_depto, id as id_caso, id_tipoevento, anio, semana_epidemiologica, id_grupoetario, cantidad
                        FROM dfResultado_A_Aux1
                        LEFT OUTER JOIN "DataSets/casos.csv"
                        ON dfResultado_A_Aux1.id_depto = "DataSets/casos.csv".id_depto
                        '''
# Aquí estoy buscando tomar todas las columnas, y una sola de las columnas de unión. Por eso me quedo con 
# 'id_depto' solamente (y no 'id_depto1', que es el nombre de la duplicada que permite la unión).
dfResultado_A_Aux2 = sql^ consulta_SQL_A_Aux2 

consulta_SQL_A:str = '''
                    SELECT nombre_depto
                    FROM dfResultado_A_Aux2 
                    WHERE cantidad = 'NaN'
                    '''
dfResultado_A = sql^ consulta_SQL_A   #! No lo puedo probar porque no reconoce el DataFrame 'dfResultado_A_Aux1' ni 
                                      #! 'dfResultado_A_Aux2'.


#* Item b.
consulta_SQL_B_Aux1:str = '''
                        SELECT id, descripcion, cantidad
                        FROM "DataSets/tipoevento.csv"
                        LEFT OUTER JOIN "DataSets/casos.csv" 
                        ON "DataSets/tipoevento.csv".id = "DataSets/casos.csv".id_tipoevento
                        '''
#? Puedo seleccionar columnas que nacen de un LEFT OUTER JOIN en la misma petición en la que hago el JOIN?
#? Ya sé que esto se responde ejecutando y viendo si el resultado es el que espero, pero justamente NO LOGRO
#? HACER CORRER MI INLINE_SQL.

dfResultado_B_Aux1 = sql^ consulta_SQL_B_Aux1 

consulta_SQL_B:str = '''
                    SELECT id, descripcion 
                    FROM dfResultado_B_Aux1 
                    WHERE cantidad = 'NaN'
                    '''

dfResultado_B = sql^ consulta_SQL_B   #! No lo puedo probar porque no reconoce el DataFrame 'dfResultado_B_Aux1'.

#* Fin. 
