# Funciones

"""Estas se definen mediante la palabra clave def seguida del nombre de la función, paréntesis (que pueden contener parámetros) y el bloque de código indentado.
Las funciones, deben representar en su nombre una acción, por lo tanto, debemos definirlo con un verbo, que exprese dicha acción, y utilizando el modo imperativo
"""
def clima():
    print('Frio porque hay viento')


def saludar():
    nombre = input('Ingrese su nombre: ')
    print('Hola', nombre)
    clima()

saludar()
    