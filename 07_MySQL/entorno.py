# Variables de entorno y MySQL

'''
Cuando hablamos de variables de entorno, nos referimos 
a la creación valores externos al código de un programa 
que proporcionan información sobre el entorno en el que 
se está ejecutando la aplicación. 
Estas variables son configuraciones externas que pueden 
afectar el comportamiento de un programa sin necesidad 
de cambiar su código fuente


Un sistema operativo suele tener variables de entorno donde se referencian diferentes tipos de información. Por ejemplo, Windows cuenta con variables de entorno del tipo:
● %path%
● %temp%
● %username%

* PATH: Especifica las rutas de los directorios donde Windows buscará ejecutables cuando intentes ejecutar un comando desde la línea de comandos. Cada ruta de directorio está separada por un punto y coma (;).
* TEMP y TMP: Especifican la ruta del directorio temporal que se utiliza para almacenar archivos temporales.
* USERNAME: Contiene el nombre del usuario actual.
* USERPROFILE: Contiene la ruta del directorio del perfil del usuario actual.
* COMPUTERNAME: Contiene el nombre de la computadora.
* SystemRoot: Contiene la ruta del directorio del sistema de Windows.
* HOMEPATH y HOMEDRIVE: Contienen la ruta del directorio personal del usuario
'''
# Podemos validar esto con Python importando el módulo os y el módulo platform, y configurando una variable según el sistema operativo en cuestión:

'''
platform.system() nos permite validar rápidamente si estamos en Windows. 

De ser así, ejecutamos el comando “cls” para que limpie la ventana Terminal y obtenemos el valor de la variable de 
entorno USERNAME.

Caso contrario, ejecutamos “clear” para limpiar la ventana Terminal y obtenemos el valor de la variable de entorno USER
'''

import os
import platform

# print(platform.system())

if platform.system() == 'Windows':
    mi_user = os.environ.get('USERNAME')
    os.system('cls')
else:
    mi_user = os.environ.get('USER')
    os.system('clear')

print('user', mi_user)   

# También podemos establecer variables de entorno directamente desde nuestro sistema Python:

# os.environ["DB_HOST"] = "localhost"
# os.environ["DB_USER"] = "root"
# os.environ["DB_PORT"] = "3306"    

# print(os.environ.get('DB_HOST'))
# print(os.environ)

"""
También contamos con la posibilidad de visualizar todas las variables de entorno configuradas en el sistema operativo donde se ejecuta nuestra aplicación Python.

Para ello, podemos recuperar las mismas en una colección y luego iterarla para visualizar su contenido:
"""

# for key, value in os.environ.items():
#     print(f"{key}: {value}")

##-------------------------------------------##

# Python cuenta también con una funcionalidad la cual nos permite utilizar un archivo .env para definir variables de entorno y, luego, utilizar la librería python-dotenv para cargarlas en nuestra aplicación:

from dotenv import load_dotenv

load_dotenv()

print(os.environ.get('DB_HOST'))

# El método os.getenv() nos permitirá también acceder al valor de cada variable de entorno definida en el archivo .env

print(os.getenv('DB_USER'))

##-------------------------------------------##



