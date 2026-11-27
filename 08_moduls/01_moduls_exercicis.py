###
# EXERCICIS (mòduls)
# Resol cada exercici en aquest fitxer amb els mòduls auxiliars facilitats.
# Executa des de l'arrel: python 08_moduls/01_moduls_exercicis.py
###

# Exercici 1 - Bàsic. Magnitud d'una mesura
# Importa math amb l'àlies matematiques. Calcula el mòdul d'un vector de
# components x i y amb sqrt(x * x + y * y).
# Entrada: x = 3.0, y = 4.0. Sortida esperada: 5.0.
# Cas límit: x = 0.0, y = 0.0 ha de donar 0.0.
x = 3.0
y = 4.0
# TODO: escriu les importacions i els càlculs.
import math as matematiques

x=5.0
y=2.6
modul=matematiques.sqrt(x*x+y*y)
print(f"El modul es: {modul}")

# Exercici 2 - Bàsic. Conversions reutilitzables
# Importa conversions amb l'àlies conv i utilitza les seves funcions.
# Converteix cada temperatura a kelvins i cada tensió a volts.
# Entrades següents. Sortides esperades en el mateix ordre:
# [263.15, 273.15, 298.15] i [0.0, 3.3, 5.0].
# Amb una llista buida, el resultat corresponent ha de ser [].
temperatures = [-10.0, 0.0, 25.0]
tensions_mv = [0, 3300, 5000]
# TODO: obtén i mostra dues llistes amb les conversions.

import conversions as conv
kelvins=[]
volts=[]
for i in range(len(temperatures)): #range nomes llegeix valors enters
    kelvins.append(conv.celsius_a_kelvin(temperatures[i])) #anem afegint amb append (ultim element de la llista)
for i in range(len(tensions_mv)):
    volts.append(conv.milivolts_a_volts(tensions_mv[i]))
print(f"Llista de kelvins: {kelvins}")
print(f"Tensions en V: {volts}")

# Exercici 3 - Intermedi. Resum d'una xarxa de sensors
# Importa únicament mitjana del mòdul sensors.
# Crea un diccionari de mitjanes amb els mateixos identificadors que dades.
# Sortida esperada: {'T1': 21.0, 'T2': 18.0, 'T3': None}.
# El mòdul sensors ja defineix el tractament de la llista buida.
dades = {"T1": [20.0, 22.0], "T2": [18.0], "T3": []}
# TODO: reutilitza la funció importada per a cada sensor.

from sensors import mitjana
diccionari_mitjanes={}
for identificador in dades:
    diccionari_mitjanes[identificador]=mitjana(dades[identificador]) #Busca en el diccionario original el valor correspondiente a esa clave.
                                                                     #en la primera vuelta devielve: [20.0,22.0] y hace la mitjana
                                                                     #luego lo guarda: diccionari_mitjanes["T1"] = 21.0



# Exercici 4 - Repte opcional. Un programa reutilitzable
# Defineix informe_sensor(nom, lectures) que retorni un diccionari amb
# les claus 'nom', 'nombre' i 'mitjana'. Reutilitza sensors.mitjana.
# Entrada: informe_sensor('T1', [20.0, 22.0]).
# Retorn esperat: {'nom': 'T1', 'nombre': 2, 'mitjana': 21.0}.
# Cas límit: informe_sensor('T0', []) ha de retornar
# {'nom': 'T0', 'nombre': 0, 'mitjana': None}.
# Afegeix una funció main() que mostri aquests dos informes.
# Protegeix TOTES les demostracions del fitxer amb __name__ == '__main__'.
# En importar el fitxer no s'ha de mostrar cap sortida.
# TODO: reorganitza les demostracions dels exercicis 1–3 dins de main().

from sensors import mitjana

def informe_sensor(nom,lectures):
    diccionari_conjunt={
        "nom":nom,
        "nombre": len(lectures),
        "mitjana":mitjana(lectures)
    }
    return diccionari_conjunt

def main(): #creamos una funcion que se llama main que contendra todas las pruebas de cada ejercicio (programa principal)
            #fuera de este estaran las funciones declaradas que iremos llamando en nuestro programa principal
    #exercici 1
    print(f"El modul es: {modul}")

    #exercici 2
    print(f"Llista de kelvins: {kelvins}")
    print(f"Tensions en V: {volts}")

    #exercici 3
    #exercici 4
    print(informe_sensor("T1", [20.0, 22.0])) #li pasem a la funcio en format: nom, llista de lectures
    print(informe_sensor("T0", []))
    # 4. Ejecutamos el programa
if __name__ == "__main__": #Si estoy ejecutando este archivo directamente, ejecuta la función principal. 
    main()                 #Si otro archivo lo importa, no ejecutes las demostraciones automáticamente.