# Condicionales

"""Ya sabemos que, los condicionales, permiten ejecutar un bloque de código si una condición especificada es verdadera. En Python están disponibles los mismos condicionales que en casi todos los otros lenguajes, incluyendo a JS, pero aquí varía ligeramente su sintaxis.
"""

# edad = input('Ingrese su edad: ' )

# if int(edad) >= 18:
#     print('Es mayor de edad')

# nombre = input('Ingrese su nombre: ')

# print(nombre.strip().lower())

# if nombre == 'Paul':
#     print('Hola', nombre)

#############################

edad = input('Ingrese su edad: ' )

if edad.isdigit() and int(edad) >= 18:
    print('Es mayor de edad')
elif not edad.isdigit():
    print('Ingrese un numero valido')
else:
    print('Es menor de edad')







