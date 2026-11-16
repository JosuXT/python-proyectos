
"""

Ejercicio_6_condicionales


Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.


"""


# Pedimos los datos y los convertimos a mayúsculas con .upper()
nombre = input("Introduce tu nombre: ").upper()
sexo = input("Introduce tu sexo (M para mujer / H para hombre): ").upper()

# Extraemos la primera letra del nombre
inicial = nombre[0]

# Evaluamos las dos condiciones del Grupo A agrupadas entre paréntesis
if (sexo == "M" and inicial < "M") or (sexo == "H" and inicial > "N"):
    print("Te corresponde el Grupo A.")
else:
    print("Te corresponde el Grupo B.")