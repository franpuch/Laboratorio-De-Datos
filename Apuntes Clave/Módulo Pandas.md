# Apuntes de `Pandas`

Importar `Pandas` en el archivo a trabajar.
```Python
import pandas as pd
```

### Typado de Variables 

A la hora de crear variables que almacenen `pdDataFrames` (DataFrames de Pandas), las puedo _typar_ con el siguiente tag
```Python
v:pd.DataFrame   
# 'v' es una variable que almacena un DataFrame de Pandas.
```

##### Formas de Consultar Tipos de Datos

```Python
import pandas as pd

data:dict[str,list] = {
	'Genero': ['M', 'F', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'F'],
	'Edad': [8, 18, 16, 27, 13, 34, 37, 23, 27, 35],
	'Altura_cm': [126.0, 159.0, 171.0, 157.0, 181.0, 159.0, 170.0, 171.0, 193.0, 163.0],
	'Peso_kg': [24.0, 61.0, 69.0, 88.0, 63.0, 59.0, 57.0, 84.0, 82.0, 61.0]
}

df:pd.DataFrame = pd.DataFrame(data)

print(type(df))
# Consultar el tipo de dato de la varible 'df'
# OutPut -> <class 'pandas.core.frame.DataFrame'>

print(df.dtypes)
# Consulta el tipo de dato de cada una de las columnas del DataFrame.
# OutPut: 
#    Genero        object
#    Edad           int64
#    Altura_cm    float64
#    Peso_kg      float64
#    dtype: object

print(df)
# Imprime el DataFrame completo
'''
OutPut: 
  Genero  Edad  Altura_cm  Peso_kg
0      M     8      126.0     24.0
1      F    18      159.0     61.0
2      M    16      171.0     69.0
3      M    27      157.0     88.0
4      M    13      181.0     63.0
5      F    34      159.0     59.0
6      M    37      170.0     57.0
7      M    23      171.0     84.0
8      M    27      193.0     82.0
9      F    35      163.0     61.0
'''
```

### Operaciones Básicas

Sea `df` el siguiente DataFrame
```Python
import pandas as pd

data:dict[str,list] = {
	'Genero': ['M', 'F', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'F'],
	'Edad': [8, 18, 16, 27, 13, 34, 37, 23, 27, 35],
	'Altura_cm': [126.0, 159.0, 171.0, 157.0, 181.0, 159.0, 170.0, 171.0, 193.0, 163.0],
	'Peso_kg': [24.0, 61.0, 69.0, 88.0, 63.0, 59.0, 57.0, 84.0, 82.0, 61.0]
}

df:pd.DataFrame = pd.DataFrame(data)

print(df)
'''
OutPut: 
  Genero  Edad  Altura_cm  Peso_kg
0      M     8      126.0     24.0
1      F    18      159.0     61.0
2      M    16      171.0     69.0
3      M    27      157.0     88.0
4      M    13      181.0     63.0
5      F    34      159.0     59.0
6      M    37      170.0     57.0
7      M    23      171.0     84.0
8      M    27      193.0     82.0
9      F    35      163.0     61.0
'''
```

El mismo DataFrame lo podemos crear de otras formas:
- Desde una lista de de diccionarios
```Python
data = [
	{"Genero": "M", "Edad": 30, "Altura_cm": 177.0, "Peso_kg": 88.0},
	{"Genero": "F", "Edad": 18, "Altura_cm": 159.0, "Peso_kg": 61.0},
	{"Genero": "M", "Edad": 16, "Altura_cm": 171.0, "Peso_kg": 69.0},
	# y asi con todos
]

df = pd.DataFrame(data)
```

- Desde un array bi-dimensional de `NumPy` y una lista de columnas
```Python
data = np.array([
	['M', 30, 177.0, 88.0],
	['F', 18, 159.0, 61.0],
	['M', 16, 171.0, 69.0],
	# y asi con todos
])

pd.DataFrame(data, columns=['Genero', 'Edad', 'Altura_cm', 'Peso_kg'])
```

##### Cantidad de Filas de un DataFrame
Hay que utilizar la función `len()` de Python.
```Python
nro_filas:int = len(df)

print(nro_filas)   # OutPut -> 10
```

##### Atributo `attrs` 
El atributo `attrs` de un DataFrame es un diccionario que te permite adjuntar meta-datos arbitrarios a tu DataFrame. Estos meta-datos pueden ser cualquier información que desees asociar con tus datos, como la fuente de los datos, el autor, la fecha de creación, o cualquier otra información relevante que desees acompañe al DataFrame.
```Python
df.attrs["Materia"] = "Laboratorio de Datos"
df.attrs["Bloque"] = 1
df.attrs["Clase"] = 2
df.attrs["Fuente"] = "Arial 11"

print(df.attrs)
# OutPut -> {'Materia': 'Laboratorio de Datos', 'Bloque': 1, 'Clase': 2, 'Fuente': 'Arial 11'}
```

