###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
    """Funcio per saludar, variable nom com a primer argument i la forma de saludar com a segon argument"""
    print(f"{salutacio} {nom}")
saludar_a("Theekhayu")#Com que ja hi ha una variable per defecte doncs nomes li pasem el que aniria a la variable nom

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(numero):
    if numero%2==0:
        return True
    else:
        return False
valor=int(input("Introdueix numero: "))
print(f"El {valor} es parell? {es_parell(valor)}")

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(numeros):
    suma=0
    for numero in numeros:
        suma+=numero
    mitjana=suma/len(numeros)
    return mitjana

diferents_numeros = [4.8, 5.0, 5.1, 4.9, 5.2]
print(f"La mitjana es: {mitjana(diferents_numeros)}")

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):## ♾️ Arguments de longitud variable (`*args`)
    suma=0
    for numero in args:
        suma+=numero
    return suma
print(f"La suma total de 1,5 es: {sumar_tot(1,5)}")
print(f"La suma total de 1,5,8,9,7 es: {sumar_tot(1,5,8,9,7)}")
print(f"La suma total de 1,5,78,5,9,4,8,77,8,8 es: {sumar_tot(1,5,78,5,9,4,8,77,8,8)}")

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for numeros in range(1,limit+1):#asi comença en 1 i acaba en 10
        print(f"{numero} x {numeros}={numeros*numero}")
valor=int(input("Introdueix el valor per sapiguer la taula: "))
taula_multiplicar(valor)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs): #con **kwargs: "No sé cuántos datos me vas a pasar. Recibe todos los datos que vengan con un nombre."
                              #kwargs es un diccionario que Python crea automáticamente con los argumentos que le pasas.
    for clau, valor in kwargs.items(): #items() obtiene todas las parejas clave: valor del diccionario para poder recorrerlas.
                              #el for: "Dame cada pareja de nombre y valor."
        print(f"{clau}: {valor}")
mostrar_perfil(nom="Theekhayu", edat=22, grau="Telecos")


# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def es_factorial(valor):
    factorial = 1
    comptador = 1
    while comptador <= valor:
        factorial *= comptador
        comptador += 1
    return factorial

def es_maxim(llista):
    maxim=0
    for valor in llista:
        if valor>maxim:
            maxim=valor
    return maxim
print(f"El factorial de 5 es: {es_factorial(5)}")
llista1=[1,5,8,4,9,8,7]
print(f"El maxim de la llista1 es {es_maxim(llista1)}")


# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    contador = 0
    for lletra in text.lower():#pasem tot a minuscula, el for recorre totes les lletres de la cadena de strings que li pasem
        if lletra in "aeiou": #"Si lletra és una de les vocals a, e, i, o o u...", La paraula in comprova si un element està dins d'un text, una llista, etc.
            contador += 1
    return contador
textito = input("Introdueix un text: ")
print(f"El text té {comptar_vocals(textito)} vocals.")
    
# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    minim=numeros[0]#aqui el que fem es comparar desde el primer valor de la llista
    maxim=numeros[0]#si fesim minim=0 potser un valor de llista seria negatiu i no compararia bé els minims
    for numero in numeros:
        if numero>maxim:
            maxim=numero
        if numero<minim:
            minim=numero
    return minim,maxim

llista=[7,8,9,5,7,8,9,1,6]
minimo, maximo = minim_i_maxim(llista)#com que retorna dos valors, el guardem a dos variables directament
print(f"El maxim es: {maximo}")
print(f"El minim es: {minimo}")


# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.

def es_palindrom(text):
    text = text.lower()
    if text == text[::-1]: #Con [::-1] Python ya puede invertir toda la cadena directamente.
        return True
    else:
        return False
            
        
