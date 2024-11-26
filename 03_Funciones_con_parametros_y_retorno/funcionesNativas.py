# Funciones nativas de Python

"""
* str(objeto): Convierte un objeto en una cadena de texto. Puede utilizarse para convertir números, listas u otros tipos de datos, en cadenas.
* int(cadena, base): Convierte una cadena a un número entero. La base es opcional y se suele utilizar para especificar la base numérica en la que se encuentra la cadena de texto a convertir.
* float(cadena): Convierte una cadena de texto en un número de punto flotante (con decimales).
* type(objeto): Devuelve el tipado del objeto en cuestión. Podemos utilizarlo con variables del tipo string, number, float, objetos, listas, tuplas, etcétera. Retorna siempre <class ‘tipo objeto’> como resultado.
* range(inicio, fin, salto): Genera una secuencia de números en un rango especificado. Podemos definir también un salto, o step.
* round(numero, dec): Redondea un valor numérico en una cantidad específica de decimales.
"""

numero = 123

print('Un numero: ' + str(numero)) # Un numero: 123

print('La suma es: ', numero + int('1')) # La suma es:  124 (lo transforma a un entero)

print('La suma es: ', type(numero), numero + float('1.56')) # La suma es:  <class 'int'> 124.56

suma = numero + float('1.56')

print('La suma es: ', type(numero), type(suma), suma) # La suma es:  <class 'int'> <class 'float'> 124.56 

#######################################

# la creación de un rango y un bucle que itera a través de él: Crea un rango de números que comienza en 2, termina en 10 (el 11 no se incluye), y avanza en pasos de 2. El código simplemente genera e imprime los números pares entre 2 y 10 de manera secuencial.

rango = range(2, 11, 2) # 2: Número inicial, 11: Límite superior (no incluido), 2: Paso o incremento entre cada número.

for numero in rango:
    print(numero) # 2 4 6 8 10






