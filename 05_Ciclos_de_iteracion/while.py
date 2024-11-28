# El ciclo while

"""
while loop: Este ciclo nos permite ejecutar una 
estructura de código repetitiva mientras que una 
determinada condición se cumpla.
Como analizamos la condición en la misma línea de 
declaración de while, si esta no se cumple, puede que el 
ciclo while nunca se ejecute
"""
lenguajes = ["C", "C++", "C#", "Python", "GoLang", "JavaScript"]

print(len(lenguajes))

contador = 0

# while contador < 5:
#     print(contador) # 0 1 2 3 4
#     contador += 1


while contador < len(lenguajes):
    contador += 1

    if contador == 2 or contador == 4:
        continue
    
    # print(contador, lenguajes[contador]) 
    print(contador)   
else:
    print('Termino el while')



# contador = 0

# while contador < len(lenguajes):
#     if contador == 3 or contador == 4:
#         contador += 1
#         continue

#     print(lenguajes[contador])
#     contador += 1

# num = 0

# while num < 100:
#     num += 1

#     if num == 51:
#         break

#     print(num)
#     # exit()

# print('sigue')

while True:
    opcion = input('Cual es la opción: ')
    print(type(opcion))

    if int(opcion) == 15:
        break

    if opcion == "15":
        break

