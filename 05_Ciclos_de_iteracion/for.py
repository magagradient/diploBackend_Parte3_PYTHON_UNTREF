# ITERACION

"""
Python nos ofrece varias estructuras de bucles que  permiten la iteración a través de secuencias, colecciones 
de elementos, o realizar tareas repetitivas. 
Los ciclos de iteración disponibles, son:
    ● for 
    ● while - loop
"""

# For:
"""
for loop: Este ciclo es ideal para iterar sobre una 
secuencia (lista, tupla, diccionario, etc.) o para ejecutar un bloque de código un número específico de veces.
Para utilizarlo, debemos combinarlo con la cláusula in, y 
establecer luego el uso de : como indicador del código que ejecutará.
Al definir la cláusula for, le indicamos como primer parámetro el nombre del ítem que utilizaremos como valor para obtener cada elemento de la lista o tupla a ejecutar. Luego, en la línea continua, tabulación mediante, 
definimos qué hacemos con el item capturado por este ciclo.
este ciclo es extremadamente versátil y puede usarse de diversas formas, proporcionando funcionalidadesadicionales y flexibilidad.
"""

lenguajes = ["C", "C++", "C#", "Python", "GoLang", "JavaScript"]

for lenguaje in lenguajes:
    print(lenguaje)

##----------------------------------------##

# For: Iteración sobre rangos: 
# Podemos hacer uso del bucle for para iterar a través una secuencia numérica, utilizando en este caso la función range(). 

for num in range(2, 11, 2):
    print('Numero: ', str(num))

for num in range(2, 5):
    print('Numero: ' + lenguajes[num])


##----------------------------------------##

# For: acceso a índices y elementos
# Esta otra implementación del ciclo For nos permite, a través del método enumerate(), acceder tanto al índice como al elemento en cada iteración

for indice, lenguaje in enumerate(lenguajes):
    print(f"El indicie {indice }contiene el lenguaje {lenguaje}") 

# devuelve: 
# El indicie 0contiene el lenguaje C
# El indicie 1contiene el lenguaje C++
# El indicie 2contiene el lenguaje C#
# El indicie 3contiene el lenguaje Python
# El indicie 4contiene el lenguaje GoLang
# El indicie 5contiene el lenguaje JavaScript

##----------------------------------------##

# For: implementar el condicional else
# También en el uso del bucle for podemos sumarle una cláusula else la cual se ejecuta cuando dicha iteración es completada sin ningún tipo de interrupciones.

for i in range(3):
    print('Numero: ' + str(i))
else:
    print('Iteracion completada con exito')

# Aca vemos el resultado del ejemplo anterior. Al finalizar la iteración completa definida en el ciclo for, se ejecuta la cláusula else definida, para imprimir finalmente el mensaje declarado en esta última cláusula.:

# Numero: 0
# Numero: 1
# Numero: 2
# Iteracion completada con exito  

##----------------------------------------##

# For: comprensiones de listas
# También podemos implementar este ciclo para las comprensiones de lista. Esto nos ayuda a crear listas de una manera más concisa:

cuadrados = [i ** 2 for i in range(5)]  # Crea una lista de cuadrados
print(cuadrados) # [0, 1, 4, 9, 16]

"""
range(5):

* Genera una secuencia de números enteros desde 0 hasta 4 (el límite superior no está incluido).
* Secuencia generada: [0, 1, 2, 3, 4].

Comprensión de lista: [i ** 2 for i in range(5)]:

* Este bloque crea una nueva lista donde cada elemento es el resultado de elevar al cuadrado (i ** 2) cada número i de la secuencia generada por range(5).

Lo que hace:

Toma 0, lo eleva al cuadrado (0 ** 2), resultado: 0.
Toma 1, lo eleva al cuadrado (1 ** 2), resultado: 1.
Toma 2, lo eleva al cuadrado (2 ** 2), resultado: 4.
Toma 3, lo eleva al cuadrado (3 ** 2), resultado: 9.
Toma 4, lo eleva al cuadrado (4 ** 2), resultado: 16.
"""

##----------------------------------------##

"""
El ciclo for también nos permite sumar una serie de 
cláusulas internas, para complementar la iteración del 
ciclo en cuestión.Entre ellas, encontramos a:
● pass
● continue
"""

# For: pass. Se utiliza como un marcador de posición o sentencia nula. No hace nada, solo evita errores cuando se requiere sintácticamente una declaración. 

# for item in lenguajes:
#     if (item == 'C#'):
#         continue

#     print(item)

"""
También podemos implementar múltiples condicionales previo a ejecutar la cláusula pass. Para ello, combinamos el uso del operador lógico OR.

continue se utiliza para pasar a la siguiente iteración del ciclo sin ejecutar el código restante del bloque. 
"""

for i in range(1, 11):
    # if (i % 2 == 1):
    #     pass

    if i == 3 or i == 6 or i == 7:
        continue

    print(i)

# def saludar(nombre):
#     pass

# saludar('Juan')

# modulo = 11 % 2
# print(modulo)