##### Atributos de `NumPy` 
A un DataFrame de `Pandas` se le pueden consultar los siguientes atributos de `NumPy`
- `.ndim`
- `.shape` 

```Python
print(df.ndim)   # OutPut -> 2
# Coherente: filas y columnas.

print(df.shape)   # OutPut -> (10, 4)
# 10 filas, 4 columnas.
```

##### Atributos Propios de `Pandas` 
Atributos de los DataFrames 
- `.columns` -> retorna un iterable con todas las columnas.
```Python
print(df.columns)
# OutPut -> Index(['Genero', 'Edad', 'Altura_cm', 'Peso_kg'], dtype='object')

print(df.columns[2])
# OutPut -> Altura_cm
```

- `.values` -> retorna una lista de listas, donde cada lista corresponde a los datos de cada fila. Al ser una doble lista, es un doblemente iterable.
```Python
print(df.values)
''' OutPut
[['M' 8 126.0 24.0]
 ['F' 18 159.0 61.0]
 ['M' 16 171.0 69.0]
 ['M' 27 157.0 88.0]
 ['M' 13 181.0 63.0]
 ['F' 34 159.0 59.0]
 ['M' 37 170.0 57.0]
 ['M' 23 171.0 84.0]
 ['M' 27 193.0 82.0]
 ['F' 35 163.0 61.0]]
'''

print(df.values[1]) 
# OutPut -> ['F' 18 159.0 61.0]

print(df.values[1][3])
# OutPut -> 61.0
```

### Métodos de un `DataFrame` de `Pandas`

Sea `df` el siguiente DataFrame
```Python
import pandas as pd

data:dict[str,list] = {
	'Genero': ['M', 'F', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'F'],
	'Edad': [8, 18, 16, 27, 13, 34, 37, 23, 27, 35],
	'Altura_cm': [126.0, 159.0, 171.0, 157.0, 181.0, 159.0, 170.0, 171.0, 193.0, 163.0],
	'Peso_kg': [24.0, 61.0, 69.0, 88.0, 63.0, 59.0, 57.0, 84.0, 82.0, 61.0]
}

df:pd.DataFrame = pd.DataFrame(data)

print(df)
'''
OutPut: 
  Genero  Edad  Altura_cm  Peso_kg
0      M     8      126.0     24.0
1      F    18      159.0     61.0
2      M    16      171.0     69.0
3      M    27      157.0     88.0
4      M    13      181.0     63.0
5      F    34      159.0     59.0
6      M    37      170.0     57.0
7      M    23      171.0     84.0
8      M    27      193.0     82.0
9      F    35      163.0     61.0
'''
```

##### `.head()`
**`head(n)`** -> Muestra las primeras `n` filas del DataFrame. Por defecto, `n` es 5, por lo que si llamas a `df.head()`, se mostrarán las primeras 5 filas.
```Python
# Mostrar las primeras 3 filas. 
print(df.head(3))
```

##### `.tail()` 
**`tail(n)`** -> Muestra las últimas `n` filas del DataFrame. Al igual que `head()`, el valor predeterminado de `n` es 5.
```Python
# Mostrar las últimas 2 filas.
print(df.tail(2))
```

##### `.describe()` 
**`describe()`** -> Retorna un DataFrame con estadísticas descriptivas para las columnas numéricas del DataFrame. Estas estadísticas incluyen:
	- **count:** Número de valores no nulos en cada columna.
	- **mean:** Media aritmética de los valores en cada columna.
	- **std:** Desviación estándar de los valores en cada columna.
	- **min:** Valor mínimo en cada columna.
	- **25%:** Percentil 25 de los valores en cada columna.
	- **50%:** Percentil 50 (mediana) de los valores en cada columna.
	- **75%:** Percentil 75 de los valores en cada columna.
	- **max:** Valor máximo en cada columna.
```Python
print(df.describe())

''' OutPut
            Edad   Altura_cm    Peso_kg
count  10.000000   10.000000  10.000000
mean   23.800000  165.000000  64.800000
std     9.919677   17.632042  18.292682
min     8.000000  126.000000  24.000000
25%    16.500000  159.000000  59.500000
50%    25.000000  166.500000  62.000000
75%    32.250000  171.000000  78.750000
max    37.000000  193.000000  88.000000
'''
```

##### `.info()`
**`info()`** -> Retorna un DataFrame con un resumen conciso de la información del DataFrame, incluyendo:
	- Número de filas y columnas.
	- Nombre de las columnas.
	- Tipo de dato de cada columna.
	- Número de valores no nulos en cada columna.
	- Uso de memoria del DataFrame.
