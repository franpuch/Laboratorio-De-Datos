# Apuntes de `NumPy`

Importar `NumPy` en el archivo a trabajar.
```Python
import numpy as np
```

### Typado de Variables `npArrays`

A la hora de crear variables que almacenen `npArrays` (arrays de NumPy), las puedo *typar* con el siguiente tag
```Python
v:np.ndarray[int]   # 'v' es una variable que almacena un array de ints.

w: np.ndarray[float]   # 'w' es una variable que almacena un array de floats.
```

### Operaciones Básicas

##### Crear un `npArray`
Formas de crear `npArrays`
```Python
v:np.ndarray[int] = np.array([3, 45, 6, -3, 0])

lista:list[float] = [-4, 4.5, 55.9, 7, 0.5, -1]
w:np.ndarray[float] = np.array(lista)
```

Para saber el tipo (de dato) de los datos que almacena un `npArray`, usamos el atributo `dtype`.
```Python
print(v.dtype)

print(w.dtype)
```

##### Atributos de un `npArray`
Más atributos :
- `v.ndim` -> Devuelve el número de dimensiones o ejes que tiene el array.
	- Un array 1D (como una lista de números) tiene `ndim = 1`.
	- Un array 2D (como una matriz) tiene `ndim = 2`.
	- Un array 3D (como un cubo) tiene `ndim = 3`.
	- Y así sucesivamente.
- `v.size` -> Devuelve el número total de elementos que contiene el array.
- `v.shape` -> Devuelve una tupla que indica la longitud de cada dimensión del array. 
	- Un array 1D de 5 elementos tiene `shape = (5,)`.
	- Una matriz de 3 filas y 4 columnas tiene `shape = (3, 4)`.
	- Un cubo de 2x2x2 tiene `shape = (2, 2, 2)`.
- `v.nbytes` -> Devuelve el número total de bytes que ocupa el array en la memoria.

### Operaciones Aritméticas y Lógicas Básicas

##### Operaciones Aritméticas Básicas
**Operaciones aritméticas** básicas aplicables a un `npArray`
```Python
x:np.ndarray = np.array([1.0, 2.0, 3.0])
y:np.ndarray = np.array([4, 5, 6])

# Operaciones entre array y un escalar.
# Se aplica la operación a cada uno de los elementos.
print(x + 2)   # Out: [3. 4. 5.]
print(y - 4)   # Out: [0 1 2]
print(x * 2)   # Out: [2. 4. 6.]
print(y / 3)   # Out: [1.33333333 1.66666667 2.        ]

# Operaciones entre arrays.
# Se realiza la operación entre componentes (posiciones) iguales.
print(x + y)   # Out: [5. 7. 9.]
print(x - y)   # Out: [-3. -3. -3.]
print( x * y)  # Out: [ 4. 10. 18.]
print(x / y)   # Out: [0.25 0.4  0.5 ]
```

> [!NOTE]
> Ejecutar operaciones entre `npArrays` de distinto tamaño (`shape`) rompe la ejecución.
> Normal, ya que las operaciones se realizan componente a componente.

**Más operaciones** aritméticas:
- `**` -> potencia
- `%` -> módulo
Ambas anteriores funcionan tanto con un `npArray` y escalar, como entre dos `npArrays` (componente a componente).

##### Operaciones Lógicas Básicas 
**Operaciones Lógicas**:
```Python
# Para el caso de dos npArrays, realiza las comparaciones componente a componente.
print (x > y)    # Out: [False False False]
print (x >= y)   # Out: [False False False]
print (x < y)    # Out: [ True  True  True]
print (x <= y)   # Out: [ True  True  True]
print (x != y)   # Out: [ True  True  True]
print (x == y)   # Out: [False False False]

# Para el caso de un escalar, realiza las comparaciones para cada uno de los elementos.
print (x > 0)    # Out: [ True  True  True]
print (x >= 2)   # Out: [False  True  True]
print (x < 5)    # Out: [ True  True  True]
print (x <= 2)   # Out: [ True  True False]
print (x != 2)   # Out: [ True False  True]
print (x == 2)   # Out: [False  True False]
```

