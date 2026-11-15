
"""

Ejercicio_3_condicionales

Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.


"""

dividendo   = float(input("Introduce el primer número (dividendo): "))
divisor     = float(input("Introduce el segundo número (divisor): "))

if divisor == 0:
    print("Error: No se puede dividir entre cero.")
else:
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)