"""
Nivel 1, Ejercicio 1: Ficha personal

Enunciado: Escribe un programa que pregunte al usuario su nombre, su ciudad y su edad, y después muestre por pantalla una sola frase con este formato:


nombre  =   input("introduce tu nombre: ")
ciudad  =   input("introduce tu ciudad: ")
edad    =   input("introduce tu edad: ")

print (f"Hola, me llamo {nombre}, vivo en {ciudad} y tengo {edad} años.")
"""
#===============================================================================================================================================================================

"""
Nivel 1, Ejercicio 2: Control de la salida con sep y end

Enunciado: Escribe un programa que pida al usuario tres palabras (una por cada input) y muestre por pantalla:

Las tres palabras en una sola línea separadas por guiones, con print y sin usar f-strings. Ejemplo: sol-luna-estrella
Las tres palabras en una sola línea, pero usando tres print distintos. Ejemplo: sol luna estrella
Un mensaje final que termine con !!! en la misma línea, sin usar + ni f-strings.


#Bloque 1: pedir las tres palabras
p1 = input("Introduce la primera palabra: ")
p2 = input("Introduce la segunda palabra: ")
p3 = input("Introduce la tercera palabra: ")

#Bloque 2: salida con guiones (un solo print)
print(p1, p2 ,p3, sep=("-"))

#Bloque 3: salida en una línea con tres prints
print(p1, end=(" "))
print(p2, end=(" "))
print(p3)

#Bloque 4: mensaje final con !!!
print("Qué bien", end=" !!!\n")

"""

#===============================================================================================================================================================================

"""
Nivel 2, Ejercicio 3: Tipos de datos y conversión

Enunciado: Escribe un programa que pida al usuario dos números enteros y muestre por pantalla:

Su suma, en una frase como La suma de 4 y 7 es 11.
Los tipos de dato que devuelve input() antes de convertir, con una frase como Lo que devuelve input es de tipo <class 'str'>.



a = input(" Introduce el primer número numero 1: ")
b = input("Introduce el primer número numero 2: ")
print("Lo que devuelve input es de tipo", type(a))

suma = int(a) + int(b)

print (f"la suma de {a} y {b} el resultado de la suma es : {suma} ")

"""
#===============================================================================================================================================================================

"""
Nivel 3, Ejercicio 4: Operadores aritméticos

Enunciado: Pide al usuario dos números enteros, a y b, y muestra:

La división normal (a / b)
El cociente entero (a // b)
El resto (a % b)
a elevado a b



a = int(input(" Introduce el primer número numero 1: "))
b = int(input("Introduce el primer número numero 2: "))

division    = (a/b)
cociente    = (a//b)
resto       = (a%b)
elevado     = (a**b)

print(f"{a} / {b} = {division}")
print(f"{a} // {b} = {cociente}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** {b} = {elevado}")
"""

#===============================================================================================================================================================================

"""
Nivel 3, Ejercicio 5: Fórmula con varios pasos

Enunciado: Pide al usuario el radio de un círculo (puede tener decimales) y muestra su área y su perímetro, con dos decimales. Usa 3.1416 como valor de pi.
Conceptos clave
Decimales: usa float() en vez de int() para aceptar números como 2.5.

Área = pi x radio², 

perímetro = 2 x pi x radio.

Dos decimales en una f-string: {valor:.2f}, como viste en tus apuntes ({pi:8.2f}), pero sin la anchura.
Prioridad de operadores: ** se evalúa antes que *, así que radio**2 ya hace lo que necesitas sin paréntesis.



radio = float(input("Dime el radio de un circulo (puede tener decimales): "))

pi = 3.1416
area = (pi * radio ** 2)
perimetro = (2 * pi * radio)

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")


"""
#===============================================================================================================================================================================