### Indexación de Elementos de `npArrays`

Para **acceder a los elementos** de un `npArray` se utilizan los `[ ]`, al igual que las listas/arrays de Python.
- El primer elemento es el `0` (Python es un lenguaje de índice cero)
- Para recorrer el `npArray` desde el final, usamos índices negativos. Ej. `-1` es el índice del último elemento, `-2` el índice del ante último, y así sucesivamente.
- Utilizando los dos puntos `:` puede obtenerse un `slice`: `a:b` . Significa tomar todos los elementos desde el `a` (incluido) hasta el `b` (excluido). Ej. `w[1:7]`
- Puede agregarse también el paso: `a:b:c` . Significa tomar todos los elementos desde el `a` (incluido) hasta el `b` (excluido) de haciendo pasos de largo `c` . Ej. `w[1:7:2]`

La misma sintaxis sirve para modificar valores de determinada posiciones.

### Funciones Trigonométricas Básicas

Estas funciones calculan el coseno (`cos`), seno (`sin`) y tangente (`tan`) de un ángulo dado.

```Python
import numpy as np

angulo = np.pi / 4  # Ángulo de 45 grados en radianes

coseno = np.cos(angulo)
seno = np.sin(angulo)
tangente = np.tan(angulo)

print("Coseno:", coseno)
print("Seno:", seno)
print("Tangente:", tangente)
```

> [!WARNING]
> Las funciones trigonométricas de NumPy **esperan que los ángulos estén en radianes**. Si tienes ángulos en grados, puedes convertirlos a radianes usando la función `np.radians()`:
> ```Python
> angulo_grados = 45
> angulo_radianes = np.radians(angulo_grados)
> ```

Estas funciones **pueden aplicarse a arrays NumPy completos**, lo que permite realizar cálculos de manera eficiente en conjuntos de datos:

```Python
import numpy as np

angulos = np.array([0, np.pi / 2, np.pi])

cosenos = np.cos(angulos)

print("Cosenos: ", cosenos)
```

##### Función Raíz Cuadrada
La función `sqrt` calcula la raíz cuadrada de un número.

```Python
import numpy as np

numero = 16

raiz_cuadrada = np.sqrt(numero)

print("Raíz cuadrada:", raiz_cuadrada)
```

Al igual que las trigonométricas, la función `sqrt` pueden aplicarse a un array NumPy completo.

##### Función Hipotenusa
La función `hypot` calcula la hipotenusa de un triángulo rectángulo dados los catetos.
```Python
import numpy as np

cateto1 = 3
cateto2 = 4

hipotenusa = np.hypot(cateto1, cateto2)

print("Hipotenusa:", hipotenusa)  # Imprime 5.0
```

La función `hypot` puede trabajar con números enteros o de punto flotante y devuelve la hipotenusa como un número de punto flotante. Al igual que todas las anteriores, **puede aplicarse a un `npArray` completo** (aplica la función elemento por elemento, y devuelve otro `npArray` con los resultados).

### Funciones de Redondeo de Números

Las funciones `round`, `ceil` y `floor` de NumPy son útiles para realizar redondeos de números.

La función `round` redondea un número al entero más cercano. Si el decimal es mayor o igual a 0.5, se redondea hacia arriba; si es menor a 0.5, se redondea hacia abajo.
```Python
import numpy as np

numero = 7.6

redondeo = np.round(numero)

print("Redondeo:", redondeo)  # Imprime 8
```

La función `round` permite especificar la cantidad de decimales a la que se desea redondear:
```Python
numero = 7.6543

redondeo_dos_decimales = np.round(numero, 2)

print("Redondeo a dos decimales:", redondeo_dos_decimales)  # Imprime 7.65
```

