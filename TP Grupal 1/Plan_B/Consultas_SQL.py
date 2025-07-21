# Laboratorio de Datos - TP 1. 
'''
Integrantes -> Dorogov Cristina 
            -> Pucciarelli Francisco Lautaro 
            -> Salto Julian 
               
Consultas SQL (sobre los DataSets limpios y procesados).
'''

'''
Si aún no leyó el 'ReadMe', por favor leerlo.
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

### Consulta i.

# Sumo la cantidad de niveles educativos (por separado) que hay en cada departamento.

consulta_i = duckdb.query(""" 
                          SELECT
                            ANY_VALUE(EE.id_departamento) as id_dept, 
                            sum(EEcomunes.jardin_maternal) AS jardin_maternal,          --Sumo la cantidad de cada nivel educativo.
                            sum(EEcomunes.jardin_infantes) AS jardin_infantes,      
                            sum(EEcomunes.primario) AS primarias,
                            sum(EEcomunes.secundario) AS secundarios,
                            ANY_VALUE (dept.nombre_departamento) AS departamento,
                            ANY_VALUE(dept.nombre_provincia) AS Provincia
                          FROM EEcomunes 
                          INNER JOIN EE 
                            ON EE.id_establecimiento = EEcomunes.id_establecimiento     --Joineo EEcomunes con EE para quedarme solo con los establecimientos comunes.
                          INNER JOIN dept
                            ON dept.id_departamento = EE.id_departamento                --Joineo la tabla (con la que vengo trabajando) con la tabla dept para obtener el nombre del departamento y de la provincia.
  
                          GROUP BY dept.id_departamento                                 --Agrupo por id_departamento.

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
                              nivel_educ_dept.poblacion_total AS poblacion_total       --Agrego la población total (útil luego para los gráficos)
                            FROM dfi 
                            INNER JOIN nivel_educ_dept 
                              ON dfi.id_dept = nivel_educ_dept.id_departamento

                            """) 
dfi2 = consultaSQL2.df()   # Básicamente, la misma tabla que 'dfi', pero le agrego la cantidad de población por nivel educativo (haciendo JOIN entre 'dfi' y 'nivel_educ_dept').

dfi2["Jardines"] = dfi2["jardin_infantes"] + dfi2["jardin_maternal"]    # Junto 'jardin_infantes' con 'jardin_maternal' para tener una sola columna de jardin (como se pide).
dfi2["Poblacion Jardin"] = dfi2["Poblacion_infante"] + dfi2["Poblacion_maternal"]   # Junto también sus poblaciones.
dfi2 = dfi2.drop(columns=["Poblacion_infante","Poblacion_maternal","jardin_infantes","jardin_maternal"])   # Elimino columnas innecesarias.
dfi2 = dfi2[["Provincia","departamento","Jardines","Poblacion Jardin","primarias","poblacion_primaria","secundarios","poblacion_secundaria", "poblacion_total"]] # Ordeno las columnas.


## Consulta ii.

# En esta consulta se busca obtener la cantidad de BP fundadas desde 1950, agrupadas según su departamento.

consulta_ii = duckdb.query(""" 
                          SELECT dept.nombre_provincia as provincia, dept.nombre_departamento as departamento, count(BP.año_fundacion) AS cantidad_BP_fundadas_desde_1950     --Tomo los datos necesarios.

                          FROM BP
                          
                          INNER JOIN dept                                           --Conecto la tabla BP con la de 'dept' para obtener la provincia y el nombre del departamento a partir de 'id_departamento' (clave en ambas tablas).
                          ON dept.id_departamento = BP.id_departamento

                          WHERE BP.año_fundacion >= 1950                            --Filtro según año.

                          GROUP BY dept.nombre_provincia,dept.nombre_departamento

                          ORDER BY dept.nombre_provincia, cantidad_BP_fundadas_desde_1950 DESC
                          """) 
dfii = consulta_ii.df()


## Consulta iii.

#En esta consulta se busca tomar la cantidad de BP y EE por departamento, junto con su población.

aux = duckdb.query('''
                   SELECT id_departamento, count(id_biblioteca) as cantBP 
                   FROM BP
                   GROUP BY id_departamento                   
                   ''')
cantBPdept = aux.df()   # Toma la cantidad de bibliotecas que hay por departamento.

aux2 = duckdb.query('''
                    SELECT EE.*
                    FROM EE
                    INNER JOIN EEcomunes 
                        ON EE.id_establecimiento = EEcomunes.id_establecimiento                 
                   ''')
a2 = aux2.df()   # Me quedo con los EE comunes (como se pide) para luego contarlos según el departamento.

aux2 = duckdb.query('''
                    SELECT id_departamento, count(id_establecimiento) as cantEE
                    FROM a2      
                    GROUP BY id_departamento
                   ''')
cantEEdept = aux2.df()


# Me voy armando tablas temporales para mantener el código encapsulado y organizado.

consulta_iii = duckdb.query(""" 

WITH tabla_temp AS(                                                            --Me quedo sólo con los establecimientos comunes.
    SELECT *
    FROM EE
    INNER JOIN EEcomunes 
        ON EE.id_establecimiento = EEcomunes.id_establecimiento
),
tabla_temp2 AS(                                                                --Conecto la tabla temporal anterior con la de 'bibliotecas', y me quedo con las columnas necesarias.         
    SELECT 
        tabla_temp.id_establecimiento,
        tabla_temp.id_departamento,
        BP.id_biblioteca
    
    FROM tabla_temp
    
    INNER JOIN BP
        ON BP.id_departamento = tabla_temp.id_departamento
)
SELECT                                                                         --Conecto 'tabla_temp2' con las de 'dept', 'nivel_educ_dept', 'cantBPdept' y 'cantEEdept' para obtener los datos necesarios.

    ANY_VALUE(dept.nombre_provincia) as Provincia,
    dept.nombre_departamento as Departamento,
    ANY_VALUE(cantBPdept.cantBP) as Cant_BP,
    ANY_VALUE(cantEEdept.cantEE) as Cant_EE,
    ANY_VALUE(nivel_educ_dept.poblacion_total) as Poblacion
FROM tabla_temp2

INNER JOIN dept
ON dept.id_departamento = tabla_temp2.id_departamento

INNER JOIN nivel_educ_dept
    ON tabla_temp2.id_departamento = nivel_educ_dept.id_departamento

INNER JOIN cantBPdept
    ON cantBPdept.id_departamento = tabla_temp2.id_departamento
    
INNER JOIN cantEEdept
    ON cantEEdept.id_departamento = tabla_temp2.id_departamento

GROUP BY Departamento

""") 

dfiii = consulta_iii.df()


## Consulta iv.

# Lo que se busca en esta consulta es quedarte con el dominio de mail más frecuente para cada departamento según sus bibliotecas.
# Me voy armando tablas temporales para mantener el código encapsulado y organizado.

consulta_iv = duckdb.query(""" 

WITH tabla_temporal AS (                                --Me armo una tabla temporal con los distintos dominios de mail no nulos que hay en cada departamento.
  SELECT 
    dept.nombre_provincia as provincia,
    dept.nombre_departamento as departamento,
    BP.dominio_email as mail 
  FROM BP
  INNER JOIN dept
  ON dept.id_departamento = BP.id_departamento
  WHERE mail IS NOT NULL
),
tabla_final AS (                                       --Tabla temporal para contar (y ordenar según) la cantidad de veces que aparece cada dominio de mail en cada departamento a partir de la tabla anterior.
  SELECT 
    ANY_VALUE(provincia) as provincia,
    departamento,
    mail,
    COUNT(*) AS cantidad
  FROM tabla_temporal
  GROUP BY departamento, mail
  ORDER BY cantidad DESC
)
SELECT                                                 --Consulta final que toma lo necesario de la tabla temporal anterior, el dominio de mail que más veces aparece en cada departamento, y agrupa por departamento.
    ANY_VALUE(provincia) as Provincia, 
    departamento as Departamento, 
    ANY_VALUE(mail) as Dominio_mas_frecuente, 
    MAX(cantidad) as max
FROM tabla_final
GROUP BY Departamento
ORDER BY Departamento

""") 
dfiv = consulta_iv.df()

dfiv = dfiv.drop(columns=["max"])   # Elimino la columna 'max' de la tabla final (me decía la cantidad de veces que aparecía cada dominio de mail por departamento).


# ----------------------------------------------------------------------------------------------------------------------------------- #
'''
Paso los 'df' a tipo CSV, y los guardo para usarlos luego al hacer los graficos.
'''

dfi2.to_csv(consultas_path / "dfi.csv", index=False)
dfii.to_csv(consultas_path / "dfii.csv", index=False)
dfiii.to_csv(consultas_path / "dfiii.csv", index=False)
dfiv.to_csv(consultas_path / "dfiv.csv", index=False)

print("Todas los resultados de las consultas exportados exitosamente (en formato CSV) en la carpeta 'Consultas_SQL'")

# Fin del archivo. 
# Saludos.
