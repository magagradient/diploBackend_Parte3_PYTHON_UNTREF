#EJERCICIO:
""""Crea un programa en Python que solicite al usuario que ingrese una cadena de texto y luego cuente el número de vocales en la cadena. Debes utilizar únicamente las siguientes estructuras y funciones:

a. variables string
b. condicionales if - elif
c. funciones input() y print()
d. Al menos una función que contenga el código principal

La función principal debe contar el número de vocales en la cadena ingresada (a, e, i, o, u) sin utilizar un ciclo de iteración. Finalmente muestra un mensaje que indique cuántas vocales se encontraron en la cadena."""

import os 
os.system('clear')

def vocales():
    texto = input('Ingrese un texto: ').strip().lower()

    if texto != '':
        contador = 0

        contador += texto.count('a')
        contador += texto.count('e')
        contador += texto.count('i')
        contador += texto.count('o')
        contador += texto.count('u')

        # print(texto.lower().count('e'))

        print('Cantidad de vocales:', contador)
    else:
        print('Ingrese un texto valido')

vocales()