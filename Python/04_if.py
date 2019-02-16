numero=int(input("Número: "))

if numero < 20:
    print("El número "+ str(numero) + " es menor que 20")
elif numero < 40:
    print("El número "+ str(numero) + " es mayor o igual que 20 y es menor que 40")
elif numero < 60:
    print("El número "+ str(numero) + " es mayor o igual que 40 y es menor que 60")
else:
    print("El número "+ str(numero) + " es mayor o igual que 60")