La función `ceil` (que viene de "ceiling", techo en inglés) redondea un número hacia el entero mayor más cercano. Siempre redondea hacia arriba, independientemente del valor decimal.
```Python
import numpy as np

numero = 7.2

redondeo_arriba = np.ceil(numero)

print("Redondeo hacia arriba:", redondeo_arriba)  # Imprime 8
```

La función `floor` (que significa "piso" en inglés) redondea un número hacia el entero menor más cercano. Siempre redondea hacia abajo, sin importar el valor decimal.
```Python
import numpy as np

numero = 7.9

redondeo_abajo = np.floor(numero)

print("Redondeo hacia abajo:", redondeo_abajo)  # Imprime 7
```

Al igual que las funciones trigonométricas y `sqrt`, `round`, `ceil` y `floor` también pueden aplicarse a arrays NumPy:
```Python
import numpy as np

numeros = np.array([3.1, 5.5, 8.9, 2.2])

redondeados = np.round(numeros)
redondeados_arriba = np.ceil(numeros)
redondeados_abajo = np.floor(numeros)

print("Redondeados:", redondeados)
print("Redondeados hacia arriba:", redondeados_arriba)
print("Redondeados hacia abajo:", redondeados_abajo)
```

### Funciones Lógicas

NumPy también provee sus propias operaciones lógicas proposicionales básicas.
- `logical_and`: Realiza una operación lógica "AND" elemento a elemento entre dos `npArrays`. Devuelve un `npArray` de booleanos donde cada elemento es True si ambos elementos correspondientes en los arrays de entrada son True, y False en caso contrario.
- `logical_or`: Realiza una operación lógica "OR" elemento a elemento entre dos `npArrays`. Devuelve un `npArray` de booleanos donde cada elemento es True si al menos uno de los elementos correspondientes en los arrays de entrada es True, y False en caso contrario.

```Python
import numpy as np

array1 = np.array([True, False, True, False])
array2 = np.array([False, True, True, False])

resultado_and = np.logical_and(array1, array2)
resultado_or = np.logical_or(array1, array2)

print("Resultado AND:", resultado_and)  # Imprime [False False  True False]
print("Resultado OR:", resultado_or)   # Imprime [ True  True  True False]
```

### Métodos Propios de Numpy

##### `.sum()`
La función `np.sum` calcula la suma de todos los elementos de un array.
```Python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

suma = np.sum(array)

print("Suma:", suma)  # Imprime 15
```

##### `.max()` y `.argmax()` 
Las funciones `np.max` y `np.argmax` de NumPy son herramientas útiles para trabajar con arrays y encontrar valores máximos, pero tienen propósitos distintos:
- La función `np.max` se utiliza para encontrar el valor máximo en un array NumPy.
	- Devuelve el valor máximo en sí.
```Python
import numpy as np

array = np.array([1, 5, 2, 8, 3])
max_valor = np.max(array)
print(max_valor)  # Imprime: 8
```

- La función `np.argmax` se utiliza para encontrar el índice del valor máximo en un array NumPy.
	- Devuelve el índice (posición) del valor máximo.
	- En caso de que haya múltiples valores máximos, `argmax` devuelve el índice del primero que encuentra.
```Python
import numpy as np

array = np.array([1, 5, 2, 8, 3])
indice_max = np.argmax(array)
print(indice_max)  # Imprime: 3 (porque el valor máximo 8 está en el índice 3)
```

##### `.copy()` 
La función `np.copy()` (de NumPy) se utiliza para crear una copia completa del array original, lo que significa que los datos se duplican en un nuevo espacio de memoria.
```Python
import numpy as np

array_original = np.array([1, 2, 3])
array_copia = np.copy(array_original)

array_copia[0] = 10  # Modificamos la copia

print(array_original)  # Imprime: [1 2 3] (el original no se modifica)
print(array_copia)  # Imprime: [10  2  3]
```

