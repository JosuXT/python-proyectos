"""
Ejercicio_9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.

"""

fecha_nac = input ("cual es tu fecha de nacimiento dd/mm/aaaa: " )

separar = fecha_nac.split("/")
dia = separar[0]
mes = separar [1]
anio = separar [2]

print (f"dia de nacimiento: {dia}")
print (f"mes de nacimiento: {mes}")
print (f"año de nacimiento: {anio}")

