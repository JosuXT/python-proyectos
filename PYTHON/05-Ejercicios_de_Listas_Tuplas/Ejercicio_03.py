
"""
Ejercicio_3_Listas y Tuplas

Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
mensaje En <asignatura> has sacado <nota> donde <asignatura> es
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
notas introducidas por el usuario.

"""
# Lista con las asignaturas
asignatura = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista vacía para ir guardando las notas
notas = []

# Bloque 1: Recorremos cada asignatura y guardamos su nota
for a in asignatura:
    nota = input(f"¿Qué nota has sacado en {a}? ")
    notas.append(nota)

# Bloque 2: Mostramos cada asignatura junto con su nota correspondiente
for i in range(len(asignatura)):
    print(f"En {asignatura[i]} has sacado {notas[i]}")
