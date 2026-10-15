
################################################################

prueba1 = int(input("escribe tu numero1: "))
prueba2 = int(input("escribe tu numero2: "))
resultado = (prueba1 + prueba2)
print (resultado)

################################################################

frase = input ("introduce tu frase: ")
vocal = input ("introduce tu vocal: ")
frase_corregida = frase.replace(vocal,vocal.upper())
print (frase_corregida)

################################################################

fecha_nac = input("introduce_tu_fecha")
separar = fecha_nac.split("/")
dia = separar [0]
mes = separar [1]
año = separar [2]

print (f"tu dia es {dia}" )
print (f"tu dia es {mes}" )
print (f"tu dia es {año}" )

################################################################

correo = input("introduce tu correo : ")
remplazo = correo.split("@")
print ("su correo nuevo es", remplazo[0] + "@ceu.es")


##############################################################

precio = input("introduce el precio en decimal con (,): ")
split = precio.split(",")
precio_int = split[0]
precio_decimal = split [1]
print (f"tu precio entero es : {precio_int}")
print (f"tu precio decimal es: {precio_decimal}")

################################################################

frase = input("introduce tu frase: ")
frase_inversa = frase[::-1]
print (f"tu frase inversa es : {frase_inversa} ")

################################################################


# pedir al usuario
telefono = input("Introduce un número de teléfono (+34-número-extensión): ")

# dividir
partes = telefono.split('-')

# obtenemos los numeros
numero_principal = partes[1]

print(f"El número principal es: {numero_principal}")



