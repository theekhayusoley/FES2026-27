###
# EXERCICIS (excepcions)
# Tots els textos d'entrada es proporcionen per evitar entrada interactiva.
###

# Exercici 1 - Bàsic. Conversió segura de tensions
# Per a cada text de tensions, intenta convertir-lo amb float.
# Captura ValueError i mostra 'Tensió incorrecta' en aquest cas.
# Utilitza else per mostrar la conversió quan sigui correcta.
# Sortida esperada, una línia per entrada: 3.3 / Tensió incorrecta / 0.0.
# Cas límit: '0' és una mesura vàlida.
tensions = ["3.3", "avaria", "0"]
# TODO: escriu el bucle i el tractament de ValueError.

for valor in tensions:
    try:
        tensio=float(valor)
    except ValueError:
        print("Conversió incorrecte")
    else:
        print(f"Conversio correcte: {tensio}")



# Exercici 2 - Bàsic. Humitat amb contracte
# Defineix validar_humitat(text) que retorni un float finit dins [0, 100].
# Genera ValueError per a text no numèric, valors no finits o fora de rang.
# Utilitza math.isfinite després de convertir el text.
# Entrades: '0', '100', '45.5', '-1', '101', 'nan', 'inf', 'error'.
# Retorns esperats per a les tres primeres: 0.0, 100.0 i 45.5.
# La resta han de produir ValueError, gestionat en les demostracions.
entrades_humitat = ["0", "100", "45.5", "-1", "101", "nan", "inf", "error"]
# TODO: defineix la funció i mostra resultats o un missatge de rebuig.

import math
def validar_humitat(text):

    # Convertimos el texto a float
    humitat = float(text)

    # Comprobamos que sea un número finito
    if not math.isfinite(humitat):
        raise ValueError("La humitat ha de ser finita") #el mensaje no sale por pantalla, solo es la identificar el problema

    # Comprobamos que esté entre 0 y 100
    if humitat < 0 or humitat > 100:
        raise ValueError("La humitat ha d'estar entre 0 i 100") #con raise podemos provocar nosotros mismos una excepción cuando un dato no cumple una condición

    # Si todo está bien, devolvemos la humedad
    return humitat

"Bucle per recorrer la llista"
for entrada in entrades_humitat:
    try:
        humitat = validar_humitat(entrada)
    except ValueError:
        print("Error")
    else:
        print(humitat)
            


# Exercici 3 - Intermedi. Fitxer absent i finalització
# Dins de TemporaryDirectory crea només una ruta a 'absent.txt' amb Path.
# Intenta obrir-la en mode lectura, amb encoding='utf-8'.
# Captura FileNotFoundError i mostra 'Fitxer absent'.
# Utilitza finally per mostrar 'Intent acabat' tant si hi ha error com si no.
# Sortida esperada: Fitxer absent / Intent acabat.
# Segona prova: crea un fitxer temporal que contingui 'T1=21.5' i repeteix.
# Sortida esperada: T1=21.5 / Intent acabat.
# Mantén tots els fitxers dins de la carpeta temporal.
# TODO: importa Path i TemporaryDirectory i prova els dos camins.

from pathlib import Path #Sirve para trabajar con rutas de archivos y carpetas.
from tempfile import TemporaryDirectory #Sirve para crear una carpeta temporal que Python eliminará automáticamente cuando terminemos de utilizarla.


# Función que intenta abrir y leer un archivo
def mostrar_fitxer(ruta): #creamos una funcion que le llega un parametro, Ese parámetro será la ubicación del archivo que queremos abrir.
                          #por ejemplo, podemos recibir: carpeta_temporal/absent.txt
    try:
        # Intentamos abrir el archivo para leerlo
        with open(ruta, encoding="utf-8") as fitxer: #Sirve para abrir un archivo.
                                                     #Como no hemos indicado ningún modo, Python utiliza el modo de lectura ("r").
                                                     #with: sirve para gestionar el archivo abierto y cerrarlo automaticamente cuando terminemos de trabajar con el
                                                     #as fitxer: guarda el fitxero abierto en una variable llamada fitxer 
            contingut = fitxer.read() #.read(): lee todo el contenido del archivo y lo guarda en la variable contingut
                                      #ej. si dentro del archivo tenemos: T1=21.5, la varirable contingut tendra "T1=21.5"          

    except FileNotFoundError: #Si al intentar abrir el archivo no lo encuentras, captura el error.
                              #la funcion FileNotFoundError es una excepcion especifica para los archivos que no existen
        # Si el archivo no existe, mostramos este mensaje
        print("Fitxer absent")

    else: #se ejecuta cuando el try lo hace correctamente
        # Si todo funciona, mostramos el contenido
        print(contingut)

    finally: 
        # Se ejecuta siempre, haya error o no
        print("Intent acabat")


def main(): #Entramos al programa principal

    # Creamos una carpeta temporal 
    with TemporaryDirectory() as carpeta: #cuando salgamos del with, se eliminara la carpeta

        # Creamos la ruta del archivo (todavía no existe)
        ruta = Path(carpeta) / "absent.txt" #Esto construye la ruta del archivo.  Fíjate en la barra /: aquí no significa división matemática.
                                            #Sirve para unir la ruta de la carpeta con el nombre del archivo.
                                            #aun no existe el archivo
        # PRIMERA PRUEBA: intentamos leer un archivo inexistente
        mostrar_fitxer(ruta) #como aun no exste el archivo, cuando llamemos a la funcion saldra qu: Fitxer absent e intent acabat

        # SEGUNDA PRUEBA: creamos el archivo y escribimos dentro
        with open(ruta, "w", encoding="utf-8") as fitxer:
            fitxer.write("T1=21.5")

        # Ahora intentamos leer el archivo que acabamos de crear
        mostrar_fitxer(ruta)


# Ejecutamos el programa directamente
if __name__ == "__main__":
    main()



# Exercici 4 - Repte opcional. Filtrar lectures de temperatura
# Defineix filtrar_temperatures(textos) que retorni (valides, rebutjades).
# valides és la llista de floats finits dins del rang simulat [-40, 85] °C.
# rebutjades és el nombre d'entrades que no es poden acceptar.
# Crea una funció validar_temperatura(text) i reutilitza-la al bucle.
# Entrada següent. Retorn esperat: ([-40.0, 21.5, 85.0], 3).
# Amb [] ha de retornar ([], 0). Amb ['nan', 'inf'] ha de retornar ([], 2).
textos = ["-40", "21.5", "85", "86", "avaria", "nan"]
# TODO: captura ValueError per cada lectura i continua amb les següents.
