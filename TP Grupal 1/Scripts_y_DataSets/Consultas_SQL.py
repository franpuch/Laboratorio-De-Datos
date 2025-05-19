# Laboratorio de Datos - TP 1. 
'''
Integrantes -> Dorogov Cristina 
            -> Pucciarelli Francisco Lautaro 
            -> Salto Julian 
               
Consultas SQL (sobre los DataSets limpios y procesados).
'''

'''
Si aún no leyó el 'README', por favor leerlo.
'''

import pandas as pd
import duckdb
from pathlib import Path

'''
Preparación de los Path a los diferentes archivos y carpeta de destino.
'''

base_path = Path(__file__).resolve().parent        # Obtener la ruta base del script actual. 
modelo_path = base_path / 'TablasModelo'           # Ruta a la carpeta donde se encuentran los DataSets limpios. 
consultas_path = base_path / 'ConsultasSQL'        # Ruta a la carpeta donde se van a guardar los DataSets limpios.
consultas_path.mkdir(exist_ok=True)                # Crear la carpeta de salida para las consultas SQL. 


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Lectura de DataSets.
'''

BP = pd.read_csv(modelo_path / "bibliotecas_populares.csv")
EE = pd.read_csv(modelo_path / "establecimientos_educativos.csv")
dept = pd.read_csv(modelo_path / "departamentos.csv")
EEcomunes = pd.read_csv(modelo_path / "establecimientos_educativos_comunes.csv")
nivel_educ_dept = pd.read_csv(modelo_path / "nivel_educativo_por_departamento.csv")


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Consultas.
'''

# Consulta i.

consulta_i = duckdb.query(""" 
                          SELECT
                            ANY_VALUE(EE.id_departamento) as id_dept,
                            sum(EEcomunes.jardin_maternal) AS jardin_maternal,
                            sum(EEcomunes.jardin_infantes) AS jardin_infantes,
                            sum(EEcomunes.primario) AS primarias,
                            sum(EEcomunes.secundario) AS secundarios,
                            ANY_VALUE (dept.nombre_departamento) AS departamento,
                            ANY_VALUE(dept.nombre_provincia) AS Provincia
                          FROM EEcomunes 
                          INNER JOIN EE 
                            ON EE.id_establecimiento = EEcomunes.id_establecimiento
                          INNER JOIN dept
                            ON dept.id_departamento = EE.id_departamento
  
                          GROUP BY dept.id_departamento

                         """) 
dfi = consulta_i.df()

consultaSQL2 = duckdb.query(""" 
                            SELECT 
                              dfi.Provincia,  
                              dfi.jardin_maternal,
                              nivel_educ_dept.jardin_maternal AS Poblacion_maternal,
                              dfi.jardin_infantes,
                              nivel_educ_dept.jardin_infante AS Poblacion_infante,
                              dfi.primarias,
                              nivel_educ_dept.primaria AS poblacion_primaria,
                              dfi.secundarios,
                              nivel_educ_dept.secundaria AS poblacion_secundaria,
                              dfi.departamento,
                            FROM dfi 
                            INNER JOIN nivel_educ_dept 
                              ON dfi.id_dept = nivel_educ_dept.id_departamento

                            """) 
dfi2 = consultaSQL2.df()

dfi2["Jardines"] = dfi2["jardin_infantes"] + dfi2["jardin_maternal"]
dfi2["Poblacion Jardin"] = dfi2["Poblacion_infante"] + dfi2["Poblacion_maternal"]
dfi2 = dfi2.drop(columns=["Poblacion_infante","Poblacion_maternal","jardin_infantes","jardin_maternal"])
dfi2 = dfi2[["Provincia","departamento","Jardines","Poblacion Jardin","primarias","poblacion_primaria","secundarios","poblacion_secundaria"]]


# Consulta ii.

consulta_ii = duckdb.query(""" 
                          SELECT nombre_provincia as provincia, nombre_departamento as departamento, count(año_fundacion) AS cantidad_BP_fundadas_desde_1950 

                          FROM BP

                          WHERE año_fundacion >= 1950 

                          GROUP BY provincia,departamento

                          ORDER BY provincia, cantidad_BP_fundadas_desde_1950 DESC
                          """) 
dfii = consulta_ii.df()


# Consulta iii.

aux = duckdb.query('''
                   SELECT id_departamento, count(id_biblioteca) as cantBP 
                   FROM BP
                   GROUP BY id_departamento                   
                   ''')
cantBPdept = aux.df()

aux2 = duckdb.query('''
                    SELECT id_departamento, count(id_establecimiento) as cantEE 
                    FROM EE
                    GROUP BY id_departamento                   
                   ''')
cantEEdept = aux2.df()

consulta_iii = duckdb.query(""" 

WITH tabla_temp AS(
    SELECT *
    FROM EE
    INNER JOIN EEcomunes 
        ON EE.id_establecimiento = EEcomunes.id_establecimiento
),
tabla_temp2 AS(
    SELECT 
        tabla_temp.id_establecimiento,
        tabla_temp.id_departamento,
        BP.id_biblioteca
    
    FROM tabla_temp
    
    INNER JOIN BP
        ON BP.id_departamento = tabla_temp.id_departamento
),
tabla_temp3 AS(
    SELECT 
        tabla_temp2.*, 
        nivel_educ_dept.poblacion_total
    FROM tabla_temp2
    
    INNER JOIN nivel_educ_dept
        ON tabla_temp2.id_departamento = nivel_educ_dept.id_departamento
)
SELECT 

    ANY_VALUE(dept.nombre_provincia) as Provincia,
    dept.nombre_departamento as Departamento,
    ANY_VALUE(cantBPdept.cantBP) as Cant_BP,
    ANY_VALUE(cantEEdept.cantEE) as Cant_EE,
    ANY_VALUE(tabla_temp3.poblacion_total) as Poblacion
FROM dept
INNER JOIN tabla_temp3
    ON dept.id_departamento = tabla_temp3.id_departamento

INNER JOIN cantBPdept
    ON cantBPdept.id_departamento = dept.id_departamento
INNER JOIN cantEEdept
    ON cantEEdept.id_departamento = dept.id_departamento

GROUP BY Departamento

""") 

dfiii = consulta_iii.df()


# Consulta iv.

consulta_iv = duckdb.query(""" 

WITH tabla_temporal AS (
  SELECT 
    nombre_provincia as provincia,
    nombre_departamento as departamento,
    dominio_email as mail 
  FROM BP
  WHERE mail IS NOT NULL
),
tabla_temp_conteo AS (
  SELECT 
    ANY_VALUE(provincia) as provincia,
    departamento,
    mail,
    COUNT(*) AS cantidad
  FROM tabla_temporal
  GROUP BY departamento, mail
),
tabla_final AS(
    SELECT 
        provincia,
        departamento,
        mail,
        cantidad
    FROM tabla_temp_conteo
    ORDER BY cantidad DESC
)
SELECT ANY_VALUE(provincia) as Provincia, departamento as Departamento, ANY_VALUE(mail) as Dominio_mas_frecuente, MAX(cantidad) as max
FROM tabla_final
GROUP BY Departamento
ORDER BY Departamento;

""") 
dfiv = consulta_iv.df()

dfiv = dfiv.drop(columns=["max"])


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Paso los df a tipo csv y los guardo para usarlos luego al hacer los graficos
'''

dfi2.to_csv(consultas_path / "dfi.csv", index=False)
dfii.to_csv(consultas_path / "dfii.csv", index=False)
dfiii.to_csv(consultas_path / "dfiii.csv", index=False)
dfiv.to_csv(consultas_path / "dfiv.csv", index=False)


# Fin. 
