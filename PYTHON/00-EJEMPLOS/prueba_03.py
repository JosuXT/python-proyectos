"""
Ejercicio 18: tipo examen, “Notas de la clase”

Este es del mismo estilo que el de la caja, pero mezclando cadenas con el menú. Vamos a seguir con vuestro acuerdo: te doy la estructura con huecos, tú intentas rellenar lo que puedas y yo reviso sin perfeccionismos.

Enunciado: Escribe un programa que gestione las notas de una clase:

Muestre este menú en bucle hasta que el usuario elija salir:
1 - Añadir alumno
2 - Ver estadísticas
3 - Salir
Con la opción 1, pida el nombre del alumno y su nota. La nota debe estar entre 0 y 10 (ambas incluidas); si no, volver a pedirla hasta que sea válida. Después debe:
Sumar la nota al total y contar el alumno.
Si la nota es >= 5, contarlo como aprobado; si no, como suspenso.
Si la nota es mayor que la mejor nota hasta ahora, guardar esa nota y el nombre del alumno (en mayúsculas).
Con la opción 2, si no hay alumnos, mostrar Aún no hay alumnos. Si los hay, mostrar:
Número de alumnos
Aprobados y suspensos
Nota media con dos decimales
El mejor alumno y su nota
Con la opción 3, mostrar Hasta pronto y terminar.
Con cualquier otra opción, mostrar Opción no válida.



Conceptos clave
Varias variables de estado antes del bucle: total, contador, aprobados, suspensos, mejor nota y mejor nombre. Todas se conservan entre vueltas del menú.
Mejor nota inicial: empieza en -1 (o en 0) para que cualquier nota válida la supere la primera vez. Piensa por qué -1 es más seguro que 0.
Validación de rango: el while True interno sale solo si 0 <= nota <= 10. Python permite escribir la comparación encadenada.
Media: total / contador, solo si contador > 0 (si no, dividirías entre cero).
.upper() para guardar el nombre del mejor alumno en mayúsculas.

total = 0
contador = 0
aprobados = 0
suspensos = 0
mejor_nota = -1
mejor_nombre = ""

while True:
    print("1 - Añadir alumno")
    print("2 - Ver estadísticas")
    print("3 - Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")

        while True:
            nota = float(input("Nota: "))
            if 0 <= nota <= 10:
                break

        total += nota
        contador += 1

        if nota >= 5:
            aprobados += 1
        else:
            suspensos += 1

        if nota > mejor_nota:
            mejor_nota = nota
            mejor_nombre = nombre.upper()

    elif opcion == "2":
        if contador == 0:
            print("Aún no hay alumnos")
        else:
            print(f"Alumnos: {contador}")
            print(f"Aprobados: {aprobados}")
            print(f"Suspensos: {suspensos}")
            print(f"Media: {total / contador:.2f}")
            print(f"Mejor alumno: {mejor_nombre} con {mejor_nota}")

    elif opcion == "3":
        print("Hasta pronto")
        break

    else:
        print("Opción no válida")

"""

#tabla de multiplicar
          
for a in range (1,11):
    for b in range (1,11):
        result = a * b
        print (f" {a} x {b} = {result}")
print()

#tabla de multiplicar pero que pide numero al usuario

# 1. Pedimos el número y lo convertimos a entero con int()
num_user = int(input("Dime tu número: "))

# 2. Un solo bucle del 1 al 10
for i in range(1, 11):
    # Multiplicamos (*) el número del usuario por cada vuelta del bucle
    resultado = num_user * i
    print(f"{num_user} x {i} = {resultado}")

print()


#triangulo

num = int(input("Introduce tu número: "))

# Bucle exterior: controla cada fila (de 1 hasta num)
for i in range(1, num + 1):
    # Bucle interior: imprime tantos asteriscos como el número de fila (i)
    for o in range(i):
        print("*", end=" ")
    # Salto de línea al terminar la fila
    print()



        

