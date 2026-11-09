
"""
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


"""

# Bucle para cada tabla (del 1 al 10)
for i in range(1, 11):
    print(f"--- TABLA DEL {i} ---")
    
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    
    print()
    