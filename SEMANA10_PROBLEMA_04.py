print("Este codigo esta programado a arrojar el factorial de un nummero entero.")
numero = int(input("Digite el numero que desea factorizar:..."))
fact = 1
for i in range(1,numero+1):
    fact = fact * i
print("El resultado es:...",fact)