```Python
print(df.info())

''' OutPut
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 4 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Genero     10 non-null     object 
 1   Edad       10 non-null     int64  
 2   Altura_cm  10 non-null     float64
 3   Peso_kg    10 non-null     float64
dtypes: float64(2), int64(1), object(1)
memory usage: 452.0+ bytes
None
'''
```

##### `.to_numpy()`
**`to_numpy()`** -> Retorna un `npArray` del DataFrame. Convierte el DataFrame en un array de NumPy.
	- Obs -> En algunos casos, el array resultante puede ser una vista del DataFrame original, lo que significa que los cambios en el array también afectarán al DataFrame y viceversa. Para evitar esto, puedes usar `df.to_numpy(copy=True)` para asegurarte de obtener una copia independiente del array.
```Python
print(df.to_numpy())

''' OutPut
[['M' 8 126.0 24.0]
 ['F' 18 159.0 61.0]
 ['M' 16 171.0 69.0]
 ['M' 27 157.0 88.0]
 ['M' 13 181.0 63.0]
 ['F' 34 159.0 59.0]
 ['M' 37 170.0 57.0]
 ['M' 23 171.0 84.0]
 ['M' 27 193.0 82.0]
 ['F' 35 163.0 61.0]]
'''
```

##### `.query()`
**`query()`** -> Permite filtrar filas de un DataFrame utilizando una expresión booleana en forma de `str`. Esta expresión se evalúa para cada fila del DataFrame, y solo las filas que cumplen con la condición especificada se incluyen en el resultado.
```Python
# Sintaxis Básica
df.query('expresión')

# Ejemplo 1 -> Filtrar por una condición 

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 22, 28, 24],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']}
df = pd.DataFrame(data)

# Seleccionar las filas donde la edad es mayor a 25
result = df.query('Age > 25')
print(result)

# Ejemplo 2 -> Filtrar por múltiples condiciones

# Seleccionar las filas donde la edad es mayor a 25 y la ciudad es 'New York' 
result = df.query('Age > 25 and City == "New York"') 
print(result)

# Ejemplo 3 -> Usar variables en la expresión

edad_minima = 25
ciudad = "New York"
result = df.query(f'Age > @edad_minima and City == @ciudad')
print(result)

# Ejemplo 4 -> Usar funciones en la expresión

# Seleccionar las filas donde la longitud del nombre es mayor a 5
result = df.query('Name.str.len() > 5')
print(result)
```

##### `.iterrows()`
**`iterrows()`** -> Se utiliza para iterar sobre las filas de un DataFrame, devolviendo un iterador que produce una tupla para cada fila. Esta tupla contiene dos elementos: **Índice** (el índice de la fila) y **Serie** (una Serie de Pandas que contiene los datos de la fila).
```Python 
# Sintaxis Básica.
for indice, fila in df.iterrows():
    # Aquí puedes acceder a los datos de cada fila
    print(indice)  # Imprime el índice de la fila
    print(fila)  # Imprime la Serie con los datos de la fila
    # Puedes acceder a valores individuales de la fila usando el índice de la columna
    print(fila['nombre_columna'])
```

```Python
# Ejemplo Práctico.
import pandas as pd

data = {'nombre': ['Alice', 'Bob', 'Charlie'],
        'apellido': ['Smith', 'Johnson', 'Williams'],
        'edad': [25, 30, 22]}
df = pd.DataFrame(data)

df['nombre_completo'] = ''  # Crear una columna vacía para el nombre completo.

for indice, fila in df.iterrows():
    nombre_completo = fila['nombre'] + ' ' + fila['apellido']
    df.loc[indice, 'nombre_completo'] = nombre_completo  # Asignar el nombre completo a la nueva columna

print(df)
```

> [!NOTE]
> `iterrows()` puede ser lento para DataFrames grandes, ya que crea una Serie para cada fila.

##### `.agg()` 
**`agg()`** -> se utiliza para realizar *operaciones de agregación* en Series o DataFrames. Esto significa que puedes aplicar una o varias funciones a tus datos para resumirlos o calcular estadísticas.
- **Aplicar múltiples funciones de agregación a la vez:** Puedes calcular varias estadísticas (como la media, la mediana, la suma, etc.) en una sola llamada a `agg()`.
- **Aplicar diferentes funciones a diferentes columnas:** Puedes especificar qué funciones aplicar a cada columna de un DataFrame.
- **Aplicar funciones personalizadas:** Puedes usar funciones definidas por el usuario para realizar cálculos específicos.
- **Trabajar con datos agrupados:** `agg()` se usa a menudo junto con `groupby()` para realizar cálculos de agregación en grupos de datos.

Sintaxis General :
```Python
resltados = df.agg(dict)
print(resultados)
```
Donde `dict` es un diccionario cuyas claves son las columnas (a las que quiero aplicarles operaciones) y valores son listas con las operaciones (que quiero aplicarle a cada columna).
**Tanto las claves como los valores se pasan como `str`**.

