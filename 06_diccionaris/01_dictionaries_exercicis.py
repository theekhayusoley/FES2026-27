###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.
estudiant={
    "nom":"Theekhayu",
    "edat": 22,
    "assignatures": ["Calcul", "CICE", "Xarxes"]
    }
print(estudiant["nom"])  
print(estudiant["edat"])  
print(estudiant["assignatures"])

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.

estudiant["edat"]=67
print(estudiant["assignatures"][1])


# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.
estudiant["grau"]="Enginyeria Electronica de Telecomunicacions"
del estudiant["edat"]
print(estudiant)

# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.
print("nom" in estudiant)
print("email" in estudiant)

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".

for clau, valor in estudiant.items():
    print(f"{clau}: {valor}")

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]

# Creamos un diccionario vacío.
# Aquí guardaremos:
# palabra → número de veces que aparece
comptador = {}

# Recorremos la lista palabra por palabra
for paraula in paraules:

    # Comprobamos si esta palabra YA está en el diccionario
    if paraula in comptador:

        # Si ya existe, sumamos 1 a su contador, como que ya estaba creada la palabra en la lista pues solo sumaos el contador
        comptador[paraula] += 1 #comptador["sol"] = comptador["sol"] + 1

    else:

        # Si no existe todavía, la añadimos, entonces la lista pasaria a {"sol":1}, cuando vuelva a encontrarla pues no vuelve a añadir la palabra
        # y empezamos a contarla con 1
        comptador[paraula] = 1

# Mostramos el resultado
print(comptador)
