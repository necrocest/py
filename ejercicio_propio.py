print("Area de un rectagulo")
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
area = base*altura
print(f"El area es: ", area)

#triangulo

print("Area de un Triangulo")
base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
area = base*altura/2
print(f"El area es: ", area)
if area<100:
    print("Gay")
elif area>100:
    print("gay")
    