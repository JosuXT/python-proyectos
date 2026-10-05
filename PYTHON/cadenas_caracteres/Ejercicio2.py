"""
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y
después muestre por pantalla el nombre completo del usuario tres veces, una con
todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
primera letra del nombre y de los apellidos en mayúscula. El usuario puede
introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
nombre_completo = input("coloca el nombre completo: ")
##print (nombre_completo)
numero = 3


print ("NORMAL")
for i in range(numero):
    print (nombre_completo)
print()   

print ("minuscula")
for i in range(numero):
    print (nombre_completo.lower())

print()   

print ("Mayuscula")
for i in range(numero):
    print(nombre_completo.upper())
print() 

print ("Primera letra Mayuscula")
for i in range(numero):
    print(nombre_completo.title())