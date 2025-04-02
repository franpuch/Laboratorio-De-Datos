# Ejercicios Clase 2. 
# Ejercicio 1.

print("No lo voy a programar.") 
print("Pero voy a desarrollar, en palabras, cada uno de los pasos que haría mi programa.")
print("Leer los comentarios...")

# Desarrollo
'''
Mi función primero abriría el archivo. Lo leería dentro de una variable, vamos a llamarla 'data'.
Listo la manipulación del archivo. Lo cierro y paso a el filtrado.

La variable 'data' (hasta donde tengo entendido) almacena una lista de strings. Cada elemento de 
'data' es una línea del archivo leído.
En una varibale llamada 'res' voy a crear un diccionario vacío.

Voy a iterar sobre 'data' (usando una variable llamada 'linea') y hacer lo siguiente:
    -  info = linea.split(',') -> esto almacena en 'info' una lista cuyos elementos son cada una 
        de las columnas de la 'linea' correspondiente.
    - En un condicional 'if', consultar si 'info[10]' es igual a 'parque' (variable pasada como 
        parámetro). Teniendo en cuenta que '10' es el index correspondiente a la columna del parque
        (o 'espacio_ve' según el nombre de la columna en el archivo original).
    - Si no es el caso, no hagas nada y pasá a la siguiente 'linea'.
    - Si es el caso, hace lo siguiente:
        - Crear una lista con los datos de 'info[3]', 'inf[4]', 'info[5]', 'info[6]', 'info[7]', 'info[8]', 'info[9]',
        'info[11]', 'info[12]', 'info[13]' y 'info[14]' (columnas que me parecen tienen datos importantes).
        - Al diccionario añadir un nuevo par clave-valor donde la clave es 'info[10]' y el valor es la lista
        creada en el pasito anterior.

Finalmente, retornar 'res'.
'''

# Fin. 