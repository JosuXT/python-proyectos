"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión.

"""
cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en porcentaje): "))
anios = int(input("Ingrese el número de años: "))

capital_obtenido = cantidad * (1 + interes_anual / 100) ** anios
print(f"El capital obtenido en la inversión es: {capital_obtenido}")
