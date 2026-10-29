
"""
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas.
"""


num = int(input("Introduce tu numero "))

if num > 0:

 for i in range(1, num + 1, 2):
        print(i, end=", ")

else:
    print ("el numero tiene que ser positivo")

