# saludo = "Hola "
# nombre = input('ingrese su nombre:')

#print(saludo+nombre)


num1 = int(input("Primer trimestre: "))
num2 = int(input("Segundo trimestre: "))
num3 = int(input("Tercer trimestre: "))


prom = (num1 + num2 + num3)/3



print("el promedio es %.2f"%prom)

if(prom > 6):
	print("aprobado")
else:
	print("desaprobado")