**Ejemplo 1** : Calcular funciones integradas a determinadas columnas.
```Python
datos = df.agg({'Altura_cm':['mean', 'median'], 'Peso_kg':['mean', 'median']})
print(datos)

''' OutPut
       Altura_cm  Peso_kg
mean        165.0     64.8
median      166.5     62.0
'''
```

> [!NOTE]
> No sólo podemos pasar funciones integradas. También podemos pasar (dentro de la lista de funciones) funciones propias definidas por nosotros. Se pasan de igual forma que las integradas: como `str` dentro de la lista.

##### `.groupby()`
**`groupby()`** -> es una herramienta fundamental para **agrupar datos** en un DataFrame según los valores de una o más columnas.
- **Dividir datos:** Separa tus datos en grupos basados en los valores de una o más columnas.
- **Aplicar funciones:** Puedes aplicar funciones de agregación (como suma, promedio, conteo, etc.) o funciones personalizadas a cada grupo (con `.agg()`).
- **Transformar datos:** Puedes transformar los datos dentro de cada grupo utilizando funciones personalizadas.
- **Filtrar datos:** Puedes filtrar grupos basados en ciertas condiciones.

Sintaxis General : 
```Python
grupo = df.groupby(agrupador)

# 'agrupador' es el nombre de la columna por la que se quiere agrupar.
# 'agrupador' debe ser un string.

print(grupo)   
# OutPut -> <pandas.core.groupby.generic.DataFrameGroupBy object at 0x77d19a3e5cd0>

# Si quiero imprimir y ver el grupo, debo iterar sobre él e ir imprimiendo de
# a poco. Revisar ejemplos de más abajo.
```

**Ejemplo 1** : Iterar sobre el grupo definido.
```Python
# Agrupo por la columna 'Género'.
genero_M = df.groupby('Genero')

# Ahora quiero iterar sobre los grupos formados para ver el contenido de cada
# uno.
for nombre_grupo, datos_grupo in genero_M :
	print(f"Grupo: {nombre_grupo}")
	print(datos_grupo)

''' OutPut
Grupo: F
  Genero  Edad  Altura_cm  Peso_kg
1      F    18      159.0     61.0
5      F    34      159.0     59.0
9      F    35      163.0     61.0
Grupo: M
  Genero  Edad  Altura_cm  Peso_kg
0      M     8      126.0     24.0
2      M    16      171.0     69.0
3      M    27      157.0     88.0
4      M    13      181.0     63.0
6      M    37      170.0     57.0
7      M    23      171.0     84.0
8      M    27      193.0     82.0
''' 
```

**Ejemplo 2** : Agrupar por una columna y aplicar una función.
```Python
promedio_alturas = df.groupby('Genero')['Altura_cm'].mean()
print('Promedio Altura Por Género: ', promedio_alturas)

''' OutPut
Promedio Altura Por Género:  Genero
F    160.333333
M    167.000000
Name: Altura_cm, dtype: float64
'''

promedio_pesos = df.groupby('Genero')['Peso_kg'].mean()
print('Promedio Peso Por Género: ', promedio_pesos)

'''OutPut
Promedio Peso Por Género:  Genero
F    60.333333
M    66.714286
Name: Peso_kg, dtype: float64
'''
```

**Ejemplo 3** : Agrupar por múltiples columnas y aplicar una función.
```Python
data = {'Grupo1': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Grupo2': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Valor': [10, 12, 15, 18, 20, 22]}
df = pd.DataFrame(data)

# Agrupar por las columnas 'Grupo1' y 'Grupo2' y calcular el promedio de 'Valor'
resultado = df.groupby(['Grupo1', 'Grupo2'])['Valor'].mean()

print(resultado)
```

No solo podemos agrupar por columnas, también **podemos agrupar por condiciones que nosotros armemos**. No es tan directo, pero `.groupby()` nos facilita mucho la tarea.

**Ejemplo 4** : Agrupar utilizando una columna booleana.
```Python
'''
La idea es crear una nueva columna donde si esa fila cumple determinada
condición, hay un 'True'; sino, un 'False'. 
Luego, agrupamos por esa columna.
'''

import pandas as pd

data = {'Grupo': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Valor': [10, 15, 12, 18, 20, 25]}
df = pd.DataFrame(data)

# Crear una columna booleana para una condición (por ejemplo, 'Valor' > 15)
df['Condicion'] = df['Valor'] > 15

# Agrupar por la columna booleana y calcular la suma
resultado = df.groupby('Condicion')['Valor'].sum()

print(resultado)
```