"""
Nivel 4, Ejercicio 6: Cadenas (índices y subcadenas)

Enunciado: Pide al usuario una palabra de al menos 4 letras y muestra:

La primera letra
La última letra
Las dos primeras letras
La palabra al revés
El número de letras

Conceptos clave
Índices: el primer carácter es c[0] y el último es c[-1].
Subcadenas: c[i:j] va desde i hasta j-1. Si omites i, empieza desde el principio.
Invertir: c[::-1].
len(c) devuelve el número de caracteres.



palabra = input("introduce tu palabra: ")

print(f"Primera: {palabra[0]}")
print(f"Última: {palabra[-1]}")

print(f"Dos primeras: {palabra[0:2]}")
print(f"Dos ultimas: {palabra[-2:]}")

print(f"Al revés: {palabra[::-1]}")
print(f"Letras: {len(palabra)}")

"""


#===============================================================================================================================================================================

""" 

Nivel 4, Ejercicio 7: Frase con upper, split, replace y find

Este es el enunciado pendiente. Te lo dejo otra vez para que lo tengas a mano:

Enunciado: Pide al usuario una frase y muestra:

La frase en mayúsculas
El número de palabras que tiene
La frase con todas las a sustituidas por *
La posición de la primera e (o -1 si no hay ninguna)

Ejemplo con Me gusta la pera:

ME GUSTA LA PERA
Palabras: 4
Me gust* l* per*
Primera e: 1



frase = input("Introduce tu palabra: ")

print(frase.upper())
print(f"Palabras: {len(frase.split())}")
print(frase.replace("a","*"))
print(f"Primera e: {frase.find("e")}")


"""
#===============================================================================================================================================================================
"""
Nivel 5, Ejercicio 8: Condicionales con if/elif/else

Enunciado: Pide al usuario una nota (puede tener decimales) y muestra su calificación:

Menor que 5: Suspenso
Desde 5 hasta menos de 7: Aprobado
Desde 7 hasta menos de 9: Notable
Desde 9 hasta 10: Sobresaliente
Si la nota es menor que 0 o mayor que 10: Nota no válida


Ejemplos: 4.5 → Suspenso, 7 → Notable, 11 → Nota no válida.

Conceptos clave
if / elif / else evalúa las condiciones en orden y ejecuta solo la primera que sea True.
Orden de las condiciones: si ya has descartado los valores menores que 5 en un if anterior, en el elif no hace falta volver a comprobarlo.
Validar primero: la comprobación de nota no válida conviene ponerla en el primer if, para que las demás no se ejecuten con valores absurdos.
or une condiciones: nota < 0 or nota > 10.



nota = float(input("Introduce la nota: "))

if nota < 0 or nota > 10:
    print("Nota no válida")
elif nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")


"""
#===============================================================================================================================================================================
"""
Nivel 5, Ejercicio 9: Condicionales con and y varios datos

Enunciado: Pide al usuario su edad y si tiene carnet de conducir (si o no). Muestra:

Si tiene 18 años o más y tiene carnet: Puedes conducir
Si tiene 18 años o más y no tiene carnet: Necesitas sacarte el carnet
Si tiene menos de 18: Eres menor de edad

Ejemplos: 20 y si → Puedes conducir, 20 y no → Necesitas sacarte el carnet, 15 y si → Eres menor de edad.

Conceptos clave
and exige que se cumplan las dos condiciones: edad >= 18 and carnet == "si".
Comparar cadenas: usa == con comillas. Para no depender de mayúsculas, aplica .lower() al leer el dato.
Orden: si compruebas primero edad < 18, en los siguientes elif ya sabes que es mayor de edad.

edad = int(input("Introduce tu edad: "))
carnet = input("¿Tienes carnet de conducir? (si/no): ").lower()

if edad < 18:
    print("Eres menor de edad")
elif carnet == "si":
    print("Puedes conducir")
else:
    print("Necesitas sacarte el carnet")

    """
#===============================================================================================================================================================================
"""
Nivel 5, Ejercicio 10: condicionales anidados

Enunciado: Pide al usuario un número entero y muestra:

Si es par y positivo: Par positivo
Si es par y negativo: Par negativo
Si es impar: Impar
Si es 0: Cero

Ejemplos: 4 → Par positivo, -6 → Par negativo, 7 → Impar, 0 → Cero.

Conceptos clave
Par: numero % 2 == 0.
Cuidado con el 0: es par, pero el enunciado lo trata aparte. Compruébalo primero.
Anidar: puedes poner un if dentro de otro, con 4 espacios más de indentación.



numero = int(input("Introduce un número entero: "))

if numero == 0:
    print("Cero")
elif numero % 2 != 0:
    print("Impar")
else:
    if numero > 0:
        print("Par positivo")
    else:
        print("Par negativo")
"""
#===============================================================================================================================================================================

