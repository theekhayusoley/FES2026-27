###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom = input("Nom del router: ")
ubicacio = input("La seva ubicacio? ")
ports = int(input("Nombre de ports? "))
ences = input("Esta ences: ")
print(f"El nom es: {nom}, esta a: {ubicacio}, te {ports} ports i esta ences?{ences}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_dispo = float(input("Pla de GB? "))
gb_consum = float(input("Consumits? "))
gb_dispo = gb_dispo - gb_consum
print(f"Els GB actuals son: {gb_dispo}")