**Ejemplo 5** : Agrupar utilizando una columna de cumplimiento.
```Python
'''
La idea es la misma que antes, solo que ahora en vez de booleanos, el valor es
algo más categórico (como 'Cumple' y 'No Cumple').
'''

import numpy as np

# Crear una columna nueva basada en la condición
df['Cumplimiento'] = np.where(df['Valor'] > 15, 'Cumple', 'No Cumple')

# Agrupar por la columna nueva y calcular la suma
resultado = df.groupby('Cumplimiento')['Valor'].sum()

print(resultado)
```

**Ejemplo 6** : Usar `.apply()` para crear grupos personalizados.
```Python
def asignar_grupo(fila):
    if fila['Valor'] > 20:
        return 'Grupo Alto'
    elif fila['Valor'] > 15:
        return 'Grupo Medio'
    else:
        return 'Grupo Bajo'

# Crear una columna nueva con los grupos asignados
df['Grupo_Personalizado'] = df.apply(asignar_grupo, axis=1)

# Agrupar por la columna nueva y calcular la suma
resultado = df.groupby('Grupo_Personalizado')['Valor'].sum()

print(resultado)
``` 

##### `.to_csv()`
**`to_csv()`** -> Exportar un DataFrame de Pandas a un archivo CSV.

```Python
df.to_csv('nombre_archivo.csv', index=True, sep=',', encoding='utf-8')
```
- `'nombre_archivo.csv'`: Es el nombre del archivo CSV que se creará. Puedes incluir la ruta completa si deseas guardar el archivo en una ubicación específica.
- `index=True`: Indica si se debe incluir el índice del DataFrame en el archivo CSV. Si no quieres incluir el índice, establece este parámetro en `False`.
- `sep=','`: Define el separador de columnas en el archivo CSV. Por defecto, es una coma (`,`), pero puedes usar otros separadores como punto y coma (`;`) o tabulaciones (`\t`).
- `encoding='utf-8'`: Especifica la codificación de caracteres que se utilizará en el archivo CSV. `utf-8` es una codificación común que admite una amplia gama de caracteres.

##### `.to_json()`
**`to_json()`** -> Exportar un DataFrame de Pandas a un archivo JSON.

```Python
df.to_json('nombre_archivo.json', orient='records', indent=4)
```
- `'nombre_archivo.json'`: Es el nombre del archivo JSON que se creará. Puedes incluir la ruta completa si deseas guardar el archivo en una ubicación específica.
- `orient='records'`: Define el formato de los datos en el archivo JSON. `'records'` es una opción común que guarda cada fila del DataFrame como un objeto JSON dentro de una lista. Otras opciones incluyen `'index'`, `'columns'`, `'values'`, `'split'`, y `'table'`.
- `indent=4`: Especifica el número de espacios que se utilizarán para la indentación en el archivo JSON. Esto hace que el archivo sea más legible. Si no deseas indentación, puedes omitir este parámetro o establecerlo en `None`.

##### `.to_excel()`
**`to_excel()`** -> Exportar un DataFrame de Pandas a un archivo Excel.

> [!IMPORTANT]
> Este método requiere la librería `openpyxl` para escribir archivos Excel, así que asegúrate de tenerla instalada (`pip install openpyxl`).

```Python
df.to_excel('nombre_archivo.xlsx', sheet_name='Hoja1', index=True, engine='openpyxl')
```
- `'nombre_archivo.xlsx'`: Es el nombre del archivo Excel que se creará. Puedes incluir la ruta completa si deseas guardar el archivo en una ubicación específica.
- `sheet_name='Hoja1'`: Especifica el nombre de la hoja de cálculo en el archivo Excel.
- `index=True`: Indica si se debe incluir el índice del DataFrame en el archivo Excel. Si no quieres incluir el índice, establece este parámetro en `False`.
- `engine='openpyxl'`: Especifica el motor que se utilizará para escribir el archivo Excel. En este caso, estamos usando `openpyxl`. 

##### `pd.read_csv()`
**`pd.read_csv()`** -> Leer un archivo CSV y generar un DataFrame a partir de sus datos.

```Python
df = pd.read_csv('nombre_archivo.csv')
```
- `'nombre_archivo.csv'`: Es el nombre del archivo CSV que se va a leer. Puedes incluir la ruta completa si el archivo se encuentra en una ubicación diferente.
- `sep=','`: Define el separador de columnas en el archivo CSV. Por defecto, es una coma (`,`), pero puedes usar otros separadores como punto y coma (`;`) o tabulaciones (`\t`).
- `header='infer'`: Especifica la fila que se utilizará como encabezado de las columnas. Por defecto, Pandas infiere el encabezado de la primera fila. Si no hay encabezado, puedes establecer este parámetro en `None`.
- `names=None`: Permite asignar nombres personalizados a las columnas.
- `index_col=None`: Especifica la columna que se utilizará como índice del DataFrame.
- `encoding='utf-8'`: Especifica la codificación de caracteres que se utilizará para leer el archivo CSV. `utf-8` es una codificación común que admite una amplia gama de caracteres.
- `skiprows=None`: Permite omitir un número determinado de filas al principio del archivo.
- `nrows=None`: Permite leer un número determinado de filas del archivo.

