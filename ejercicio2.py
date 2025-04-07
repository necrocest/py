import math
radio = 30
area_of_circle = math.pi*radio**2
print("el area del circulo es: ",area_of_circle)
circum_of_circle=2*math.pi*radio
print("circum of circle: ", circum_of_circle)
radio_usuer = float(input("ingrese el radio del circulo en metros:" ))
area_of_user = math.pi*radio_usuer**2
print(f"El radio del usuario fue {radio_usuer} m: el area es: {area_of_circle} m2")