##### `.ptp()`
La función `ptp` de NumPy (abreviatura de "peak to peak") se utiliza para calcular la diferencia entre el valor máximo y el valor mínimo de un array. En otras palabras, te da el rango de los valores en tu array.
```Python
numpy.ptp(a, axis=None, out=None, keepdims=False)
```
- `a`: El array de entrada.
- `axis`: (Opcional) El eje a lo largo del cual se calcula el rango. Si no se especifica, se calcula el rango de todo el array.
- `out`: (Opcional) Un array alternativo en el que colocar el resultado. Debe tener la misma forma que el resultado esperado.
- `keepdims`: (Opcional) Si se establece en `True`, las dimensiones del array de resultado se conservarán como dimensiones con tamaño 1.

```Python
import numpy as np

array = np.array([1, 5, 2, 8, 3])
rango = np.ptp(array)
print(rango)  # Imprime: 7 (porque 8 - 1 = 7)
```

##### `.mean()`
La función `np.mean()` calcula la media aritmética (promedio) de los elementos de un array.
```Python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

media = np.mean(array)
print(media)  # Imprime: 3.0
```

##### `.std()`
La función `np.std()` calcula la desviación estándar de los elementos del array. La desviación estándar es una medida de cuánto se dispersan los valores alrededor de la media.
```Python
import numpy as np

array = np.array([1, 2, 3, 4, 5])

desviacion_estandar = np.std(array)
print(desviacion_estandar)  # Imprime: 1.4142135623730951
```

##### `.median()`
La función `np.median()` calcula la mediana de los elementos del array. La mediana es el valor central del conjunto de datos ordenado.
```Python
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7])

mediana = np.median(array)
print(mediana)  # Imprime: 4.0
```

##### `.percentile()`
La función `np.percentile(a:ndArray , b:int)` calcula el percentil `b` del array `a`. El percentil 75, por ejemplo, es el valor que separa el 75% inferior de los datos del 25% superior. El percentil 25 es el valor que separa el 25% inferior de los datos del 75% superior.
```Python
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7])

q75 = np.percentile(array, 75)
q25 = np.percentile(array, 25)

# El rango intercuartílico (IQR) se calcula restando el percentil 25 del 
# percentil 75. El IQR es una medida de la dispersión de los datos que es 
# menos sensible a los valores atípicos que la desviación estándar.
iqr = q75 - q25
print(iqr)  # Imprime: 3.0
```

### Parámetros `axis` y `out`

Se trata de argumentos opcionales que pueden utilizarse en algunas funciones (métodos) propios de NumPy. 

El **parámetro `axis`** especifica el eje sobre el que se realiza una operación. Los ejes de un array NumPy se indexan de la siguiente manera:
- `0` : Eje de las columnas (eje vertical).
- `1` : Eje de las filas (eje horizontal).
- `2` : Eje de profundidad (para arrays 3D).

El valor predeterminado de `axis` suele ser 0.

**Ejemplo.**
```Python
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

# Suma de los elementos a lo largo del eje 0 (filas)
suma_filas = np.sum(array, axis=0)
print(suma_filas) # Resultado: [5 7 9]

# Suma de los elementos a lo largo del eje 1 (columnas)
suma_columnas = np.sum(array, axis=1)
print(suma_columnas) # Resultado: [ 6 15]
```

El **parámetro `out`** permite especificar un array existente en el que se almacenará el resultado de una operación. Esto puede ser útil para evitar la creación de nuevos arrays y ahorrar memoria.
**Ejemplo.** 
```Python
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

# Se crea un nuevo array para almacenar el resultado
resultado = np.zeros_like(array)

# Se realiza la suma de los elementos y se almacena el resultado en 'resultado'
np.sum(array, axis=0, out=resultado)
print(resultado) # Resultado: [[5 7 9] [0 0 0]]
```

### Operaciones `all` y `any`

##### `.all()` 
La función `all` verifica si _todos_ los elementos de un array cumplen una condición específica. 
En un uso simple, devuelve `True` si todos los elementos son verdaderos (o evaluables como verdaderos); y `False` en caso contrario.
```Python
import numpy as np

array = np.array([True, True, True])

todos_verdaderos = np.all(array)

print("Todos verdaderos:", todos_verdaderos)  # Imprime True
```

