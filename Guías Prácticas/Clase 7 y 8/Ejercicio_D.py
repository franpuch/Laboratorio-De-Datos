import pandas as pd 
import duckdb as dk

# Lectura de DataSets.
departamento:pd.DataFrame = pd.read_csv('DataSets/departamento.csv') 
casos:pd.DataFrame = pd.read_csv('DataSets/casos.csv')
eventos:pd.DataFrame = pd.read_csv('DataSets/tipoevento.csv')
provincia:pd.DataFrame = pd.read_csv('DataSets/provincia.csv')


#* Item a.
consulta_SQL_A:str = '''
                    SELECT SUM(cantidad) AS cantidad_total_casos
                    FROM casos
                    '''

df_Resultado_A = dk.query(consulta_SQL_A).df()  
# print(df_Resultado_A) 


#* Item b.
consulta_SQL_B_Aux1:str = '''
                    SELECT id_tipoevento, anio, SUM(cantidad) AS cantidad_total_casos
                    FROM casos
                    GROUP BY id_tipoevento, anio
                    ORDER BY id_tipoevento ASC, anio DESC
                    '''

df_Resultado_B_Aux1 = dk.query(consulta_SQL_B_Aux1).df() 
# print(df_Resultado_B_Aux1) 


consulta_SQL_B:str = '''
                    SELECT descripcion, anio, cantidad_total_casos 
                    FROM df_Resultado_B_Aux1 
                    LEFT OUTER JOIN eventos
                    ON df_resultado_B_Aux1. id_tipoevento = eventos.id
                    '''

df_Resultado_B = dk.query(consulta_SQL_B).df() 
# print(df_Resultado_B) 


#* Item c.
# Uso el resultado del Ítem anterior.
consulta_SQL_C:str = '''
                    SELECT * 
                    FROM df_Resultado_B 
                    WHERE anio = 2019
                    '''

df_Resultado_C = dk.query(consulta_SQL_C).df() 
# print(df_Resultado_C) 


#* Item d.
consulta_SQL_D:str = '''
                    SELECT id_provincia, COUNT(*) AS cantidad_departamentos
                    FROM departamento 
                    GROUP BY id_provincia 
                    ORDER BY id_provincia ASC
                    '''

df_Resultado_D = dk.query(consulta_SQL_D).df() 
# print(df_Resultado_D) 


#* Item e.
# Tomo el 'listar los departamentos con menos cantidad de casos' como un 'listar los departamentos cuya 
# cantidad de casos es menor que el promedio'. Aspero este... creo que necesito 'subqueries'

consulta_SQL_E:str = '''
                        SELECT id_depto, cantidad AS cantidad_casos
                        FROM casos 
                        WHERE casos.cantidad < (
                            Aquí va la subquery que calcula el promedio de casos de 2019.
                            Me salió así... pero creo que no arranca.
                            SELECT AVG(cantidad) AS promedio 
                            FROM casos 
                            GROUP BY anio
                            WHERE anio = 2019
                                                )
                        ORDER BY cantidad DESC
                        '''

#! PREGUNTAR CÓMO TERMINARLO/CORREJIRLO.
# Dejo comentada la consulta hasta que pregunte cómo terminarlo.
# df_Resultado_E = dk.query(consulta_SQL_E).df() 
# print(df_Resultado_E) 


#* Item f.
# Tomo el 'listar los departamentos con mayor cantidad de casos' como un 'listar los departamentos cuya 
# cantidad de casos es mayor que el promedio'. Aspero este... creo que necesito 'subqueries'

consulta_SQL_F:str = '''
                        SELECT id_depto, cantidad AS cantidad_casos
                        FROM casos 
                        WHERE casos.cantidad > (
                            Aquí va la subquery que calcula el promedio de casos de 2019.
                            Me salió así... pero creo que no arranca.
                            SELECT AVG(cantidad) AS promedio 
                            FROM casos 
                            GROUP BY anio
                            WHERE anio = 2020
                                                )
                        ORDER BY cantidad ASC
                        '''

