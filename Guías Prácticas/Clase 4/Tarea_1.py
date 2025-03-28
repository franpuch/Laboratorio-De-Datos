# Tarea 1 - Procesamiento de Datos.

empleado_01:list[list[int]] = [[20222333, 45, 2, 20000], 
                               [33456234, 40, 0, 25000],
                               [45432345, 41, 1, 10000]]

# Actividad Nro. 01 ------------------------------------------------------------------------------------------------------- #

def superanSalarioActividad01(matriz:list[list[int]], umbral:int) -> list[list[int]] :
    res:list[list[int]] = list() 

    for empleado in matriz :
        if (empleado[3] > umbral) :
            res.append(empleado) 
    
    return res 

'''
Es una función usando las herramientas básicas de Python. No me costó mucho.
'''


# Actividad Nro. 2 -------------------------------------------------------------------------------------------------------- #

def agregarFilas(dataset:list[list[int]], filas_nuevas:list[list[int]]) -> list[list[int]] :
    res:list[list[int]] = list() 

    for fila in dataset :
        res.append(fila) 

    for fila_nueva in filas_nuevas :
        res.append(fila_nueva) 

    return res 

nuevas_filas:list[list[int]] = [[43967304, 37, 0, 12000],
                                [42236276, 36, 0, 18000]]
empleado_02:list[list[int]] = agregarFilas(empleado_01, nuevas_filas) 


# Actividad Nro. 3 -------------------------------------------------------------------------------------------------------- #

def cambiarColumnas(matriz:list[list[int]], columna_1:int, columna_2:int) -> list[list[int]] :
    res:list[list[int]] = list() 

    for fila in matriz :
        nueva_fila:list[list[int]] = list()
        for j in range(0, len(fila)) :
            if ((j != columna_1 - 1) and (j != columna_2 - 1)) :
                nueva_fila.append(fila[j])  
            elif (j == columna_1 - 1) :
                nueva_fila.append(fila[columna_2 - 1]) 
            elif (j == columna_2 - 1) :
                nueva_fila.append(fila[columna_1 - 1]) 
        
        res.append(nueva_fila)

    return res 

empleado_03:list[list[int]] = cambiarColumnas(cambiarColumnas(empleado_02, 2, 4), 3, 4)

'''
Ok... creo que me adelanté.
El ejercicio pide re-implementar la función 'superanSalarioActividad01', para que ahora funcione 
con 'empleado_03'. PERO, como implementé una función que cambia el orden de las columnas (para poder
armar empleado_03), me basta con aplicarle mi función que cambia columnas (a 'empleados_03' de nuevo)
y ahí voy a poder usar 'superanSalarioActividad01' sin problemas.
Como obtengo el mismo resultado que el que debería devolver 'superanSalarioActividad03', me ahorro 
implementarla.
O bueno... la implemento "sin implementarla".'
'''

def superanSalarioActividad03(matriz:list[list[int]], umbral:int) -> list[list[int]] :
    # Esto recibe una matriz con el orden de empleado_03, la acomodo a algo que pueda
    # recibir 'superanSalarioActividad01'
    nueva_entrada:list[list[int]] = cambiarColumnas(cambiarColumnas(matriz, 2, 3), 3, 4)

    return superanSalarioActividad01(nueva_entrada, umbral) 


# Actividad Nro. 4 -------------------------------------------------------------------------------------------------------- #

empleado_04:list[list[int]] = [[20222333, 33456234, 45432345, 43967304, 42236276],
                               [20000, 25000, 10000, 12000, 18000], 
                               [45, 40, 41, 37, 36], 
                               [2, 0, 1, 0, 0]]

def superanSalarioActividad04(matriz:list[list[int]], umbral:int) -> list[list[int]] :

    if (len(matriz) == 0) :
        return [] 

    res:list[list[int]] = [] 
    index_aux:int = 0

    for salario in matriz[1] :
        if (salario > umbral) :
            valido:list[int] = []
            for i in matriz :
                valido.append(i[index_aux])
            res.append(valido) 
        index_aux += 1
    
    # Aprovecho la función que armé antes (que me facilita bastante el trabajo de devolver 
    # las columnas ordenadas de la forma que pide).
    res = cambiarColumnas(res, 2, 3) 
    res = cambiarColumnas(res, 3, 4) 
    
    return res


# Actividad Nro. 5 -------------------------------------------------------------------------------------------------------- #

