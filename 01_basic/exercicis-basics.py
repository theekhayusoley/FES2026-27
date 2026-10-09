###

# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Theekhayu \nCaldes de Montbui")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
enter = int("12345")
floatt = float(enter)
entero = int(3.99)
print(entero) #ha perdut els decimals conservant nomes el primer numero (ineficient, podria haver arrodonit)

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
nom = input("El nom es: ")
edat = int(input("La edat es: "))
alçada = float(input("Altura es: "))
print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {alçada:.2f} metres")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

PI = 3.141592
numero_redondeado = round(PI)
resultado = numero_redondeado // 2 #La divisio entera es fa amb: //
print(resultado)

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

temp_c = float(input("Introdueix la temp en graus celsius: "))
fahren = (temp_c * 9/5) + 32
print(f"La temperatura en graus celcius introduida es: {temp_c:.2f}º que equival a {fahren} fahrenheit")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

total = float(input("El total del compte es de: "))
per_propina = int(input("El total de propina es de: "))
propina = total*per_propina/100
print(f"La comisió es de {propina:.2f} pesetes y el compte total ascens a {total+propina:.2f} euros ")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

contrasenya = input("Introdueix una contrasenya: ")

if len(contrasenya) >= 8: #funcio len diu la cuantitat de caracters que te la variable
	print("Contrasenya vàlida")
else:
	print("Contrasenya no vàlida")