##### `pd.read_excel()`
**`pd.read_excel()`** -> Leer un archivo Excel y generar un DataFrame a partir de sus datos.

> [!IMPORTANT]
> Esta función requiere la librería `openpyxl` para leer archivos Excel (`.xlsx`), así que asegúrate de tenerla instalada (`pip install openpyxl`).

```Python
df = pd.read_excel('nombre_archivo.xlsx', sheet_name='Hoja1')
``` 
- `'nombre_archivo.xlsx'`: Es el nombre del archivo Excel que se va a leer. Puedes incluir la ruta completa si el archivo se encuentra en una ubicación diferente.
- `sheet_name='Hoja1'`: Especifica el nombre de la hoja de cálculo que se va a leer. Por defecto, se lee la primera hoja. Puedes pasar un nombre de hoja o un índice numérico (0 para la primera hoja, 1 para la segunda, etc.).
- `header=0`: Especifica la fila que se utilizará como encabezado de las columnas. Por defecto, se utiliza la primera fila (índice 0). Si no hay encabezado, puedes establecer este parámetro en `None`.
- `names=None`: Permite asignar nombres personalizados a las columnas.
- `index_col=None`: Especifica la columna que se utilizará como índice del DataFrame.
- `skiprows=None`: Permite omitir un número determinado de filas al principio de la hoja.
- `nrows=None`: Permite leer un número determinado de filas de la hoja.

### Métodos Para Modificar Datos

Los métodos `map()`, `replace()` y `apply()` son herramientas poderosas en Pandas para transformar y manipular datos en Series y DataFrames. Aunque los tres se utilizan para realizar modificaciones, tienen diferencias importantes en cómo operan y para qué son más adecuados.

##### `.map()`
**Qué hace?** El método `map()` se utiliza para mapear o reemplazar valores en una Serie (una columna de un DataFrame) según un diccionario, una función o otra Serie.

**¿Cómo funciona?** Toma cada elemento de la Serie y lo busca en el diccionario o lo pasa a través de la función. El valor correspondiente del diccionario o el resultado de la función se utiliza para reemplazar el valor original.

**¿Cuándo usarlo?**
- Cuando tienes un mapeo uno a uno entre valores existentes y nuevos valores (usando un diccionario).
- Cuando necesitas aplicar una transformación simple a cada elemento de una Serie.

```Python
import pandas as pd

# Crear una Serie de ejemplo
s = pd.Series(['manzana', 'banana', 'naranja', 'manzana'])

# Mapear los valores a nuevos valores usando un diccionario
mapeo = {'manzana': 'roja', 'banana': 'amarilla', 'naranja': 'naranja'}
s_mapeada = s.map(mapeo)

print(s_mapeada)
```

##### `.replace()` 
**¿Qué hace?** El método `replace()` se utiliza para reemplazar valores específicos en una Serie o DataFrame con otros valores.

**¿Cómo funciona?** Busca los valores que se especifican para reemplazar y los sustituye con los nuevos valores. Puede usar diccionarios, listas, expresiones regulares, etc. para definir los reemplazos.

**¿Cuándo usarlo?**
- Cuando necesitas reemplazar valores específicos con otros valores.
- Cuando necesitas realizar reemplazos más complejos usando expresiones regulares.

```Python
import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']})

# Reemplazar valores específicos en el DataFrame
df_reemplazado = df.replace({1: 10, 'b': 'BB'})

print(df_reemplazado)
```

##### `.apply()`
**¿Qué hace?** El método `apply()` se utiliza para aplicar una función a lo largo de un eje de un DataFrame (filas o columnas) o a todos los elementos de una Serie.

**¿Cómo funciona?** Toma una función como argumento y la aplica a cada fila o columna del DataFrame, o a cada elemento de la Serie. La función puede realizar operaciones más complejas que `map()` o `replace()`.

**¿Cuándo usarlo?**
- Cuando necesitas realizar operaciones más complejas que involucran múltiples columnas o filas.
- Cuando necesitas aplicar una función personalizada a cada elemento de una Serie o DataFrame.

```Python
import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})

# Aplicar una función a cada fila del DataFrame
def sumar_cuadrado(fila):
  return fila['A']**2 + fila['B']**2

df_aplicado = df.apply(sumar_cuadrado, axis=1)

print(df_aplicado)
```

##### `.transform()`
El método `transform()` se utiliza para aplicar una función a lo largo de un eje de un DataFrame (filas o columnas) y devolver un nuevo objeto con la misma forma que el DataFrame original.

