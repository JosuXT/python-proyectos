"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
un descuento del 60%. Escribir un programa que comience leyendo el número de
barras vendidas que no son del día. Después el programa debe mostrar el precio
habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
coste final total.

"""
precio_barra = 3.49
descuento = 0.60
descuento_porcentaje = precio_barra * descuento

barras_vendidas = int(input("Ingrese el número de barras vendidas que no son del día: "))

coste_total = barras_vendidas * (precio_barra - descuento_porcentaje)

print(f"Precio habitual de una barra de pan: {precio_barra:.2f}€")
print(f"Descuento por no ser fresca: {descuento_porcentaje:.2f}€")
print(f"Coste final total: {coste_total:.2f}€")