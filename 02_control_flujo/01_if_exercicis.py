###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
dbm = int(input("Introdueix els dBm de la senyal rebuda: "))
if dbm>-50:
    print("Cobertura excel·lent")
elif dbm>=-67 and dbm<=-50:
    print("Cobertura bona")
elif dbm>=-75 and dbm<-67:
    print("Cobertura feble")
else:
    print("Cobertura molt feble")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
dBm = int(input("Introdueix el la potència óptica de la senyal "))
if dBm>=-27 and dBm<=-8:
    print("Senyal acceptable")
elif dBm>-8:
    print("Senyal massa alta")
else:
    print("senyal massa baixa")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = int(input("Introdueix el consum de dades en GB: "))
if consum > 20:
    print("Has superat el plà màxim :(")
    exces = consum - 20
    print(f"T'has pasat {exces} GB tt ")
else:
    print("De moment estas dintre")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("esta ences el indicador los? (si/no) ").lower() #lower() converteix el text en minuscules
internet = input ("esta ences el indicador internet? (si/no) ").lower()
if los =='si':
    print("Hay que revisar el cable de fibra.")
elif internet == 'no':
    print("Hay que comprobar el servicio del proveedor.")
else:
    print('Tot bé')

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

nivell = int(input(' Introdueix el nivel de bateria de SAI: '))
if nivell > 100 or nivell < 0:
    print('Nivell fora de rang')
elif nivell < 20:
    print('Nivell critic')
elif nivell >=20 and nivell <= 49:
    print('Nivell baix')
elif nivell >= 50:
    print('Nivell suficient')

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introdueix la latència en mil·lisegons: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0 or perdua < 0 or perdua > 100:
    print("Valor fora de rang")
elif latencia <= 30 and perdua <= 1:
    print("Connexió excel·lent")
elif latencia <= 80 and perdua <= 3:
    print("Connexió bona")
elif latencia <= 150 and perdua <= 5:
    print("Connexió acceptable")
else:
    print("Connexió deficient")


# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla = input('introdueix el pla que tens: (bàsic/plus)')
consum = int(input('Introdueix el consum mensual: '))
if consum < 0:
    print('No es posible un consum negatiu Einstein')
elif pla == 'basic':
    if consum > 10:
        gb_addicionals = consum - 10
        cost = 10 + gb_addicionals * 1.50
        print("Cost total:", cost, "euros")
        print("S'ha superat el límit")
    else:
        cost = 10
        print("Cost total:", cost, "euros")
        print("No s'ha superat el límit")

elif pla == "plus":
    if consum > 30:
        gb_addicionals = consum - 30
        cost = 20 + gb_addicionals * 0.75
        print("Cost total:", cost, "euros")
        print("S'ha superat el límit")
    else:
        cost = 20
        print("Cost total:", cost, "euros")
        print("No s'ha superat el límit")
else:
    print('Tipus de pla desconegut')




# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

compte_actiu = input("El compte està actiu? (sí/no): ").lower()

if compte_actiu != "sí" and compte_actiu != "si":
    print("Accés denegat: el compte està desactivat")
else:
    contrasenya = input("Introdueix la contrasenya: ")

    if contrasenya != "python123":
        print("Accés denegat: contrasenya incorrecta")
    else:
        codi = input("Introdueix el codi de doble verificació: ")

        if codi != "456789":
            print("Accés denegat: codi incorrecte")
        else:
            print("Accés permès")

# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router = input("El router està encès? (sí/no): ").lower()

if router != "sí" and router != "si":
    print("Cal encendre el router")
else:
    los = input("L'indicador LOS està encès? (sí/no): ").lower()

    if los == "sí" or los == "si":
        print("Cal revisar el cable de fibra")
    else:
        internet = input(
            "L'indicador d'Internet està encès? (sí/no): ").lower()

        if internet != "sí" and internet != "si":
            print("Cal contactar amb el proveïdor")
        else:
            print("La connexió funciona correctament")

# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

servei_critic = input("La incidència afecta un servei crític? (sí/no): "0).lower()

usuaris = int(input("Quants usuaris estan afectats? "))

alternativa = input("Hi ha una alternativa de connexió? (sí/no): ").lower()

es_critic = servei_critic == "sí" or servei_critic == "si"
hi_ha_alternativa = alternativa == "sí" or alternativa == "si"

if usuaris < 0:
    print("Nombre d'usuaris incorrecte")
elif es_critic and not hi_ha_alternativa:
    print("Prioritat crítica")
elif (
    (usuaris >= 50 and not hi_ha_alternativa) or usuaris >= 10 or es_critic
):
    print("Prioritat alta")
else:
    print("Prioritat baixa")