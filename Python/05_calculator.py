import math

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

def exponencial(num1,num2):
    return math.expnum1^num2 

num1=int(input("Número 1: "))
num2=int(input("Número 2: "))

operacion=(input("¿Qué operación quiere realizar? (+,-,*,/,^): "))

if operacion == "+":
    print(str(num1) + " + " + str(num2) + " = " + str(suma(num1,num2)))
elif operacion == "-":
    print(str(num1) + " - " + str(num2) + " = " + str(resta(num1,num2)))
elif operacion == "*":
    print(str(num1) + " * " + str(num2) + " = " + str(multiplicacion(num1,num2)))
elif operacion == "/":
    print(str(num1) + " / " + str(num2) + " = " + str(division(num1,num2)))
elif operacion == "^":
    print(str(num1) + " ^ " + str(num2) + " = " + str(exponencial(num1,num2)))
else:
    print("Operación desconocida")
