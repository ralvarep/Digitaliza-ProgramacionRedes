##########
# Listas #
##########
lista_numeros= [1, 2, 3]
lista_strings= ["Uno", "Dos", "Tres"]
lista_mixta= [1, "Dos", 3.0]

print("Lista de números")
for item in lista_numeros:
    print(item)
    
print("\nLista de strings")
for item in lista_strings:
    print(item)
    
print("\nLista mixta")
for item in lista_mixta:
    print(item)
    
print("\nLos números son: ", end='', flush=True)
for item in lista_mixta:
    print(item, end=' ', flush=True)

ultimo_lista_numeros=lista_numeros[-1]
ultimo_lista_strings=lista_strings[-1]
ultimo_lista_mixta=lista_mixta[-1]

print("\n\nLos últimos valores de las listas son: " + str(ultimo_lista_numeros) + ", " + str(ultimo_lista_strings) + ", " + str(ultimo_lista_mixta))

    
################
# Diccionarios #
################
diccionario_peliculas= {"Martin Scorsese":"Infiltrados","Francis Ford Coppola":"El Padrino","Javier Fesser":"Campeones"}

print("\nDiccionario de películas")
print(diccionario_peliculas)

print("\nLas claves del diccionario de películas son:")
for item in diccionario_peliculas:
    print(item)
    
print("\nLos valores del diccionario de películas son:")
for item in diccionario_peliculas:
    print(diccionario_peliculas[item])
