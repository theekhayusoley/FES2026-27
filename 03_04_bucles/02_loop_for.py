###
# 02 - Bucles (for)
# Permeten executar un bloc de codi repetidament mentre ITERA un iterable o una llista
###

import sys
sys.stdout.reconfigure(encoding="utf-8")


print("\nBucle for:")

# Iterar una llista
# fruites = ["poma", "pera", "mandarina"]
# for fruita in fruites:
#   print(fruita)

# Iterar sobre qualsevol cosa que sigui iterable
# cadena = "marc"
# for caracter in cadena:
#   print(caracter)

# enumerate()

fruites = ["poma", "pera", "mandarina"]
for idx, valor in enumerate(fruites):
  print(f"L'�ndex �s {idx} i la fruita �s {valor}")
# Mostra l'�ndex i el valor de cada element de la llista fruites

# bucles imbricats
# lletres = ["A", "B", "C"]
# numeros = [1, 2, 3]

# for lletra in lletres:
#   for numero in numeros:
#     print(f"{lletra}{numero}")

# Revisar Python Tutor: http://pythontutor.com/visualize.html#mode=edit


# break
# print("\nbreak:")
# animals = ["gos", "gat", "ratol�", "lloro", "peix", "canari"]
# for idx, animal in enumerate(animals):
#   print(animal)
#   if animal == "lloro":
#     print(f"El lloro est? amagat a l'�ndex {idx}")
#     break

# continue
# print("\ncontinue:")
# animals = ["gos", "gat", "ratol�", "lloro", "peix", "canari"]
# for idx, animal in enumerate(animals):
#   if animal == "lloro": continue
#   print(animal)

# Comprensi� de llistes (list comprehension)
# animals = ["gos", "gat", "ratol�", "lloro", "peix", "canari"]
# animals_majus = [animal.upper() for animal in animals]
# print(animals_majus)

# Mostra els n�meros parells d'una llista
# parells = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
# print(parells)

###
# EXERCICIS (for)
###

# Exercici 1: Imprimir n�meros parells
# Imprimeix tots els n�meros parells del 2 al 20 (inclosos) fent servir un bucle for.
# print("\nExercici 1:")

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de n�meros seg�ent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels n�meros fent servir un bucle for.
# print("\nExercici 2:")

# Exercici 3: Buscar el m?xim d'una llista
# Donada la llista de n�meros seg�ent:
# numeros = [15, 5, 25, 10, 20]
# Troba el n�mero m?xim de la llista fent servir un bucle for.
# print("\nExercici 3:")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules seg�ent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui nom�s les paraules amb m�s de 5 lletres
# fent servir un bucle for i list comprehension.
# print("\nExercici 4:")

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules seg�ent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar maj�scules/min�scules).
# print("\nExercici 5:")
