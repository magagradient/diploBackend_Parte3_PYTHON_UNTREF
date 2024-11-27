# LISTAS

# crear una función que limpie la pantalla previo o post ejecutar funciones específicas:
def limpiar_pantalla():
    import os
    if (os.system.__name__ == 'MacOS' or 'Linux'):
        os.system('clear') 
    else:
        os.system('cls')

# Luego otra función que llame a la primera, y luego muestre el contenido de la lista en cuestión:
def mostrar_lista():
    limpiar_pantalla()
    print(str(mi_lista))

"""
Las listas en Python nos permiten generar una estructura de elementos que permiten representar un mismo contenido, ordenado.
Nos permiten definir una lista de elementos del mismo 
tipo o de diferentes tipos, según nuestra necesidad.
Posee una estructura similar a los arrays de elementos JS. Se estructura entre corchetes, donde almacenamos los valores o elementos, separando cada uno de ellos por una coma
"""

mi_lista = ['Argentina', 'Uruguay', 'Chile', 'Venezuela', 'Paraguay']

print("Mi Lista:", mi_lista) # Mi Lista: ['Argentina', 'Uruguay', 'Chile', 'Venezuela', 'Paraguay']

print("Mi Lista: " + str(mi_lista)) # Mi Lista: ['Argentina', 'Uruguay', 'Venezuela', 'Chile', 'Paraguay']

lista_dos = [11, 'Maga', True]

print("Mi Lista: " + str(lista_dos)) # Mi Lista: [11, 'Maga', True]

# Si queremos agregar un elemento a la lista, disponemos del método .append() el cual recibe como parámetro el nuevo elemento a agregar.

# mi_lista.append("Brasil")

# Y para eliminar algún elemento de la lista, el método .remove() nos permite lograr el cometido indicando cuál elemento deseamos eliminar, en un solo paso.

mi_lista.remove('Chile')
print("Mi lista" + str(mi_lista))

def agregar_elemento():
    nuevo_pais = input("Ingresa un nuevo país: ")
    mi_lista.append(nuevo_pais)
    mostrar_lista()

# Para tener un mayor control de diferentes posibles situaciones, podemos controlar la operación de eliminación, integrando el uso de try -except, por si el elemento no existe o no se ha escrito correctamente.

def quitar_elemento():
    a_quitar = input("Ingresa el país a quitar: ")
    if (a_quitar != ''):
        # quita un elemento de la lista por su nombre
        try:
            mi_lista.remove(a_quitar)
            mostrar_lista()
            print("🟡 Se quitó a " + a_quitar + " de la lista.")

        except ValueError:
            limpiar_pantalla()
            print("⛔️ No se encontró el país indicado:", a_quitar)
            
    else:
        limpiar_pantalla()
        print("⛔️ No se encontró el país indicado. " + a_quitar)


# agregar_elemento()

# quitar_elemento()

print(len(mi_lista))

##---------------------------------------##

# Métodos en Listas

"""
* insert(index, element): Inserta un elemento en una posición específica de la lista.
* pop(index): Elimina y retorna el elemento en la posición especificada.
* extend(iterable): Extiende la lista agregando los elementos del iterable (otra lista, tupla, cadena, etc.).
* index(element): Encuentra el índice de la primera ocurrencia del elemento especificado.
* count(element): Cuenta el número de veces que aparece un elemento en la lista.
* sort(): Ordena la lista en su lugar en orden ascendente.
* reverse(): Invierte el orden de los elementos en la lista.
* clear(): Elimina todos los elementos de la lista
"""

lista_tres = ['Francia', 'España', 'Portugal', 'Inglaterra', 'Italia']

# lista_tres.insert(2, 'Irlanda')

# pais = lista_tres.pop(4) # ['Francia', 'España', 'Irlanda', 'Portugal', 'Italia'] Inglaterra 

# index = lista_tres.index('Italia') # 4

# print(lista_tres, pais, index) # ['Francia', 'España', 'Irlanda', 'Portugal', 'Inglaterra', 'Italia'] 

lista_tres.sort(reverse=True)
# lista_tres.reverse()

# print(lista_tres.count('Portugal')) # 1 

lista_tres.clear()

print(lista_tres) # ['Francia', 'España', 'Irlanda', 'Portugal', 'Inglaterra', 'Italia'] 


# parecido al concat de js:
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits, cars) # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo'] ['Ford', 'BMW', 'Volvo']

##-----------------------------------##

"""El método .pop() en Python, se utiliza para remover un elemento de una lista, definiendo su ID o índice.
Veamos un ejemplo a continuación:Para ello, creamos una función que nos retorne True o False si un valor 
enviado por parámetro puede convertirse o no en un número.

Luego definimos una función que nos permita remover un elemento de la lista, a través de su ID. Solicitamos el ID por input(), y validamos con la función convertir_a_nro() si lo ingresado es un no un ID. Si retorna True, entonces removemos el elemento de la lista, utilizando .pop()
"""

def convertir_a_nro(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def quitar_elemento_por_id():
    a_quitar = input("Ingresa el ID del elemento a quitar: ")
    if (convertir_a_nro(a_quitar)):
        try:
            mi_lista.pop(int(a_quitar))
            mostrar_lista()
            print("🟡 Se quitó el ID " + a_quitar + " de la lista.")

        except ValueError:
            limpiar_pantalla()
            print("⛔️ No se encontró el ID indicado:", a_quitar)
        except:
            limpiar_pantalla()
            print("⛔️ El indice esta fuera de rango:", a_quitar)
    else:
        limpiar_pantalla()
        print("⛔️ Debes ingresar un ID válido.")

quitar_elemento_por_id()

# print(mi_lista[2:4])









