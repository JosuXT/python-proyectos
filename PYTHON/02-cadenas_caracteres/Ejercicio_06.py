"""
Ejercicio_6
Escribir un programa que pida al usuario que introduzca una frase en la consola y
una vocal, y después muestre por pantalla la misma frase pero con la vocal
introducida en mayúscula.

"""

frase = input("introduce tu frase: ")
vocal = input("introduce tu vocal: ")

frase_final = frase.replace(vocal, vocal.upper())

print(frase_final)