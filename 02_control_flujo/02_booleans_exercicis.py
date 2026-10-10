###
# EXERCICIS
###

# Exercici 1: Comparar nombres
# Donats els nombres:
nombre_a = 8
nombre_b = 5
# Mostra el resultat de comparar si nombre_a és més gran, més petit o igual
# que nombre_b.
print (nombre_a > nombre_b)
print (nombre_a < nombre_b)
print (nombre_a == nombre_b)

# Exercici 2: Comparar cadenes de text
#Donades les cadenes:
paraula_a = "Hola"
paraula_b = "hola"
# Mostra si són iguals i si paraula_a és igual a "Hola".
# Observa si Python distingeix entre majúscules i minúscules.
print(paraula_a == paraula_b)
#Si distingeix les majuscules amb les minuscules, el resultat ha sortit False


# Exercici 3: Connexió de xarxa
# Donats els valors booleans:
router_encès = True
connexio_activa = False
# Crea una variable anomenada xarxa_disponible que sigui True només si el
# router està encès i la connexió està activa. Mostra'n el resultat.

if router_encès == True and connexio_activa== True:
    xarxa_disponible = True
else:
    xarxa_disponible= False

print(xarxa_disponible)
    
# Exercici 4: Avisos pendents
# Donats els valors booleans:
actualitzacio_disponible = False
alerta_critica = True
# Crea una variable anomenada cal_avisar que sigui True si hi ha una
# actualització disponible o una alerta crítica. Mostra'n el resultat.

if actualitzacio_disponible == True or alerta_critica == True:
    cal_avisar = True
else:
    cal_avisar = False

print(cal_avisar)



# Exercici 5: Accés a un compte
# Donats els valors booleans:
compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
# Crea una variable anomenada accés_permes que sigui True si el compte està
# actiu, la contrasenya és correcta, el compte no està bloquejat i, a més,
# el codi és correcte o el dispositiu és de confiança. Fes servir and, or i not.
# Mostra'n el resultat.

if compte_actiu == True and contrasenya_correcta == True and compte_bloquejat == False:
    if codi_correcte == True or dispositiu_de_confianca == True:
        acces_permes = True
    else:
        acces_permes = False
else:
    acces_permes = False

print(acces_permes)