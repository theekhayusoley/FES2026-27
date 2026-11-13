###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
for numero in range(2, 21, 2):  # range(inici, final, pas)
  print(numero)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
suma=0
for valor in numeros:
  suma+=valor
longitud=len(numeros)
mitjana=suma/longitud
print(f"La mitjana es: {mitjana}")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
numeros1 = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
maxim=0
for valor in numeros1:
  if valor>maxim:
    maxim=valor
print(f"El valor maxim es: {maxim}")


# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
llista_llarga=[]
for lletres in paraules:
  if len(lletres)>=5: #Mes gran o igual a 5 lletres, aixi puc veure si afegeix diferentes cadenes
    llista_llarga.append(lletres)
print(llista_llarga)


# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
lletra = input("Introdueix alguna lletra: ").lower() #.lower converteix en minuscula si o si
comptador = 0
for paraula in paraules:
  if paraula.lower().startswith(lletra):  #comprova si la paraula comença amb el contingut de "lletra", retorna un False o True
    comptador += 1
print(f"Hi ha {comptador} paraules que comencen per la lletra {lletra}")

# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
suma_tensions=0
for tensio in tensions:
  suma_tensions+=tensio
mitjana=suma_tensions/len(tensions)
print(f"La mitjana de tensions es: {mitjana}V")


# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
tensio=12
resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
for ohms in resistencies:
  intensitat=tensio/ohms
  print(f"La tensio de {tensio}V que cau en la resistecia de {ohms} Ohms genera una intensistat de {intensitat:f}A")




# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
comptador=0
for valors in nivells_soroll:
  if valors>-80:
    comptador+=1
print(f"El numero de nivells que superen els -80dBm son: {comptador}")


# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
bits_diferents = 0
for i in range(len(bits_transmesos)):#i recorre una longitud de la llista de bits transmesos vegades
    if bits_transmesos[i] != bits_rebuts[i]:#comparem el index de cada llista per veure si son iguals
        bits_diferents += 1
taxa_error = bits_diferents / len(bits_transmesos)
print("Bits diferents:", bits_diferents)
print("Taxa d'error:", taxa_error)

# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
for freq in frequencies:
  periode=1/freq
  print(f"El periode de la frequencia {freq} Hz es: {periode}s ")
