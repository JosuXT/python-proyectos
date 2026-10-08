"""
Ejercicio_8
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.
"""

precio = input ("introdcue el precio del producto con dos decimales: ")

separar = precio.split (".")
precio_entero = separar[0]
precio_decimal = separar [1]

print (f"parte entera: {precio_entero}")
print (f"parte decimal: {precio_decimal}")


