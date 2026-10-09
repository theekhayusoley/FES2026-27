###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

tecnic = input("Nom del tecnic: ")
xarxa = input("Quina xarxa estas instalant companyerete? ")
print(f"El colegon es diu {tecnic} i t'esta instalant la xarxa {xarxa} a casa teva")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = int(input("Quants km de fibra? "))
velocitat = int(input("Quina velocitat en Gbps? "))
segons = 8 / velocitat
print(f"Per transmetre 1 GB de dades calen {segons} segons.")


# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores = int(input("Cuantes hores has fet? "))
preu = float(input("A cuanto estas cobrando especulador? "))
material = float(input("Preu del material:"))
total = hores*preu+material
if total>100:
    print(f"T'ha sortit cara la broma, preu es: {total:.2f}")
else:
    print(f"No t'ha afectat la inflació encara, el preu total sera de {total:.2f} euros")