'''
1. A priori, el cambio de las condiciones que cumplen los parámetros de entrada siempre llevan el riesgo de afectar las 
   funcionalidades que uno preparó. Ya que uno resuelve el problema a partir de ciertas condiciones iniciales. O mejor 
   dicho, a partir de suponer que las entradas (del programa) van a cumplir siempre las mismas condiciones.
   En mi opinión, cambiar las características de los parámetros de entrada es (en el fondo) cambiar el problema. Con 
   "cambiar el problema" me refiero a el problema implementativo. Ya que el problema general, en este caso filtrar aquellos 
   empleados cuyo salario es mayor a un umbral, no cambia. Pero el problema que resuelven las funciones, que depende directamente
   de la forma de los parámetros de entrada, sí. Ya que la función va a tener que trabajar los parámetros de otra forma para 
   obtener el mismo resultado.

   a. Agregar mas filas no cambia la forma de los parámetros de entradas. Ya que agregar más filas no implica un cambio 
      estructural, sino un "cambio de tamaño" del parámetro de entrada. 
      Por lo tanto, ahí no tuve problema en volver a utilizar las funciones que ya había preparado. 
    
    b. Alterar el orden de las columnas sí, ya implica un cambio en las precondiciones que segían los parámetros de entrada.
       Por lo tanto, fue necesario implementar nuevas funcionalidades que sépan cómo manejar estas nuevas formas. Ya que, 
       por ejemplo, los "salarios" dejaron de estar donde estaban, entonces la función debe ir a buscarlos en otro lado.

2. La misma idea que antes. Los parámetros de entrada pasan a cumplir unas nuevas precondiciones, por lo tanto hay que preparar 
   nuevas funcionalidades que sepan trabajar con esas precondiciones. 
   Acá me surge una inquietud, que me lleva a pensar qué es mejor: hacer nuevas funcionalidades que sepan trabajar parámetros que 
   cumplen distintas precondiciones (pero devuelvan el mismo resultado), o hacer funcionalidades que acomoden la forma de los 
   parámetros (de entrada) a la forma que mi función sabe trabajar. Pensandolo bien, creo que depende del caso. Depende de cuánto
   me cuesta hacer una y la otra, computacionalmente como en esfuerzo de programación. Ya que tener muchas funciones que atajan 
   entradas distitnas pero hacen lo mismo, no está bueno. Pero acomodar las entradas tal vez me cuesta mucho (computacionalmente o
   en esfuerzo de pensar los algoritmos) debido a que, por ejemplo, las entradas son super complejas. En estas actividades no hay 
   mucha diferencia, hacerlos de una forma u otra no cambia mucho ya que son funciones y entradas simples. Pero de nuevo, creo que 
   depende del caso.
   Creo que me desvié un poco de la cuestión principal. Pero bueno... lo dejo porque me tomo un tiempito pensarlo y no quiero que 
   quede en simples ideas mías. Tal vez la mayor experiencia de ustedes pueda orientarme un poco más. 

3. Ok... no entiendo bien la pregunta. Qué es "ella"? La función 'superanSalarioActividad0...'? El programa completo? Cuál de todas
   las funciones 'superanSalarioActividad0...' especificamente (porque todas trabajan de forma distinta)?. Digo... al usuario siempre 
   le conviene tener una sola función que resuelva el problema. Si después por atrás hay varias funciones que trabajan de forma 
   distinta (pero dan el mismo resultado) no es necesario que el usuario lo sepa. De hecho, por una cuestión de facilidad de uso
   y entendimiento, al usuario siempre le conviene tener una sola fucnión que resuelva su problema. 
'''


# Test -------------------------------------------------------------------------------------------------------------------- #

'''
Sé que no es la forma correcta de hacer Testing. Sé que lo ideal sería hacer tests unitarios con PyTest 
u otra herramienta dedicada. Pero como son pocas implementaciones a probar, recurro a la mala práctica 
de probar todo con 'prints' (PERO EN FORMA PROLIJA Y ENTENDIBLE... por lo menos).
'''

# print(superanSalarioActividad01(empleado_01, 15000)) 
# print(superanSalarioActividad01(empleado_01, 1000))
# print(superanSalarioActividad01(empleado_01, 50000))
# print(superanSalarioActividad01([], 1000)) 

# print(empleado_02) 
# print(superanSalarioActividad01(empleado_02, 15000)) 

# print(cambiarColumnas(empleado_02, 2, 4))
# print(cambiarColumnas(empleado_02, 2, 2))
# print(cambiarColumnas(cambiarColumnas(empleado_02, 2, 4), 3, 4)) 

# print(superanSalarioActividad03(empleado_03, 15000)) 

# print(superanSalarioActividad04(empleado_04, 15000)) 
# print(superanSalarioActividad04(empleado_04, 5000)) 
# print(superanSalarioActividad04(empleado_04, 50000))
# print(superanSalarioActividad04([], 1000)) 

# Fin.