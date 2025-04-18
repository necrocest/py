"""
formula= 2(b.h)
"""

def perimeter(b,h):
    perimetro = 2*(b + h)
    print(f"su perimetro es: ", {perimetro})
    return perimetro
b=float(input("ingrese la base: "))
h=float(input("ingrese la altura: "))
perimeter(b,h)
