
"""

Ejercicio_7_condicionales


Los tramos impositivos para la declaración de la renta en un determinado país son
los siguientes:


"""

# Pedimos la renta anual permitiendo decimales
renta = float(input("Introduce tu renta anual en euros: "))

#  tramos de menor a mayor
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

# Mostramos el resultado final
print(f"Para una renta de {renta}€, te corresponde un tipo impositivo del {tipo}%.")