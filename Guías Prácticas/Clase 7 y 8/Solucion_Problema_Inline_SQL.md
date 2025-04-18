# Solución al Error de `Inline SQL`

Estoy realizando las consultas con **Inline SQL**. 
Para ello, lo estoy importando: `from inline_sql import sql`.

Para poder realizazr las consultas y demás, estoy siguiendo los pasos que se detallan en las Presentaciones de la *Clase 6, 7 y 8 - AR SQL*.
Pero, por alguna razón que desconozco, no me reconoce los *pandas DataFrames* y no puedo hacer ninguna consulta a nada.

### Solución: utilizar `Duckdb`

Importo la librería de la siguiente forma: `import duckbd as dk`.

Para usarlo, escribo las consultas dentro de un string (como hacía antes para `inline_sql`); por ejemplo, en la variable `consultaSQL:str`.
A la hora de crear el DataFrame resultado de la consulta, con `inline_sql` hacía (por ejemplo): `df_Resultado = sql^ consultaSQL`. 
El equivalente en `Duckdb` es `df_Resultado = dk.query(consultaSQL).df()`. 

Es más, puedo usar `df_Resultado` dentro de otras consultas (para hacer *JOINS* y demás) y los reconoce sin problemas.


**Fin.** 