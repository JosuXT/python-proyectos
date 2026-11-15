
"""
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.

"""


#  Pedimos los tres datos
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
años = int(input("Introduce el número de años: "))

#  Creamos un bucle que dé tantas vueltas como 'años'
for i in range(años):
    
    # Calculamos el nuevo capital para ese año
    cantidad = cantidad + (cantidad * interes / 100)
  
    print(f"Año {i + 1}: el capital obtenido es {cantidad:.2f} euros")