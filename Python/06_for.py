lista_nombres = ["Juan",
                 "Pedro",
                 "Luisa",
                 "Edu",
                 "Miguel"]

selected = []

print("Lista de nombres:")
for nombre in lista_nombres:
    print(" " + nombre, end='')
    if nombre.find("a") >= 0:
        print(" <<<< TIENE LA LETRA 'a'", end='')
        selected.append(nombre)
    print()
    
print("\nLista de nombres seleccionados con letra 'a':")
for nombre in selected:
    print(" " + nombre)
