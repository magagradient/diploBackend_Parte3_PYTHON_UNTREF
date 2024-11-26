# metodos en variables

"""
* len(var): se utiliza para obtener la longitud de una cadena, es decir, el número de caracteres que contiene.
* lower(var): Convierte todos los caracteres de la cadena a minúsculas.
* upper(var): Convierte todos los caracteres de la cadena a mayúsculas.
* strip() - lstrip() - rstrip(): Elimina los espacios en blanco al principio y al final de la cadena, los espacios al inicio de la cadena, y los espacios al final de la cadena, respectivamente.
* replace(prev, new): Reemplaza todas las apariciones de una subcadena prev en la cadena con la subcadena new.
* count(var): Cuenta cuántas veces aparece una subcadena en la cadena.
* find(var): Encuentra la primera posición de una subcadena en la cadena. Si no se encuentra, devuelve -1.
* split(separador): Divide la cadena en una lista de subcadenas utilizando el separador especificado.
* startswith(var): Comprueba si la cadena comienza con la subcadena especificada y devuelve True o False.
* endswith(var): Comprueba si la cadena termina con la subcadena especificada y devuelve True o False.
* isalpha(var): Comprueba si la cadena contiene solo letras (sin espacios ni números) y devuelve True o False.
* isalnum(var): Comprueba si la cadena contiene solo dígitos numéricos y devuelve True o False.
* isupper(): Comprueba si todos los caracteres de la cadena están en mayúsculas y devuelve True o False.
* islower(): Comprueba si todos los caracteres de la cadena están en minúsculas y devuelve True o False.
"""
nombre = "        Juan Domingo Peron       "

print(len(nombre)) # 18 (cantidad de caracteres)

print(nombre.lower()) # juan domingo peron

print(nombre.upper()) # JUAN DOMINGO PERON

nombre = nombre.replace('Juan Domingo', 'Eva Duarte de') # Eva Duarte de Peron

print(nombre.strip()) # quita los espacios

print(nombre.lstrip()) # quita los espacios de la izuierda

print(nombre.rstrip()) # quita los espacios de la derecha

print(nombre.count('e')) # 3 letras e 

print(nombre.find('Maria')) # devulve -1 porque no esta en el texto 

print(nombre.find('Peron')) # devulve 22 (cuenta la posicion con los espacios incluidos)

print(nombre.strip().split(' ')) # devuelve una lista: ['Eva', 'Duarte', 'de', 'Peron'] (no se llama 'array' como seria en javascript si no 'lista')

print(nombre.strip().startswith('Ev')) # True

print(nombre.strip().endswith('on')) # True

print(nombre.strip().isdigit()) # False porque es solo para digitos. 

print(nombre.strip().isalnum()) # False 

print(nombre.strip().isupper()) # False porque no esta todo en mayuscula.

print(nombre.upper().isupper()) # True





























