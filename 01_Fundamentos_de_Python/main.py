import os 

os.system("clear")

# Sintaxis básica:

# La depuración de nuestras aplicaciones la haremos integrando el uso de la función print(), nativa de Python. Esta es una función equivalente a console.log() de JS.

print("hola python!", 10 - 5)

# La misma función print() nos permite visualizar el resultado de cualquier operación aritmética con números. Estos se escriben igual que en JS, sin comillas, y el resultado de dicha operación se imprimirá en la ventana Terminal.

print(10 - 5) # python main.py en la terminal para imprimir. 

###################################
#Comentario multilinea: 
""" 
Los comentarios de línea simple se realizan con el caracter #. Los comentarios de líneas múltiples, repitiendo tres veces el caracter “““, tanto para la apertura como para el cierre.
"""

####################################
# input para pedirle al usuario algo
"""El ingreso de datos en JavaScript orientado al backend mediante la ventana Terminal no era 
posible. Sin embargo, Python sí cuenta con una función que nos permite ingresar contenido.

Podemos comparar la función input() de Python con prompt() de JavaScript frontend."""

nombre = input("ingresa su nombre: ")

print("Hola", nombre)

#####################################
"""La declaración de variables es dinámica. Podemos 
definir una variable y asignarle un valor sin tener 
que especificar el tipado de datos de la misma."""

#string:
nombre_completo = "Magali Guerzoni"

#number:
fecha_nacimiento = 1990

#boolean:
is_admin = False

######################################
"""Los módulos en Python son archivos que contienen código reutilizable, como funciones, clases y variables. Estos permiten organizar y estructurar el código de manera más eficiente, lo que facilita su mantenimiento y reutilización. Los módulos pueden incluir definiciones de objetos y funciones que se pueden importar en otros programas o módulos para extender la funcionalidad de una aplicación."""

"""Por ejemplo, Python tiene comunicación con el Sistema Operativo donde se está ejecutando. Para 
ello, requiere el uso de un módulo denominado os.
Podemos importar este módulo para luego ejecutar acciones desde Python, sobre el sistema operativo 
en sí. Un ejemplo de ello sería si deseamos limpiar la ventana Terminal o de Línea de comandos, en 
el momento de iniciar nuestra aplicación Python y justo antes de ejecutar su lógica"""

# import os (se importa al principio del codigo).

# os.system("clear")





