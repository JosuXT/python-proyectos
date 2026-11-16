
"""

Ejercicio_10_condicionales


Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quiere calcular de forma automática el precio que debe cobrar a sus
clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

"""
# Preguntamos el tipo de pizza y convertimos a minúsculas
print("Bienvenido a la pizzería Bella Napoli.")
tipo = input("¿Quieres una pizza vegetariana? (si/no): ").lower()

# Primer nivel: Evaluamos si es vegetariana o no
if tipo == "si" or tipo == "sí":
    print("\nIngredientes vegetarianos disponibles:")
    print("1 - Pimiento")
    print("2 - Tofu")
    opcion = input("Elige el número de tu ingrediente: ")

    # (solo se ejecuta si dijo que SÍ)
    if opcion == "1":
        ingrediente = "Pimiento"
    elif opcion == "2":
        ingrediente = "Tofu"
    else:
        ingrediente = "Ninguno (opción no válida)"

    print(f"\nHas elegido una pizza VEGETARIANA con: mozzarella, tomate y {ingrediente}.")

elif tipo == "no":
    print("\nIngredientes no vegetarianos disponibles:")
    print("1 - Peperoni")
    print("2 - Jamón")
    print("3 - Salmón")
    opcion = input("Elige el número de tu ingrediente: ")

    # Condicional anidado
    if opcion == "1":
        ingrediente = "Peperoni"
    elif opcion == "2":
        ingrediente = "Jamón"
    elif opcion == "3":
        ingrediente = "Salmón"
    else:
        ingrediente = "Ninguno (opción no válida)"

    print(f"\nHas elegido una pizza NO VEGETARIANA con: mozzarella, tomate y {ingrediente}.")

else:
    print("\nRespuesta no válida. Por favor, responde 'si' o 'no'.")