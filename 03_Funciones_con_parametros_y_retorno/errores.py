# Controlar errores

"""
En Python tenemos la posibilidad de controlar errores en determinadas situaciones, implementando el uso del bloque try - except.
Este funciona igual al bloque try - catch utilizado en muchos lenguajes de programación definiendo en el bloque try, el código a ejecutar en el cual podemos tener algún tipo de error.
Además de controlar los errores utilizando TypeError, Python ofrece una variedad de tipos de excepciones que puedes controlar utilizando el bloque except.

* ValueError: Se produce cuando ocurre un error relacionado con el tipo correcto pero un valor incorrecto, como cuando intentas convertir una cadena en un número y la cadena no es numérica.
* ZeroDivisionError: Se produce cuando intentas dividir un número por cero, lo cual no está permitido.
* NameError: Se produce cuando intentas acceder a una variable o función que no está definida en el ámbito actual.
* IndexError: Se produce cuando intentas acceder a un índice fuera de rango en una secuencia, como una lista o una cadena.
* KeyboardInterrupt: Se produce cuando el usuario interrumpe la ejecución del programa presionando Ctrl + C en la consola.
"""

def normalizar_nombre(texto):
    if len(texto.strip()) > 0:
        return texto.strip().lower()

try:
    nombre = normalizar_nombre("      AubReY pLaZa   ")
    print(nombre) # aubrey plaza

    nombre = normalizar_nombre()
    print(nombre) 
except TypeError:  
    print('El parametro es incorrecto')  

####-----------------####

def dividir(num1, num2):
    return num1 / num2

try:
    dividir(85, 5)
except ZeroDivisionError:
    print('Division por cero')
except:
    print('Error')
else:
    print('Sin error')
finally:
    print('Siempre se ejecuta')


####-----------------####

# Este bloque de código define una función para dividir dos números de forma segura, manejando posibles errores, y luego ejecuta esa función interactuando con el usuario:

# Definición de la función dividir_numeros:

"""
Parámetros:

* dividendo: El número que será dividido.
* divisor: El número por el que se divide el dividendo.

Bloque try:
Intenta realizar la operación de división dividendo / divisor.
Si es exitosa, devuelve el resultado con return resultado.

Manejo de excepciones (except):
* ZeroDivisionError: Se lanza si el divisor es 0. En ese caso, se genera un nuevo error (ValueError) con el mensaje "⛔️ Error: División por cero no permitida.".
* TypeError: Se lanza si los valores no son numéricos (por ejemplo, si se pasa un string). También se genera un error ValueError con el mensaje "⛔️ Error: Los valores deben ser numéricos.".
"""

def dividir_numeros(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        raise ValueError("⛔️ Error: División por cero no permitida.")
    except TypeError:
        raise ValueError("⛔️ Error: Los valores deben ser numéricos.")

# Ejecutamos la función
try:
    num1 = float(input("Ingresa el dividendo: "))
    num2 = float(input("Ingresa el divisor: "))
    resultado = dividir_numeros(num1, num2)
    print("✅ El resultado de la división es:", resultado)

except ValueError as error:
    print("Error de valor: " + str(error))
except KeyboardInterrupt:
    print("🟡 Operación interrumpida por el usuario.")

"""
Ejecución de la función:

Entrada del usuario:
Se solicita el dividendo y el divisor con input. Ambos valores se convierten a tipo float para garantizar que sean numéricos.

Llamada a la función:
Se pasa num1 y num2 a dividir_numeros.

Salida:
Si la operación es exitosa, se imprime el resultado.
"""

"""
Manejo de errores al ejecutar la función:

* ValueError: Si ocurre un error relacionado con la lógica de la división (por ejemplo, división por cero o valores no numéricos), se captura y se imprime el mensaje de error.

* KeyboardInterrupt: Se captura si el usuario interrumpe la ejecución del programa (por ejemplo, presionando Ctrl + C). Se imprime un mensaje indicando que la operación fue interrumpida.
"""

# El código es robusto y asegura que:

# Se puedan manejar entradas erróneas (como valores no numéricos o divisor igual a cero).
# Se pueda interactuar de forma segura con el usuario.
# Ofrezca mensajes claros para cada tipo de error.