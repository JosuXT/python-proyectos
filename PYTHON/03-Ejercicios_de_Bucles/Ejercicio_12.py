""" 
Ejercicio_12_bucles
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

veces = frase.lower().count(letra.lower())

print(f"La letra '{letra}' aparece {veces} veces en la frase.")