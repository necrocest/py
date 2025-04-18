"""
La función ord() es especialmente útil cuando necesitas 
trabajar con caracteres y sus valores numéricos, por ejemplo, 
en algoritmos de cifrado, ordenación de caracteres, o simplemente 
para entender la representación interna de los caracteres
"""
caracter = str(input("ingrese el caracter del cual quiere saber el valor acsii: "))
valor_acssi = ord(caracter)
print("el valor del caracter es: ", valor_acssi)