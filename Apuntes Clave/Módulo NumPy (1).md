Importar la librería -> `import numpy as np`

> [!NOTE]
> A los *arrays* de *numpy* los llamamos *nparrays*.

**Crear un NpArray a partir de una lista**
```Python
lista1 = [31,28,29,19]

arr = np.array(lista1)

# Mismo comando sirve para crear arreglos de matrices.
matriz1 = [[2,3,4],[5,6,7],[8,9,10],[22,25,78]]

arr_2 = np.array(matriz1)
```

Sea `arr` una variable de tipo `array numpy`...
**Verificar dimensiones del NpArray**
```Python
arr.shape
# Devuelve una tupla (filas,columnas) según la dimensión del nparray 'arr'.

# Ejemplo: arr = [[2,3,4],[3,4,5],[3,4,5],[2,2,2]]
print(arr.shape)   # Imprime '(4,3)'


arr.ndim
# Devuelve un número (entero) que indica la dimensión del nparray 'arr'.

# Ejemplo: arr = [[2,3,4],[3,4,5],[3,4,5],[2,2,2]]
print(arr.dim)   # Imprime '3'
```

**Verificar el tipo de dato de un NpArray**
```Python
arr.dtype
# Devuelve el tipo (de dato) de los elementos que almacena el nparray 'arr'. 

# Ejemplo: arr = [[2,3,4],[3,4,5],[3,4,5],[2,2,2]]
print(arr.dtype)   # Imprime 'dtype('int32')'
```

**Longitud de un NpArray**
```Python
arr.size
# Devuelve un número (entero) con la cantidad de elementos del nparray 'arr'.

# Ejemplo: arr = [[2,3,4],[3,4,5],[3,4,5],[2,2,2]]
print(arr.size)   # Imprime '12'
```

**Especificar el tipo de dato de un NpArray**
```Python
lista1 = [[2,3,4],[3,4,5],[3,4,5],[2,2,2]]

arr = np.array(lista1 , dtype = np.int16)
# En la variable 'arr' crea un nparray con los datos de la variable lista (pasada
# como argumento) pero especificandole el tipo de dato con el que quiero que se
# almacene. Si no especifico el tipo de dato, el default es 'int32'.
```

**Crear una matriz de ceros**
```Python
matriz_vacia = np.zeros((3,2))
# Crea una matriz en la variable 'matriz_vacia' de tamaño 3x2 donde todos los 
# elementos son ceros.

print(matriz vacía)   # Imprime '[[0,0],[0,0],[0,0]]'
```

**Crear una matriz de unos**
```Python
matriz_pseudo_vacia = np.ones((3,3))
# Crea una matriz en la variable 'matriz_pseudo_vacia' de tamaño 3x3 donde todos
# los elementos son 1.
```

**Crear una matriz de un mismo elemento**
```Python
matriz_7 = np.full((2,3),7)
# Crea una matriz de tamaño 2x3 donde todos los elementos son 7.
```

**Crear un NpArray con los números del 0 al 15**
```Python
arr = np.arange(16)
# Crea un nparray (de dimensión 1) con los números del 0 (porque python empieza a 
# contar desde el índice cero) al 15.
# ¿Por qué le paso como argumento '16' y no '15'? Porque la lectura es "hasta el
# 16 exclusive".

print(arr)   # Imprime '[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]'
```

**Crear un NpArray con los números del 10 al 20 con saltos**
```Python
arr = np.arange(10,21,2)
# Crea un nparray (de dimesión 1) con los números del 10 al 20 de a dos en dos.
# ¿Por qué le paso como argumento '21' y no '20'? Porque la lectura es "hasta el
# 21 exclusive".

print(arr)   # Imprime '[10,12,14,16,18,20]'
```

**Crear un NpArray con 20 números del 10 al 16**
```Python
arr = np.linspace(10,16,20)
# Crea un nparray (de dimensión 1) con 20 números entre el 10 y el 16.
# Toma el rango y divide equitativamente para poder darte la cantidad de números
# que le pedis en el rango que le señalas.
```

**Operaciones entre NpArrays**
```Python
a = np.array([2,2,7,8,1,1])
b = np.array([4,2,1,3,1,7])

# Sumar nparrays: suma elementos de posiciones iguales.
c = a + b
print(c)   # Imprime '[6,4,8,11,2,8]'
# Misma sintaxis con '-','*','/','%' y '**'. De igual forma, trabaja con elementos
# de posiciones iguales.

# Concatenar dos nparrays en uno.
d = np.concatenate((a,b))
print(d)   # Imprime '[2,2,7,8,1,1,4,2,1,3,1,7]'
``` 

**Ordenar elementos numéricos de un NpArray**
```Python
arr = np.array([10,5,7,2,1,9,25])

arr.sort()   # Ordena los elementos de menor a mayor.

print(arr)   # Imprime '[1,2,5,7,9,10,25]'
```

**NpArrays con números aleatorios**
```Python
arr_aleatorios = np.random.rand(25)
# Crea un nparray con 25 números aleatorios.

arr_aleatorios2 = np.random.rando(2,3,4)
# Crea un nparray con 2 matrices de 3 filas y 4 columnas con valores aleatorios.
```

```Python
rg = np.random.default_rng(2)
# Este comando lo que hace es configurar la distribución de valores según el
# argumento que le pase (en este caso '2').

# A partir de ahora, para trabajar con aleatoriedad, no llamo a 'np' sino a 'rg'.

aleatorios = rg.random(1000)
# Crea un nparray de mil números aleatorios (de la semilla 2).

enteros_aleatorios = rg.integers(20 , size = 2000)
# Crea un nparray con 2000 números aleatorios que van desde el 0 al 20 (exclusive).

sin_repetidos = rg.choice(26 , size = 10 , replace = False )
# Crea un nparray de 10 números que van desde el 0 al 26 (exclusive) sin repetidos.
```

