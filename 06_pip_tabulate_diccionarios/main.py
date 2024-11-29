# Tabulate

"""
Tabulate es un módulo Python en formato de librería el cual nos permite imprimir tablas legibles en la consola a partir de listas de datos o estructuras de datos como diccionarios. 
Dentro de las ventajas de implementarlo, podemos destacar que nos facilita la visualización de datos tabulares con diferentes estilos de formato, como ser:
● tablas Markdown
● reStructuredText
● HTML
y más.

* si queremos visualizar información desde una lista simple, debemos primero reconvertirla a una estructura tabular, la cual debe incluir índices para una mejor visualización. 
"""

lenguajes = ["Python", "JavaScript", "Java", "C++", "Ruby", "Swift", "PHP", "Go", "Rust", "Kotlin"]

from tabulate import tabulate

tabla = [[indice + 1, lenguaje] for indice, lenguaje in enumerate(lenguajes)]

print(lenguajes)

# print(tabulate(tabla))
"""
devuelve:
1  Python
2  JavaScript
3  Java
4  C++
5  Ruby
6  Swift
7  PHP
8  Go
9  Rust
10  Kotlin
"""

# print(tabulate(lenguajes))

print(tabulate(tabla, headers=["id","Lenguaje"]))
"""
devuelve:
id  Lenguaje
----  ----------
 1  Python
 2  JavaScript
 3  Java
 4  C++
 5  Ruby
 6  Swift
 7  PHP
 8  Go
 9  Rust
 10  Kotlin
"""

# Los formatos predeterminado y keys tienen una estructura similar, por lo tanto casi que no veremos diferencias sustanciales entre ellos.

print(tabulate(tabla, headers=["id","Lenguaje"], tablefmt="keys"))

# Los formatos html entrega una estructura de tabla HTML con encabezado y cuerpo:

print(tabulate(tabla, headers=["id","Lenguaje"], tablefmt="html"))

"""
devuelve:
<table>
<thead>
<tr><th style="text-align: right;">  id</th><th>Lenguaje  </th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;">   1</td><td>Python    </td></tr>
<tr><td style="text-align: right;">   2</td><td>JavaScript</td></tr>
<tr><td style="text-align: right;">   3</td><td>Java      </td></tr>
<tr><td style="text-align: right;">   4</td><td>C++       </td></tr>
<tr><td style="text-align: right;">   5</td><td>Ruby      </td></tr>
<tr><td style="text-align: right;">   6</td><td>Swift     </td></tr>
<tr><td style="text-align: right;">   7</td><td>PHP       </td></tr>
<tr><td style="text-align: right;">   8</td><td>Go        </td></tr>
<tr><td style="text-align: right;">   9</td><td>Rust      </td></tr>
<tr><td style="text-align: right;">  10</td><td>Kotlin    </td></tr>
</tbody>
</table>
"""

# El formato github estructura una tabla algo más completa que las anteriores, utilizando el formato markdown para su armado:

print(tabulate(tabla, headers=["id","Lenguaje"], tablefmt="github"))

"""
devuelve:
|   id | Lenguaje   |
|------|------------|
|    1 | Python     |
|    2 | JavaScript |
|    3 | Java       |
|    4 | C++        |
|    5 | Ruby       |
|    6 | Swift      |
|    7 | PHP        |
|    8 | Go         |
|    9 | Rust       |
|   10 | Kotlin     |
"""









