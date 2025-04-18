"""
Temperatura
Para convertir grados Celsius a Fahrenheit, se utiliza la fórmula F = (C * 9/5) + 32. 
Para convertir grados Fahrenheit a Celsius, se utiliza la fórmula C = (F - 32) * 5/9.
la idea es que se haga viseversa al tiempo
"""
def fahrenheit(f): 
    fahren = (f * 9/5) + 32
    print("Su temperatura en Fahrenheit es : ", fahren)
    return fahren
def celcius(fahren):
    cels = (fahren-32) * 5/9
    print("Su temperatura en celcius es: ", cels)
    return cels
f = float(input("ingres la temperatura en celsius: "))
fahrenheit(f)
celcius(fahren = (f * 9/5) + 32)