>[!NOTE]
>¿Para qué sirve configurar la distribución (o semilla de generación)? Para lograr repruducibilidad de los resultados. Basicamente, cada vez que generamos número al azar con semilla 2 (por ejemplo), van a ser aleatorios pero siempre los mismos. De esta forma, usuarios distintos pueden obtener mismos resultados desde distintos códigos con los mismos números aleatorios.

**Funciones estadísticas básicas**
```Python
ejemplo = np.array([2,5,1,8,4,7,15])

valor_minimo = ejemplo.min()
# Valor mínimo del nparray.
print(valor_minimo)   # Imprime '1'

valor_maximo = ejemplo.max()
# Valor máximo del nparray.
print(valor_maximo)   # Imprime '15'

promedio = ejemplo.mean()
# Valor promedio del nparray.
print(promedio)   # Imprime '6'

des_estandar = ejemplo.std()
# Valor de la desviación estándar del nparray.

suma_total = ejemplo.sum()
# Suma de todos los elementos del nparray.
print(suma_total)   # Imprime '42'
```

Cambiamos el ejemplo a una matriz.
```Python
ejemplo = np.array([[6,7,11,8],
				    [13,14,0,0],
				    [5,10,1,2],
				    [18,16,14,2]])

valor_minimo = ejemplo.min(axis = 0)
# Crea un nparray con el valor mínimo de cada columna.
print(valor_minimo)   # Imprime '[5,8,0,0]'

valor_maximo = wjwmplo.max(axis = 1)
# Crea un nparray con el valor máximo de cada fila.
print(valor_maximo)   # Imprime '[11,14,19,10,18]'
```

> [!NOTE]
> `axis = 0` -> columnas.
> `axis = 1` -> filas.

**Filtrar datos**
Lo muestro con algunos ejemplo.
```Python
ejemplo = np.array([[6,7,11,8],
				    [13,14,0,0],
				    [5,10,1,2],
				    [18,16,14,2]])

matriz_booleana = ejemplo < 12
# Devuelve una matriz con booleanos según se cumpla o no la condición en cada dato.
print(matriz_booleana)   # Imprime ([[True,True,True,True],
				         #           [False,False,True,True],
						 #		     [True,True,True,True],
						 #		     [False,False,False,True]])

a = ejemplo[ejemplo < 12]
# Devuelve un nparray con los elementos (de toda la matriz) que cumplan la 
# condición especificada.
print(a)   # Imprime 'array([6,8,11,8,0,0,8,10,5,10,1,2,2])'
```

**Pegar NpArrays en forma vertical y horizontal**
```Python
n1 = np.array([[19,19,15],
			   [19,15,10],
			   [15,16,5]])

n2 = np.array([[9,18,14],
			   [7,19,17],
			   [8,11,2]])

pegar_vertical = np.vstack((np1 , np2))
# Pega dos nparrays en forma vertical.
print(pegar_vertical)   # Imrpime array([[19,19,15],
			            #                [19,15,10],
			            #                [15,16,5],
			            #                [9,18,14],
			            #                [7,19,17],
			            #                [8,11,2]])

pegar_horizontal = np.hstack((np1 , np2))
# Pega dos nparrays en forma horizontal.
print(pegar_horizontal)   # Imprime array([[19,19,15,9,18,14],
			              #                [19,15,10,7,19,17],
			              #                [15,16,5,8,11,2]])
```

**Seleccionar datos de un arreglo**
```Python
aa = np.array([0,14,8,19,3,4,1,8,15,15])

recorte = aa[0:6]
# Crea un nuevo nparray con los elementos entre índices 0 y 6.
print(recorte)   # Imprime 'array([0,14,8,19,3,4])'

recorte_condicionado = aa[0:6:2]
# Crea un nuevo nparray con los elementos entre índices 0 y 6 con saltos de a 2.
print(recorte_condicionado)   # Imprime 'array([0,8,3])'

recorte_condicionado_2 = aa[::2]
# Crea un nuevo nparray tomando elementos de a saltos de a 2.
```

Cambio el ejemplo :
```Python
bb = np.array([[4,3,8,8,12],     # fila 0
			   [8,19,8,19,5],    # fila 1
			   [2,13,0,4,10],    # fila 2
			   [6,10,9,0,4],     # fila 3
			   [2,18,15,1,8],    # fila 4
			   [17,17,16,1,15],  # fila 5
			   [1,13,4,5,5],     # fila 6
			   [16,0,4,7,3]])    # fila 7

elemento_particular = bb[1,3]
# Agarra el dato ubicado en la segunda fila (o el sub-nparray 2) columna 3
# (recordar que las columnas también se cuentan desde el cero).
# El prime argumento corresponde a la fila, el segundo a la columna (dentro de esa
# fila).
print(elemento_particular)   # Imprime '19'

elementos_seleccionados = bb[3:6,1]
# Crea un nparray con los segundos elementos (columna índice 1) de las filas 3,4 y 
# 5 (recordar que siempre la cota superior es excluyente).
print(elementos_seleccionados)   # Imprime 'array([10,18,17])'

sub_matriz = bb [4:7,0:2]
# Crea otra matriz con los primeros dos elementos de las filas 4,5 y 6.
# Nuevamente, el primer argumento corresponde a las filas, el segundo argumento a
# las columnas.
print(sub_matriz)   # Imprime array([[2,18],
                    #                [17,17],
                    #                [1,13]])
```

