"""
Temperatura
Para convertir grados Celsius a Fahrenheit, se utiliza la fórmula F = (C * 9/5) + 32. 
Para convertir grados Fahrenheit a Celsius, se utiliza la fórmula C = (F - 32) * 5/9
"""
def fahrenheit( c ): 
    fahrenheit = (c * 9/5) + 32
    print( "Su temperatura es: ", fahrenheit)
    return fahrenheit
c = float(input("ingres la temperatura en celsius: "))
fahrenheit(c)
