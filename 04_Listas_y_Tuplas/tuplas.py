# TUPLAS

"""
Cuando hablamos de tuplas en el lenguaje Python, estamos hablando de una estructura de datos, similar a las listas que vimos anteriormente, pero con la diferencia de que éstas no pueden ser modificadas.
Una tupla permite almacenar diversos tipos de contenidos, de forma ordenada, para luego representarlos con claridad

Cuando nos referimos a que una tupla no puede ser 
modificada, estamos hablando de que la misma es inmutable, por lo tanto, una vez que cargamos el contenido en la misma, al momento de referenciarla éste, no variará, será inalterable.

Al no poder modificarse los elementos de una tupla, no podemos agregar nada en la misma pero sí podemos recurrir a unificar dos tuplas en una tercera tupla nueva, o, agregar en una tupla nueva el contenido de una tupla existente más otros valores adicionales, tal como vemos en el ejemplo de la imagen.
"""

grado = ("estudiante", "Recibido", "Maestría", "Doctorado", "PosDoc")
taskStatuses = ("no iniciada", "en proceso", "finalizada")

# print(taskStatuses[1:3])

# print(len(taskStatuses))

# mi_tupla = grado + taskStatuses
# print(mi_tupla)

paises = ('Argentina', 'Uruguay', 'Chile')

mi_lista = list(paises)
mi_lista.append('Brasil')

print(mi_lista)

mi_tupla = tuple(mi_lista)

print(mi_tupla)

""""La aplicación de datos basados en tuplas, dentro de una aplicación de software, debe apuntar a aquellos casos donde los valores contenidos no varían con el tiempo. Ejemplos:
● Tipos de comprobantes según situación ante afip
    ○ (FA, FB, FC, NDA, NDB, NDC, NCA, NCB, NCC)
● listado de posibles países limitados a una región
● ciudades o localidades a elegir
● estados de una tarea correspondiente a un gestorespecífico. Entre otras tantas opciones posibles"""