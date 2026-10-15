"""
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

"""
producto = input("Escribe el producto: ")
precio = float(input("Escribe el precio: "))
unidades = int(input("Escribe las unidades: "))

# Calculamos el coste total multiplicando
coste_total = unidades * precio

# Tu f-string (¡que está perfecta!)
print(f"El producto {producto} tiene el precio {precio:09.2f}, el cual tiene {unidades:03d} unidades y el coste total es {coste_total:011.2f}")