```Python
df.transform(func, axis=0, *args, **kwargs)
```
- `func`: La función que se va a aplicar a los datos.
- `axis`: El eje a lo largo del cual se va a aplicar la función (0 para filas, 1 para columnas).
- `*args`: Argumentos posicionales adicionales para pasar a la función.
- `**kwargs`: Argumentos de palabras clave adicionales para pasar a la función.

**Ejemplo 1** : Normalización de Datos
```Python
import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# Normalizar la columna 'A' restando la media y dividiendo por la desviación estándar
df['A_normalizado'] = df['A'].transform(lambda x: (x - x.mean()) / x.std())

print(df)
```

**Ejemplo 2** : Transformaciones Personalizadas
```Python
# Función para calcular el cuadrado de un valor
def cuadrado(x):
    return x ** 2

# Aplicar la función 'cuadrado' a la columna 'Valor'
df['Valor_cuadrado'] = df['Valor'].transform(cuadrado)

print(df)
```

**Diferencias con `apply()`**
Aunque `transform()` y `apply()` pueden realizar transformaciones similares, tienen diferencias importantes:
- `transform()` siempre devuelve un objeto con la misma forma que el DataFrame original, mientras que `apply()` puede devolver un objeto de forma diferente.
- `transform()` es más eficiente para operaciones que se pueden vectorizar, ya que aplica la función a toda la columna o fila a la vez, mientras que `apply()` puede ser más lento para operaciones que requieren iteración.

**Cuándo usar `transform()`**
- **Transformaciones que preservan la forma del DataFrame:** `.transform()` es ideal cuando necesitas aplicar una función a una o varias columnas de un DataFrame y deseas que el resultado tenga la misma forma (mismo número de filas y columnas) que el DataFrame original. 
 
- **Operaciones a nivel de grupo:** `.transform()` brilla cuando realizas operaciones que involucran grupos de datos. Por ejemplo, si deseas calcular la media de un grupo y luego asignar esa media a cada fila dentro de ese grupo, `.transform()` es la herramienta perfecta. 

- **Cálculos que dependen de otros valores en la columna:** Si necesitas realizar cálculos en una columna que dependen de otros valores en la misma columna (por ejemplo, normalización, estandarización), `.transform()` te permite acceder a toda la columna dentro de la función de transformación.

**Cuándo usar otro método**
- **`.map()`:** Útil para mapear o reemplazar valores uno a uno en una Serie (columna) basándote en un diccionario o una función simple. Es eficiente para transformaciones sencillas que no involucran grupos de datos ni cálculos complejos.

- **`.replace()`:** Ideal para reemplazar valores específicos en una Serie o DataFrame con otros valores. Puedes usar diccionarios, listas o expresiones regulares para definir los reemplazos. Es útil cuando necesitas realizar sustituciones directas sin necesidad de aplicar una lógica compleja.

- **`.apply()`:** El método más versátil, te permite aplicar una función a lo largo de un eje de un DataFrame (filas o columnas) o a todos los elementos de una Serie. Úsalo cuando necesitas realizar operaciones más complejas que involucran múltiples columnas o filas, o cuando requieres una función personalizada que no se ajusta a los casos de uso de `.map()` o `.transform()`. Sin embargo, ten en cuenta que `.apply()` puede ser menos eficiente que `.transform()` para operaciones vectorizadas.

### Acceder a Elementos de un DataFrame

##### Acceder a Columnas.
Tenemos tres formas de acceder a columnas.
- Usando el nombre como si fuera clave de un diccionario: `df["Altura_cm"]`
- Usando el nombre como si fuera un atributo de un objeto: `df.Altura_cm` 
	- (Es cómodo, pero **no** es recomendable)
- Usando una lista: `df[["Altura_cm", "Peso_kg"]]`

> [!NOTE]
> Obviamente si queremos verlo en terminal, debemos acompañarlo de su correspondiente `print()`. O, en todo caso, almacenarlo en otra variable.

##### Acceder a Filas.
Tenemos cuatro formas distintas de acceder a las filas de un DataFrame.
- Usando el atributo `.iloc` con el número de fila : `df.iloc[4]`
```Python
print(de.iloc[4])

''' OutPut
Genero           M
Edad            13
Altura_cm    181.0
Peso_kg       63.0
Name: 4, dtype: object
'''
```

- Usando el atributo `.iloc` con un `slice` y el número de fila `n` : `df.iloc[:n]`
	- Esto devuelve las primeras `n` filas.
```Python
print(df.iloc[:4])

''' OutPut
  Genero  Edad  Altura_cm  Peso_kg
0      M     8      126.0     24.0
1      F    18      159.0     61.0
2      M    16      171.0     69.0
3      M    27      157.0     88.0
'''
```

