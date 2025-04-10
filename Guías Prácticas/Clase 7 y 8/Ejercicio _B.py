import pandas as pd 
from inline_sql import sql 

# Lectura de DataSets.
# departamento:pd.DataFrame = pd.read_csv('DataSets/departamento.csv') 
# provincia:pd.DataFrame = pd.read_csv('DataSets/provincia.csv')
# casos:pd.DataFrame = pd.read_csv('DataSets/casos.csv')
#! Por alguna razón, al querer hacer las consultas con el DataFrame creado, no lo reconoce.
#! Solución: junto la instrucción FROM llamar directamente al Path del archivo .csv del que fabricaría el DataFrame.
#! En este caso: 'DataSets/departamento.csv'

# Esta es otra opción que probé para llamar en FROM directamente usando 'departamento'.
# Pero no funcionó :(
# departamento = sql^ "SELECT * FROM 'DataSets/departamento.csv'"

#* Item a.
consulta_SQL_A:str = '''
                    SELECT * 
                    FROM "DataSets/departamento.csv" 
                    INNER JOIN "DataSets/provincia.csv" 
                    ON (departamento.id_provincia = provincia.id)
                    '''
# Me molesta que en el resultado queden tanto 'id_provincia' como 'id'.
# Siendo que ambos tienen los mismos datos. En el próximo trato de sacarlo y dejar uno solo.

#? Si hago renombres de los atributos a machear... existe el 'NATURAL JOIN' como una operación para consultas?

dfResultado_A = sql^ consulta_SQL_A 


#* Item b.
consulta_SQL_B_Aux:str = '''
                    SELECT * 
                    FROM "DataSets/departamento.csv"
                    INNER JOIN "DataSets/provincia.csv"
                    ON departamento.id_provincia = provincia.id
                    ''' 
dfResultado_B_Aux = sql^ consulta_SQL_B_Aux

consulta_SQL_B:str = '''
                    SELECT id AS codigo_depto, descripcion AS nombre_depto, descripcion_1 AS nombre_prov
                    FROM dfResultado_B_Aux
                    '''
dfResultado_B = sql^ consulta_SQL_B   #! No lo puedo probar porque no reconoce el DataFrame 'dfResultado_B_Aux'.


#* Item c.
consulta_SQL_C_Aux1:str = '''
                        SELECT id as id_Chaco 
                        FROM "DataSets/provincia.csv" 
                        WHERE (descripcion = 'Chaco')
                        '''
dfResultado_C_Aux1 = sql^ consulta_SQL_C_Aux1 

consulta_SQL_C:str = '''
                        SELECT id as codigo_depto 
                        FROM "DataSets/casos.csv" 
                        INNER JOIN dfResultado_C_Aux1
                        ON casos.id_depto = dfResultado_C_Aux1.id_depto
                        '''
dfResultado_C = sql^ consulta_SQL_C   #! No lo puedo probar porque no reconoce el DataFrame 'dfResultado_C_Aux1'.


#* Item d.
consulta_SQL_D_Aux1:str = '''
                        SELECT id as id_BsAs 
                        FROM "DataSets/provincia.csv" 
                        WHERE descripcion = 'Buenos Aires'
                        '''
dfResultado_D_Aux1 = sql^ consulta_SQL_D_Aux1 

consulta_SQL_D_Aux2:str = '''
                        SELECT *
                        FROM "DataSets/casos.csv"
                        INNER JOIN dfResultado_D_Aux1 
                        ON casos.id_depto = dfResultado_D_Aux1.id_BsAs
                        '''
dfResultado_D_Aux2 = sql^ consulta_SQL_D_Aux2 

consulta_SQL_D:str = '''
                    SELECT *
                    FROM dfResultado_D_Aux2 
                    WHERE (cantidad > 10) 
                    '''
dfResultado_D = sql^ consulta_SQL_D   #! No lo puedo probar porque no reconoce el DataFrame 'dfResultado_D_Aux1' ni 
                                      #! 'dfResultado_D_Aux2'.


# Banco de Pruebas -------------------------------------------------------------------------------------------------------- #

# print(dfResultado_A) 
