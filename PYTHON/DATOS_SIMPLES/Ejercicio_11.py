"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales.


"""
cantidad = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 0.04

balance_1 = cantidad * (1 + interes)
balance_2 = balance_1 * (1 + interes)
balance_3 = balance_2 * (1 + interes)

print ("resultados:")
print(f"Balance tras el primer año: {balance_1:.2f}")
print(f"Balance tras el segundo año: {balance_2:.2f}")
print(f"Balance tras el tercer año: {balance_3:.2f}")
