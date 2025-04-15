""" 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
c. Utilizar un vector para representar la mochila."""


mochila = ['Pan', 'Capa', 'Mapa', 'Cristal Kyber', 'Sable de luz', 'Comlink']

def usar_la_fuerza(mochila, contador=0):

    if not mochila:
        return False, contador

    objeto = mochila[0]
    
    if objeto == 'Sable de luz':
        return True, contador

    return usar_la_fuerza(mochila[1:], contador + 1)

# Guarda dos valores devueltos por la función en dos variables separadas para poder usarlas después.
encontrado, objetos_sacados = usar_la_fuerza(mochila)


if encontrado:
    print(f"¡La Fuerza está contigo, joven padawan! Encontraste el sable de luz después de sacar {objetos_sacados} objetos.")
else:
    print("La Fuerza no fue suficiente... No hay sable de luz en la mochila.")
