"""
Ejercicio_7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
de la arroba @) pero con dominio ceu.es.


"""

correo = input ("introdcue tu correo: ")

partes_correo = correo.split("@")
nuevo_correo = partes_correo[0] + "@ceu.es"

print (f"tu neuvo correo es:{nuevo_correo}")