"""
Nivel 6, Ejercicio 11: bucle for con range

Terminamos los condicionales y empezamos con bucles, lo que más pesa en un examen. Este es más corto para entrar en materia.

Enunciado: Pide al usuario un número entero n y muestra los números del 1 al n, todos en una sola línea separados por espacios.

Conceptos clave
range(inicio, fin) llega hasta fin - 1. Para incluir n, el final debe ser n + 1.
for i in range(...) repite el bloque indentado, y i toma cada valor.
print(i, end=" ") deja un espacio en lugar de salto de línea (lo viste en el Ejercicio 2).

n = int(input("Introduce un número entero: "))

for i in range(1, n + 1):
    print(i, end=" ")

    """


#===============================================================================================================================================================================

"""

Nivel 6, Ejercicio 12: acumulador con for

Enunciado: Pide al usuario un número entero n y muestra la suma de los números del 1 al n.

Ejemplo con 5: La suma es 15



n = int(input("Introduce un número entero: "))

suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma es {suma}")

"""
#===============================================================================================================================================================================

"""
Nivel 7, Ejercicio 13: while con break

Ahora pasamos a while. Para que no sea solo copiar, te propongo un trato: intenta rellenar solo los huecos y, si te atascas en uno, dime cuál y te doy esa pista.

Enunciado: Pide números al usuario hasta que introduzca 0. Al terminar, muestra la suma de todos los números introducidos (el 0 no cuenta).

Ejemplo con 4, 6, 2, 0:

La suma es 12
Conceptos clave
while True: repite indefinidamente hasta que un break lo corte.
break sale del bucle inmediatamente. Va dentro de un if.
Acumulador otra vez: suma = 0 antes del bucle.
Orden: primero lees el número, luego compruebas si es 0 (y haces break), y solo si no lo es, lo sumas.


suma = 0

while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    suma += num

print(f"La suma es {suma}")
"""
#===============================================================================================================================================================================
""" 
Nivel 7, Ejercicio 14: contador y validación

Enunciado: Pide números al usuario hasta que introduzca 0. Al terminar, muestra cuántos números eran positivos y cuántos negativos (el 0 no cuenta).

Ejemplo con 5, -3, 8, -1, -7, 0:

Positivos: 2
Negativos: 3
Conceptos clave
Contador: como un acumulador, pero sumando 1 en vez del valor: positivos += 1.
Dos contadores empiezan en 0 antes del bucle.
Dentro del bucle: primero break si es 0, luego if num > 0 / else para decidir cuál contador sube.

positivos = 0
negativos = 0

while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    if num > 0:
        positivos += 1
    else:
        negativos += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
"""

#===============================================================================================================================================================================
""" 
Nivel 8, Ejercicio 15: recorrer una cadena con for

Ahora mezclamos bucle, condicional y cadenas, como en un examen.

Enunciado: Pide una frase y muestra cuántas vocales tiene (minúsculas o mayúsculas).

Ejemplo con Me gusta Python:

Vocales: 4
Conceptos clave
for letra in frase: recorre la cadena carácter a carácter.
in con cadenas: letra in "aeiou" es True si la letra es una vocal.
.lower() sobre la frase evita tener que escribir también las mayúsculas.
Contador a 0 antes del bucle.





Cómo se lee
.lower() pasa la frase a minúsculas al leerla. Así A y a cuentan igual y solo necesitas comprobar "aeiou".
contador = 0 antes del bucle, para que no se reinicie en cada vuelta.
for letra in frase: recorre la frase carácter a carácter. En cada vuelta, letra es un solo carácter.
if letra in "aeiou": es True si ese carácter está dentro de la cadena de vocales. Los espacios, consonantes y signos no pasan el filtro.
contador += 1: un contador suma 1 por cada vocal encontrada.
print fuera del bucle, una sola vez al final.
Traza con Me gusta Python

Frase en minúsculas: me gusta python



frase = input("Introduce una frase: ").lower()
contador = 0

for letra in frase:
    if letra in "aeiou":
        contador += 1

print(f"Vocales: {contador}")


"""
#===============================================================================================================================================================================