Podemos darle uso mas sofisticados... Por ejemplo

**Verificación de rangos en un conjunto de datos**:
Imagina que tienes un array con medidas de temperatura y necesitas verificar si todas las temperaturas están dentro de un rango seguro (por ejemplo, entre 20°C y 30°C):
```Python
import numpy as np

temperaturas = np.array([22, 25, 28, 15, 29, 21])

rango_seguro = np.all((temperaturas >= 20) & (temperaturas <= 30))

if rango_seguro:
  print("Todas las temperaturas están dentro del rango seguro.")
else:
  print("Al menos una temperatura está fuera del rango seguro.")
```

##### `.any()` 
La función `any` verifica si _al menos uno_ de los elementos de un array cumple una condición específica.
En un uso simple, devuelve `True` si al menos un elemento es verdadero (o evaluable como verdadero), y `False` si ninguno lo es.
```Python
import numpy as np

array = np.array([False, False, True])

alguno_verdadero = np.any(array)

print("Alguno verdadero:", alguno_verdadero)  # Imprime True
```

Podemos darle uso mas sofisticados... Por ejemplo

**Búsqueda de patrones en datos**:
Imagina que tienes un array con datos de ventas y quieres saber si hubo algún día en el que todas las ventas superar:
```Python
import numpy as np

ventas = np.array([
    [150, 200, 180],
    [100, 120, 110],
    [220, 250, 200]
])

umbral = 150

dia_exitoso = np.any(np.all(ventas > umbral, axis=1))

if dia_exitoso:
  print("Hubo al menos un día en el que todas las ventas superaron el umbral.")
else:
  print("Ningún día tuvo todas las ventas por encima del umbral.")
```

### Arrays y Elecciones Aleatorias

NumPy cuenta con funcionalidades para trabajar de forma pseudo-aleatoria.

Para ello, primero debemos crear una instancia de RNG (*random number generator*)
```Python
import numpy as np

# Crear una instancia de RNG.
rng = np.random.default_rng()
```

Con la función `.choice` podemos hacer una elección aleatoria en un grupo finito de opciones.
```Python
import numpy as np

moneda:np.ndarray[str] = np.array(['cara', 'cruz'])

lanzamientos:np.ndarray[str] = rng.choice(moneda, size=10)
print(lanzamientos) 
''' Por ejemplo:
array(['cara', 'cara', 'cara', 'cruz', 'cara', 'cruz', 'cruz', 'cruz', 'cara', 'cara'])
'''
```
El parámetro `size` settea la cantidad de elecciones a hacer (determina la longitud del `npArray` de salida).

**Parámetro `replace`**
A este método también podemos pasarle el parámetro `replace`, se utiliza para especificar si los elementos pueden ser seleccionados repetidamente o no.
- `replace = True` (valor por defecto) : Los elementos pueden ser seleccionados repetidamente. Esto significa que un mismo elemento puede aparecer varias veces en la selección resultante.
- `replace = False` : Los elementos no pueden ser seleccionados repetidamente. Cada elemento solo puede aparecer una vez en la selección resultante.

```Python
import numpy as np

# Generar una selección aleatoria de 5 elementos del array [1, 2, 3, 4, 5] con
# reemplazo.
seleccion_con_reemplazo = np.random.choice([1, 2, 3, 4, 5], size=5, replace=True)
print("Selección con reemplazo:", seleccion_con_reemplazo)

# Generar una selección aleatoria de 5 elementos del array [1, 2, 3, 4, 5] sin
# reemplazo.
seleccion_sin_reemplazo = np.random.choice([1, 2, 3, 4, 5], size=5, replace=False)
print("Selección sin reemplazo:", seleccion_sin_reemplazo)
```

### Arrays Multi-Dimensionales 

Además de vectores, con NumPy podemos manejar arreglos multi-dimensionales a partir de `arrays` anidados.

