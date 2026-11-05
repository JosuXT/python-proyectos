
"""
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.

"""

#  Guardamos la contraseña correcta (lo que ya tenías)
password_correcta = "segura1234!"

# Pedimos el primer intento al usuario
intento = input("Introduce la contraseña: ")

#  Mientras (!=) el intento sea DIFERENTE a la contraseña correcta:
while intento != password_correcta:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    # Pedimos la contraseña otra vez (si no volvemos a pedirla dentro, el bucle sería infinito)
    intento = input("Introduce la contraseña: ")

# Si el bucle termina, significa que el usuario ha acertado
print("¡Contraseña correcta! Acceso concedido.")