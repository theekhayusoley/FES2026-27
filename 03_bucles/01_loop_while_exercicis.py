###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
comptador=10
while comptador > 0: #a la que el comptador de 1 pasa a 0, ja no s'executa perque ya no compleix la condició
    print(comptador)
    comptador-=1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

suma=0
comptador=0
while comptador<=20:
    if comptador%2==0: #comprovar si el numero es parell
        suma+=comptador
    comptador+=1
print(suma)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
valor=int(input("Introdueix un valor enter: "))
factorial = 1
comptador = 1
while comptador <= valor:
    factorial *= comptador
    comptador += 1
print(factorial)

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya=''
while len(contrasenya) < 8:
    contrasenya=input("Introdueix una contrasenya de almenys 8 caracters: ")
    if len(contrasenya) < 8:
        print("Torna a provar.")

print("Ja era hora. Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero=int(input("Introdueix un valor: "))
comptador=1
while comptador <=10:
    multiplicacio=numero*comptador
    print(f"{numero} x {comptador} = {multiplicacio}")
    comptador+=1
# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

N = int(input("Introdueix un enter positiu: "))

comptador = 2

while comptador <= N:
    divisor = 2
    es_primer = True

    while divisor < comptador and es_primer:
        if comptador % divisor == 0:
            es_primer = False
        divisor += 1

    if es_primer:
        print(comptador)

    comptador += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
suma = 0
numero = int(input("Introdueix un número enter ( o Introdueix 0 per acabar): "))
while numero != 0:
  suma += numero
  numero = int(input("Introdueix un altre número enter (0 per acabar): "))
print(f"La suma total és: {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
numero=int(input('Introdueix un valor enter positiu: '))
xifres = 0
while numero > 0:
    numero = numero // 10 #es com un desplaçament lateral que va treient valors de la dreta
    cifras += 1
print("El número té", xifres, "xifres") #482 // 10 da 48 y el contador pasa a 1.
                                        #48 // 10 da 4 y pasa a 2.
                                        #4 // 10 da 0 y pasa a 3; el bucle termina.


# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

termes=int(input('Introdueix els valor que vols de Fibonacci: '))
anterior = 0
actual = 1
comptador = 0
while comptador < termes:
    print(anterior)
    siguiente = anterior + actual #En cada vuelta, siguiente suma los dos términos actuales
    anterior=actual #Después avanzamos: anterior toma el valor de actual
    actual=siguiente #actual toma el de siguiente.
    comptador+=1


# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

secret = 7  

valor=int(input("Intenta trobar el valor secret: "))
while valor != secret:
    
    if valor > secret:
        print("El secret es mes petit")
    else:
        print("T'has passat")
    valor=int(input("No has encertat: "))

print("Molt bé, era el numero 7")

          