""" 

Nivel 8, Ejercicio 16: validación con while y contar con for

Enunciado: Pide una contraseña hasta que tenga al menos 6 caracteres. Cuando sea válida, muestra cuántos dígitos contiene.

Ejemplo: si escribes abc (se rechaza), luego ab12 (se rechaza), luego hola2024:

Dígitos: 4
Conceptos clave
while True + break: pides la contraseña en cada vuelta y sales solo si len(clave) >= 6.
len(clave) da el número de caracteres.
letra.isdigit() devuelve True si el carácter es un dígito ("7".isdigit() es True).
Dos fases: primero el while de validación, después el for que cuenta dígitos, ya fuera del while.


Cómo se lee
while True + break: se pide la contraseña una y otra vez. Solo se sale cuando len(clave) >= 6. Si es más corta, el if no se cumple y el bucle vuelve a empezar.
clave sigue existiendo después del while: las variables creadas dentro de un bucle se pueden usar fuera. Por eso el for de abajo la recorre sin problema, y contiene la contraseña válida (la última que escribiste).
contador = 0 va después del while y antes del for, para empezar a contar solo con la contraseña buena.
for letra in clave: recorre la contraseña carácter a carácter.
if letra.isdigit(): es True solo para 0-9. Las letras y símbolos no pasan el filtro.
contador += 1: suma 1 por cada dígito encontrado.
print fuera de los bucles, una sola vez.


while True:
    clave = input("Introduce una contraseña (mínimo 6 caracteres): ")
    if len(clave) >= 6:
        break

contador = 0
for letra in clave:
    if letra.isdigit():
        contador += 1

print(f"Dígitos: {contador}")

"""

#===============================================================================================================================================================================

""" 
Nivel 9, Ejercicio 17: ejercicio tipo examen

Aquí juntamos todo: menú, validación, bucle, condicionales y formato. Es largo, así que lo dividimos en partes. Antes de pedirme el resultado, intenta al menos el Bloque 1 y el Bloque 2: es lo que más te va a servir el día del examen, y yo te lo reviso rápido, sin perfeccionismos.

Enunciado: Escribe un programa de caja de una tienda que:

Muestre este menú en bucle hasta que el usuario elija salir:
1 - Añadir producto
2 - Ver resumen
3 - Salir
Con la opción 1, pida el nombre del producto y su precio (que debe ser mayor que 0; si no, volver a pedirlo hasta que sea válido) y lo añada al total y al contador de productos.
Con la opción 2, muestre el número de productos y el total con dos decimales. Si todavía no hay productos, muestre Aún no hay productos.
Con la opción 3, muestre Hasta pronto y termine.
Con cualquier otra opción, muestre Opción no válida.

Ejemplo de sesión:

Opción: 1
Producto: pan
Precio: 1.5
Opción: 1
Producto: leche
Precio: -2
Precio: 0.9
Opción: 2
Productos: 2
Total: 2.40
Opción: 3
Hasta pronto
Conceptos clave
Bucle principal: while True con el menú dentro y break en la opción 3.
Variables antes del bucle: total = 0 y contador = 0.
Validación anidada: dentro de la opción 1, otro while True que pide el precio hasta que sea > 0.
if / elif / else para las opciones del menú.
Formato: {total:.2f} para dos decimales.


"""

#===============================================================================================================================================================================

total = 0
contador = 0

while True:
    print("1 - Añadir producto")
    print("2 - Ver resumen")
    print("3 - Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Producto: ")
        while True:
            precio = float(input("Precio: "))
            if precio > 0:
                break
        total += precio
        contador += 1
    elif opcion == "2":
        if contador == 0:
            print("Aún no hay productos")
        else:
            print(f"Productos: {contador}")
            print(f"Total: {total:.2f}")
    elif opcion == "3":
        print("Hasta pronto")
        break
    else:
        print("Opción no válida")