Veamos algunas matrices :
```Python
import numpy as np 

A = np.array([[3, 2, 2], [-1, 0, 1], [-2, 2, 4]])
B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
C = np.array([[0, 1, -1], [5, -2, 1]])

print(A)
'''Por ejemplo, imprime:
[ 3 2 2
 -1 0 1 
 -2 2 4 ]
'''

# También podemos realizar operaciones entre matrices.
suma = A + B
print(suma)
''' Imprime
[ 4 2 2 
 -1 1 1 
 -2 2 5 ]
'''
```

##### Indexación
**Indexar** elementos de un arreglo multi-dimensional : 
Por ejemplo -> para una matriz, siendo `x` la *fila* e `y` la *columna* ...
- `a[x][y]` 
- `a[x, y]` 

También podemos acceder a una fila/columna completa, en forma directa.
- Para **acceder a una fila completa**, se utiliza la indexación de array con un solo índice. El índice que proporciones corresponderá al número de fila (empezando desde 0).
```Python
import numpy as np

# Crear un array 2D de ejemplo
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Acceder a la primera fila (índice 0)
primera_fila = matriz[0]
print("Primera fila:", primera_fila)  # Output: [1 2 3]

# Acceder a la segunda fila (índice 1)
segunda_fila = matriz[1]
print("Segunda fila:", segunda_fila)  # Output: [4 5 6]
```

- Para **acceder a una columna completa**, puedes utilizar la indexación de array con dos índices. El primer índice debe ser `:` (dos puntos) para indicar que quieres seleccionar todas las filas, y el segundo índice debe ser el número de columna (empezando desde 0).
```Python
# Acceder a la primera columna (índice 0)
primera_columna = matriz[:, 0]
print("Primera columna:", primera_columna)  # Output: [1 4 7]

# Acceder a la segunda columna (índice 1)
segunda_columna = matriz[:, 1]
print("Segunda columna:", segunda_columna)  # Output: [2 5 8]
```

##### Traspuesta de una Matriz
NumPy provee dos formas de obtener, en forma directa y eficiente, una matriz traspuesta.
- Método `.T` -> Este atributo devuelve una vista de la matriz original con las filas y columnas intercambiadas.
- Función `transpose()` -> También puedes utilizar la función `np.transpose()` para obtener la matriz transpuesta. Esta función acepta la matriz original como argumento y devuelve una nueva matriz con las filas y columnas intercambiadas.

```Python
import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matriz original:")
print(matriz)

# Utilizando .T
matriz_transpuesta_T = matriz.T
print("\nMatriz transpuesta (con .T):")
print(matriz_transpuesta_T)

# Utilizando np.transpose()
matriz_transpuesta_transpose = np.transpose(matriz)
print("\nMatriz transpuesta (con np.transpose()):")
print(matriz_transpuesta_transpose)

'''
OutPut:
Matriz original: 
[[1 2 3] 
 [4 5 6] 
 [7 8 9]] 
 
Matriz transpuesta (con .T): 
[[1 4 7] 
 [2 5 8] 
 [3 6 9]] 

Matriz transpuesta (con np.transpose()): 
[[1 4 7] 
 [2 5 8] 
 [3 6 9]]
'''
```


##### Producto Matricial
El producto entre matrices está definido en NumPy. Se realiza con el operador `@`.
- Como en todo producto de matrices, debe cumplirse la Condición del Producto de Matrices: en `a@b`, si el número de **columnas de `a` no es igual** al número de **filas de `b`**, lanza una **excepción**.

```Python
import numpy as np

a = np.array([[3, 2, 2], [-1, 0, 1], [-2, 2, 4]])
c = np.array([[0, 1, -1], [5, -2, 1]])

producto_1 = a @ c
# Excepción: No se cumple la Condición de Producto de Matrices.

producto_2 = c @ a
print(producto_2)

'''
OutPut: 
[[ 1 -2 -3]
 [15 12 12]]
'''
```

**Fin.** 
