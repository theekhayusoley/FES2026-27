# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("barcelona", "roma", "cracovia", "bangkok", "manila")
llista_ciutats=list(ciutats)
print(llista_ciutats[1])
print(llista_ciutats[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
valors_enters=(1,5,2,6,2,3,9)
llista_valors_enters=list(valors_enters)
quantitat=llista_valors_enters.count(3)
print(f"Apareix el numero 3 un total de {quantitat} vegades")

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.

def ordenar_numeros(tupla_numeros):
    return tuple(sorted(tupla_numeros)) #convertim en tupla perque la funció sorted sempre retorna una llista
tuplaca=(8,6,8,4,2,6,8,0,1)
tupla_ordenada=ordenar_numeros(tuplaca)
print(f"La llista ordenada: {tupla_ordenada}")