#! PREGUNTAR CÓMO TERMINARLO/CORREJIRLO.
# Dejo comentada la consulta hasta que pregunte cómo terminarlo.
# df_Resultado_F = dk.query(consulta_SQL_F).df() 
# print(df_Resultado_F) 


#* Item g.

# Primero busco tener en una misma tabla los id de departamentos con su nombre y  provincia correspondiente.
consulta_SQL_G_Aux1:str = '''
                        SELECT depto.id AS id_depto, depto.descripcion AS nombre_depto, 
                               prov.descripcion AS nombre_provincia
                        FROM departamento AS depto
                        INNER JOIN provincia AS prov
                        ON depto.id_provincia = prov.id
                        '''
df_Resultado_G_Aux1 = dk.query(consulta_SQL_G_Aux1).df() 
# print(df_Resultado_G_Aux1) 

# Ahora busco tener en una misma tabla todos los casos unidos a su provincia correspondiente.
consulta_SQL_G_Aux2:str = '''
                        SELECT casos.anio, casos.cantidad AS cantidad_casos, aux.nombre_provincia
                        FROM casos 
                        INNER JOIN df_Resultado_G_Aux1 AS aux
                        ON casos.id_depto = aux.id_depto 
                        '''
df_Resultado_G_Aux2 = dk.query(consulta_SQL_G_Aux2).df() 
# print(df_Resultado_G_Aux2)  

# Ahora sí, aplico la función de agregación y devuelvo lo que pide el ejercicio.
consulta_SQL_G:str = '''
                    SELECT anio, nombre_provincia AS provincia, AVG(cantidad_casos) AS promedio_casos
                    FROM df_Resultado_G_Aux2 AS aux
                    GROUP BY anio, nombre_provincia
                    ORDER BY anio ASC
                    '''
df_Resultado_G = dk.query(consulta_SQL_G).df() 
# print(df_Resultado_G) 


#* Item h.
# Igual que antes, en una sola tabla busco tener relacionado los departamentos con su respectiva provincia.
consulta_SQL_H_Aux1:str = '''
                        SELECT depto.id AS id_depto, depto.descripcion AS nombre_depto, prov.descripcion AS nombre_provincia
                        FROM departamento AS depto 
                        INNER JOIN provincia AS prov
                        ON depto.id_provincia = prov.id
                        '''
df_Resultado_H_Aux1 = dk.query(consulta_SQL_H_Aux1).df()
# print(df_Resultado_H_Aux1) 

# Ahora busco los casos de cada uno de los departamentos. Pero, ya armo la suma de todos los casos de cada
# departamento por año.
consulta_SQL_H_Aux2:str = '''
                        SELECT casos.anio, aux.nombre_depto AS depto, SUM(casos.cantidad) AS cantidad_casos, aux.nombre_provincia AS provincia
                        FROM df_Resultado_H_Aux1 AS aux
                        INNER JOIN casos
                        ON aux.id_depto = casos.id_depto
                        GROUP BY anio, nombre_depto, nombre_provincia 
                        ORDER BY anio ASC, cantidad_casos ASC 
                        '''
df_Resultado_H_Aux2 = dk.query(consulta_SQL_H_Aux2).df()
# print(df_Resultado_H_Aux2) 

# Ahora sí, por cada año y cada provincia, busco el departamento que más cantidad de casos tuvo.
consulta_SQL_H:str = '''
                    SELECT t1.anio, t1.provincia, t1.depto AS depto_mayor_cantidad_casos, t1.cantidad_casos AS max_casos
                    FROM df_Resultado_H_Aux2 AS t1
                    INNER JOIN 
                        (SELECT anio, provincia, MAX(cantidad_casos) AS max_cantidad
                        FROM df_Resultado_H_Aux2
                        GROUP BY anio, provincia) AS t2
                    ON t1.anio = t2.anio AND t1.provincia = t2.provincia AND t1.cantidad_casos = t2.max_cantidad
                    ORDER BY t1.anio ASC;
                    '''
df_Resultado_H = dk.query(consulta_SQL_H).df() 
# print (df_Resultado_H) 


#* Item i.


#* Fin. 