- Usando un filtro booleano (dentro de un llamado como a la clave de un diccionario) : `df[df["Altura_cm"] < 160]`
```Python
print(df[df['Altura_cm'] > 160]) 

''' OutPut
  Genero  Edad  Altura_cm  Peso_kg
2      M    16      171.0     69.0
4      M    13      181.0     63.0
6      M    37      170.0     57.0
7      M    23      171.0     84.0
8      M    27      193.0     82.0
9      F    35      163.0     61.0
''' 
```

- Usando el método `.query()` : `df.query("Altura_cm < 160")`
```Python
print(df.query('Edad < 25'))

''' OutPut
 Genero  Edad  Altura_cm  Peso_kg
0      M     8      126.0     24.0
1      F    18      159.0     61.0
2      M    16      171.0     69.0
4      M    13      181.0     63.0
7      M    23      171.0     84.0
'''
```

> [!NOTE]
> El método `.query()` en Pandas es una herramienta poderosa y versátil que te permite filtrar filas de un DataFrame utilizando una expresión en formato `str`. Esta expresión se evalúa para cada fila del DataFrame, y solo las filas que cumplen con la condición especificada se incluyen en el resultado.
> 
> ```Python
> df.query('expresión')
> ```
> Donde `expresión` es el `str` que representa la condición que deben cumplir las filas para ser seleccionadas.

> [!EXAMPLE]
> **Filtrar con `.query()` una expresión con mas de una condición**
> ```Python
> filtro_a:pd.DataFrame = df.query("Altura_cm < 160 and Genero == 'M'")
> 
> print(filtro_a)
> 
> ''' OutPut
>  Genero  Edad  Altura_cm  Peso_kg
0      M     8      126.0     24.0
3      M    27      157.0     88.0
> '''
> ```

##### Algunas Operaciones Sobre Columnas
Podemos ejecutar algunos métodos simples sobre una columna.
- `df["Nombre_de_la_Columna"].mean()` -> devuelve el promedio de la columna especificada.
- `df["Nombre_de_la_columna].sum()` -> devuelve la suma de todos los elementos de la columna especificada.

```Python
print(df["Altura_cm"].mean())   # OutPut -> 165.0

print(df["Altura_cm"].sum())   # OutPut -> 1650.0
```

### Tablas Dinámicas 

La función `pivot_table` en Pandas es una herramienta poderosa para **resumir y reorganizar datos** en un DataFrame. Es especialmente útil cuando tienes datos en un formato "largo" y deseas transformarlos a un formato "ancho", similar a una tabla dinámica en hojas de cálculo.

`pivot_table` te permite:
- **Agrupar datos:** Puedes agrupar datos por una o varias columnas, lo que te permite analizar subconjuntos específicos de tus datos.
- **Resumir datos:** Puedes calcular estadísticas (como sumas, promedios, medianas, etc.) para los datos agrupados.
- **Reorganizar datos:** Puedes cambiar la estructura de tu DataFrame, moviendo valores de columnas a filas o viceversa.

Sintaxis básica de `pivot_table`
```Python
pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
```

- `data`: El DataFrame que contiene los datos.
- `values`: La columna o columnas que se van a resumir (los valores que se mostrarán en la tabla dinámica).
	- Si queres pasarle varias columnas, le pasas una lista con las columnas en cuestión.
- `index`: La columna o columnas que se van a utilizar como índices de la tabla dinámica (las filas).
- `columns`: La columna o columnas que se van a utilizar como columnas de la tabla dinámica.
- `aggfunc`: La función de agregación que se va a utilizar (por defecto es 'mean', pero puedes usar otras como 'sum', 'count', 'median', etc.).
- `fill_value`: El valor que se va a utilizar para rellenar los valores faltantes.

**Ejemplo 1** : Resumir Ventas por Región y Producto.
```Python
import pandas as pd

data = {'Region': ['Norte', 'Norte', 'Sur', 'Sur', 'Este', 'Este'],
        'Producto': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Ventas': [100, 150, 200, 250, 300, 350]}
df = pd.DataFrame(data)

# Crear una tabla dinámica que muestre las ventas por región y producto
tabla_dinamica = pd.pivot_table(df, values='Ventas', index='Region', columns='Producto', aggfunc='sum')

print(tabla_dinamica)
```

**Ejemplo 2** : Calcular el Promedio de Edad Por Género y Ciudad.
```Python
data = {'Genero': ['M', 'F', 'M', 'F', 'M'],
        'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Barcelona', 'Madrid'],
        'Edad': [25, 30, 22, 28, 24]}
df = pd.DataFrame(data)

# Crear una tabla dinámica que muestre el promedio de edad por género y ciudad
tabla_dinamica = pd.pivot_table(df, values='Edad', index='Genero', columns='Ciudad', aggfunc='mean')

print(tabla_dinamica)
```


**Fin.** 