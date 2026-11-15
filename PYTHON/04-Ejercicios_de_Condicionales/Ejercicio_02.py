
"""

Ejercicio_2_condicionales

Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas

"""

contrasena_guardada = "pepe1234"
contrasena_usuario  = input("intruduce la contraseña: ")

if contrasena_usuario.lower() == contrasena_guardada.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña no coincide.")