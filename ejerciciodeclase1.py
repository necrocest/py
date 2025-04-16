'''
1. Un estudiante desea conocer su desempeño en una materia y 
necesita calcular el promedio de tres calificaciones. 
Escribe un programa que solicite tres notas al usuario y 
calcule su promedio aritmético. Asegúrate de que los valores 
ingresados sean números válidos y estén dentro del rango de 0 a 100.
'''
def new_func():
    print("Promedio De tres Materias")
    def mensaje():
        print("las notas deben ser en decimal de 0.0 a 5.0")
        print("Introduzca sus notas")
    def  operacion_promedio(a, b, c):
        mi_promedio = (a + b + c) / 3
        print("Su promedio es: ", mi_promedio)
        return mi_promedio
    while a < 5:
        mensaje()
        a = float(input("Introduzca la nota 1: "))
        if(0.0 <= a >=5.0): 
            print("su nota es invalida")
        b = float(input("Introduzca la nota 2: "))
        if(0.0 <= b >=5.0):
            print("su nota es invalida")
        c = float(input("Introduzca la nota 3: "))
        if(0.0 <= c >=5.0): 
            print("su nota es invalida")
        operacion_promedio(a, b, c)
new_func()