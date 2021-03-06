def input_nums():
    global num1
    global num2
    num1=int(input(" Número_1: "))
    num2=int(input(" Número_2: "))

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

def exponencial(num1,num2):
    return num1**num2

operaciones = {"1":"Suma",
              "2":"Resta",
              "3":"Multiplicación",
              "4":"Divisón",
              "5":"Exponencial"}

print("¿Qué operación quiere realizar?")
for operacion in operaciones:
    print(" " + operacion + ") " + operaciones[operacion])
operacion=(input("Seleccione una opción: "))

try:
    if operacion == "1":
        print("\nSUMA: Número_1 + Número_2")
        input_nums()
        print(" => " + str(num1) + " + " + str(num2) + " = " + str(suma(num1,num2)))
    elif operacion == "2":
        print("\nRESTA: Número_1 - Número_2")
        input_nums()
        print(" => " + str(num1) + " - " + str(num2) + " = " + str(resta(num1,num2)))
    elif operacion == "3":
        print("\nMULTIPLICACIÓN: Número_1 * Número_2")
        input_nums()
        print(" => " + str(num1) + " * " + str(num2) + " = " + str(multiplicacion(num1,num2)))
    elif operacion == "4":
        print("\nDIVISIÓN: Número_1 / Número_2")
        input_nums()
        print(" => " + str(num1) + " / " + str(num2) + " = " + str(division(num1,num2)))
    elif operacion == "5":
        print("\nEXPONENCIAL: Número_1 ^ Número_2")
        input_nums()
        print(" => " + str(num1) + " ^ " + str(num2) + " = " + str(exponencial(num1,num2)))

except Exception as e:
    print("\n<<< OPERACIÓN DESCONOCIDA (" + str(e) + ") >>>")
