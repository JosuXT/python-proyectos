"""
Ejercicio_3
Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
número de letras que tienen el nombre.

"""

# Pedimos el nombre
nombre = input("¿Cuál es tu nombre? ")

# mayusculas
nombre_mayus = nombre.upper()


cantidad_letras = len(nombre)

print(f"{nombre_mayus} tiene {cantidad_letras} letras.")