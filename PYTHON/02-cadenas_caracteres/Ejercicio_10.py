"""
Ejercicio_10

Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta.

"""
cesta_compra = input("Qué productos quieres comprar (separados por comas): ")


cesta_modificada = cesta_compra.replace(",", "\n")

print(cesta_modificada)
