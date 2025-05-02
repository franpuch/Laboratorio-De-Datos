# Apuntes Generales.

### Exploración e Investigación de DataSets Originales.

Del DataSet 'Padron_Oficila_Establecimientos_educativos_2022' observamos:
- De toda la tabla, las columnas binarias correspondientes a la descripción de cada modalidad las separaríamos en *relaciones independientes*.

Del DataSet 'Bibliotecas_Populares.csv' observamos: 
- Las columnas de 'observación' y 'subcategoría' estan vacías en todas las filas.
- La columna 'información_adicional' parece estar vacía en todas las filas (**investigar con SQL**). 
- La columna 'web' parece estar vacía en todas las filas (**investigar con SQL**). 
- Las columnas correspondientes al contacto (de cada fila) no están todas completas. 
- La última columna 'anio_actualizacion' parece tener en todas el mismo dato '2023' (**verificarlo con SQL**). 

Del DataSet 'Padron_Población':
- No tenemos mucho contexto de las columnas 'casos' y 'Edad'. No sabemos bien qué representan.
- Suponemos que la columna 'casos' es la cantidad de personas con edad 'Edad' que viven en el área taggeada.
- La columna '%' suponemos representa cuánto es la cantidad (de casos) respecto del total de personas de esa edad.
- La columna 'Acumulado %' es simplemente la suma de los porcentajes anteriores + el dato de '%' de esa fila.

Relaciones entre DataSets:
- El código de 'Area' en el DataSet 'Padron_Poblacion' es el mismo que 'id_departamento' del Dataset 'Bibliotecas_Populares'. 

### Planteamiento del Objetivo. 

**Objetivo General del Trabajo**: saber si existe alguna relación entre la cantidad de *establecimientos educativos* en cada una de las 
provincias y la cantidad de Bibliotecas Populares. 
- Conocer la relación entre la cantidad de establecimientos educativos respecto la población y su influencia en la cantidad 
de bibliotecas populares (por departamento). 

**Objetivos Preliminares:** Cosas que podemos extraer de los datos (para luego sacar conlcusiones). 
- Saber cuál es el porcentaje de establecimientos educativos (correspondiete a cada grupo etario) respecto a la cantidad de población 
(de cada grupo etario). 
- Saber cuál es el porcentaje de bibliotecas respecto a la cantidad de establecimientos educativos. 
- Saber cuál es el porcentaje de bibliotecas respecto a la cantidad de población. 
- Cuál es la región del país (provincias, departamentos) que mayor cantidad de bibliotecas tiene y si eso se corresponde correctamente con la 
población y establecimientos educativos. 

### Fuente de Datos para cada Cosa.

*Cantidad de Población por Departamento*: lo tenemos explícitamente en 'Padron_Poblacion'. 

*Cantidad de Población de Provincia con Bibliotecas Registradas*: lo obtenemos de combinar 'Padron_Poblacion' con 'Bibliotecas_Populares'. 

*Cantidad de Establecimientos Educativos de cada tipo (modalidad) por provincia y por departamento (capaz)*: lo obtenemos de 
'Padron_Oficila_Establecimientos_Educativos_2022'.

*Problema de Mergear el departamento del Establecimiento Educativo con el departamento de las Bibliotecas Populares*: 
Confiamos que en ambos DataSets están escritos todos con los mismos nombres. Sino, no tenemos forma de unir ambos DataSets (los demás datos no son 
siempre iguales).

