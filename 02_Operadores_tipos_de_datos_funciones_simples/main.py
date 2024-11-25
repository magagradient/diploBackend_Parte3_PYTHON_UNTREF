# TIPOS DE VARIABLES

# 1. Enteros (int): Representan números enteros, como 5 o -3.
edad = 39

# 2. Punto flotante (float): Representan números con decimales, como 3.14 o -0.5.
antiguedad = 3.4

# 3. Cadenas de texto (str): Almacenan texto, como "Hola, mundo!".
nombre_completo = "Lana Del Rey"

# 4. Booleanos (bool): Representan valores de verdad, True o False. (Recordar que en python se declaran on la primera inicial en mayuscula).
mando_medio = True
accionista = False

# 5. NoneType (None): Representa la ausencia de un valor o un valor nulo.

########################################
"""Si deseamos representar tipos de datos diferentes a String en pantalla, utilizando print(), aquí debemos tener presente que Python no se comporta igual que JS.

En este caso, debemos castear cualquier variable no string, utilizando la función str(), la cual convierte el valor de dicha variable a una cadena de texto.
"""
print("la edad es: " + str(edad))
print("Valor de accionista: " + str(accionista))


#########################################
# CONSTANTES
"""En Python, no existe un mecanismo nativo para declarar constantes como lo hay en JavaScript, donde usamos la palabra clave const para definir una constante. Aquí, las variables se pueden reasignar siempre.

Sin embargo, se utiliza una convención para nombrar las variables que se consideran constantes como si fueran tales, utilizando letras mayúsculas y guiones bajos para separar palabras combinadas

Aunque estas variables pueden ser reasignadas en Python, se considera una buena práctica no modificar su valor una vez que se les ha asignado un valor inicial. Si otros programadores encuentran una variable escrita en mayúsculas en el código, se espera que se comporte como una constante y no sea modificada.
"""

# API_KEY = 'f454d6f4fggf'
# API_KEY = 1234

# print('API Key', API_KEY)

#############################################
# Typeof
"""En Python, no existe un operador typeof como el que se utiliza en JavaScript para verificar el tipo de una variable. En lugar de typeof, Python nos ofrece el operador isinstance() y la función type() para verificar y obtener información sobre el tipo de una variable.Retornará como resultado True o False, una vez analizado el valor de la 
variable"""

print(type(edad), isinstance(edad, bool)) # <class 'int'> False

texto = 'la edad es: ' + str(edad)

print(type(texto), isinstance(texto, str)) # <class 'str'> True

print(texto) 


####################################
# Operadores de comparación

"""Al igual que lo visto en JS, en Python, los 
operadores de comparación también son fundamentales para la lógica de control de flujo. Estos operadores de comparación son comunes a prácticamente cualquier lenguaje de programación.
Tienen la estructura similar a la utilizada en JS, con la diferencia de “igual a” y “distinto de”, donde sólo se utiliza el doble igual o un simple igual para el último de los casos.
Aquí no existe el “estrictamente igual” o “estrictamente distinto de” porque, a diferencia de JS, en Python cada variable maneja un tipado dinámico pero no débil"""

# numero_uno = 123
# numero_dos = '123'

# print(type(numero_uno), type(numero_dos)) # <class 'int'> <class 'str'>

# print(str(numero_uno == numero_dos)) # False

# print(str('Hola' == 'hola')) # False

########################################
# Operadores lógicos

'''El operador lógico AND retorna True si ambas expresiones son verdaderas. Si al menos una es falsa, el resultado es False.
El operador lógico OR retorna True si al menos una de las expresiones es verdadera. Si ambas son 
falsas, el resultado es False.
El operador lógico NOT retorna el valor opuesto de la expresión; es decir: True si la expresión es falsa, y 
False si la expresión analizada es verdadera.
'''

numero_uno = 4
numero_dos = 5

print(str(numero_uno >= 4 and numero_dos == 5)) # True

print(str(numero_uno >= 4 or numero_dos < 5)) # True











