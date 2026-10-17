###
# EXERCICIS
###

#.pop surt examen
# Exercici 1: El missatge secret
# Donada la llista següent:
missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
# Fent servir slicing i concatenació, crea una llista nova que contingui només
# el missatge "secret".

secret = missatge[5:11] #Eso es slicing: "coger un trozo de la lista"
print(secret) 
'-----------------------------------------------------------------------------------------------------'

# Exercici 2: Intercanvi de posicions
# Donada la llista següent:
nombres = [10, 20, 30, 40, 50]
# Intercanvia la primera i l'última posició fent servir només l'assignació per índex.
primer = nombres[0]
nombres[0]= nombres[4]
nombres[4]=primer
print(nombres)

#tambien prodriamos haber hecho:
nombres[0], nombres[-1] = nombres[-1], nombres[0] #el index [-1] indica la ultima posicio de la lista
'---------------------------------------------------------------------------------------------'
# Exercici 3: L'entrepà de llistes
# Donades les llistes següents:
pa_de_dalt = ["pa de dalt"]
ingredients = ["pernil", "formatge", "tomàquet"]
pa_de_sota = ["pa de sota"]
# Crea una llista anomenada entrepa que contingui, en aquest ordre, el pa de dalt,
# els ingredients i el pa de sota.

entrepa = pa_de_dalt + ingredients + pa_de_sota #concatenem lista
print(entrepa)

#tambe es pot fer amb:
entrepa1 = []
entrepa1.append(pa_de_dalt[0])#afegir un element al final de llista
entrepa1.extend(ingredients)#afegir varios elements 
entrepa1.append(pa_de_sota[0])

'----------------------------------------------------------------------------------------'
# Exercici 4: Duplicar una llista
# Donada una llista:
llista = [1, 2, 3]
# Crea una llista nova que contingui duplicats els elements de la llista original.
# Exemple: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

llista = [1, 2, 3]
llista_duplicada = llista[:]   # copia
llista_duplicada.extend(llista)
print(llista)          # [1, 2, 3]
print(llista_duplicada) # [1, 2, 3, 1, 2, 3]

# Exercici 5: Extreure l'element central
# Donada una llista amb un nombre senar d'elements, extreu-ne l'element central
# fent servir slicing.
# Exemple: llista = [10, 20, 30, 40, 50] -> L'element central és 30

central = llista[2:3]

# Exercici 6: Inversió parcial
# Donada una llista, inverteix-ne només la primera meitat (fent servir slicing
# i concatenació).
# Exemple: llista = [1, 2, 3, 4, 5, 6] -> Resultat: [3, 2, 1, 4, 5, 6]