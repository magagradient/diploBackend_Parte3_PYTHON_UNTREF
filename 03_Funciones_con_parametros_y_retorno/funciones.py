# Funciones con parámetros

""""
Las funciones con parámetros permiten recibir uno o más argumentos para utilizarlos internamente, realizando tareas u operaciones con estos datos.
En aquellos escenarios donde, por ejemplo, esperamos números para realizar una operación aritmética, 
podemos convertir los mismos para asegurarnos de que los valores son los esperados.
O aplicar el uso de type() previo a realizar la operación aritmética, retornando un resultado o un mensaje alternativo si no son los valores numéricos esperados
"""
def saludar():
    print('Hola boludx')
    print('...')

saludar()

# def sumar(num1, num2):
#     suma = num1 + num2
#     print('La suma es: '+ str(suma))

# sumar(1, 2)
# sumar(-13, 25)

def sumar(num1, num2):
    if type(num1) == int and type(num2) == int:
        suma = num1 + num2
        print('La suma es: '+ str(suma))
    else:
        print('Los parametros tienen que ser numeros')

sumar(3, 2)
sumar(3, '9')


######################################
# Funciones con retorno

"""
Las funciones con retorno utilizan la palabra reservada return para devolver a través de la misma función, una transformación o cálculo realizado. Ten presente que, cualquier código adicional que 
escribamos después de return, no será procesado."""

def limpiar_texto(texto):
    return texto.strip().lower()

frase = limpiar_texto("      Es Un ExTrAñO pArAiSo   ")
print(frase)


def normalizar_nombre(texto):
    if len(texto.strip()) > 0:
        return texto.strip().lower()
    else:
        return 'Ingrese un nombre' 

nombre = normalizar_nombre("      AubReY pLaZa   ")
print(nombre) # aubrey plaza

nombre = normalizar_nombre("   ")
print(nombre) # Ingrese un nombre



