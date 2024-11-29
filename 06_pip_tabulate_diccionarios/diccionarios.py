#  Diccionarios

"""
En Python son estructuras de datos que almacenan pares clave-valor. Son muy versátiles y se utilizan ampliamente debido a su capacidad para almacenar y recuperar datos de manera eficiente.

En un diccionario, cada elemento está representado por 
una clave única y su valor correspondiente.

Dentro de las principales características que encontramos 
en un diccionario, podemos destacar:
● estructura clave-valor
● claves únicas
● mutabilidad
● heterogeneidad
"""

# Aquí tenemos la estructura de un diccionario Python, donde almacenamos la información de un estudiante, los cursos tomados y la puntuación de cada uno de ellos.(parecido a un json de js)

estudiante = {
    "nombre": "Coki Argento",
    "edad": 25,
    "cursos": ["Node.js", "Python"],
    "puntuacion": {
        "Node.js": 9.2,
        "Python": 8.5
    }
}

print(estudiante)

# el diccionario estudiante tiene claves como "nombre", "edad", "cursos" y "puntuacion", y cada una tiene su respectivo valor asociado (pares clave-valor).

# Podemos acceder a los valores de un diccionario utilizando la sintaxis de corchetes [] y la clave:

print(estudiante["nombre"])
print(estudiante["puntuacion"]["Python"])

# Para listar debemos iterarlo primero para armar un diccionario de lista simple, eliminando sus propiedades (clave). Las mismas deben ser representadas en una tupla, como encabezado de la tabla a mostrar

from datos import productos

from tabulate import tabulate

headers = ["ID", "Nombre", "Importe", "Categoría"]
tabla = [[producto["id"], producto["nombre"], producto["importe"], producto["categoria"]] for producto in productos]


print(tabulate(tabla, headers=headers, tablefmt="github"))

# Importar y Exportar

"""
Python nos permite modular la estructura de nuestras 
aplicaciones, generando en archivos separados contenido 
que tengamos que implementar.
Esto nos permite estructurar mejor nuestras aplicaciones, 
separando en capas la lógica, los datos, y el resto de 
funcionalidades necesarias para nuestra app
"""
