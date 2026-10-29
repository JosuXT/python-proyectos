
"""
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.


"""
#se escribe por lineas

num= input("introduce tu numero")

for num in range (1,10+1,2):
    for j in range(num,0,-2):
        print (j,end=" ")
    print ("")