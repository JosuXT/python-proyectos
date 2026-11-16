"""
Ejercicio_4
Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
número de letras que tienen el nombre.

"""
# pedir al usuario
telefono = input("Introduce un número de teléfono (+34-número-extensión): ")

# dividir
partes = telefono.split('-')

# obtenemos los numeros
numero_principal = partes[1]

print(f"El número principal es: {numero_principal}")