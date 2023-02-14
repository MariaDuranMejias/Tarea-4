#Se define la funcion que va a contar todas las apariciones de cada caracter en la string, con el parametro de string.
#Guardamos la string en una lista
#Utilizamos lambda, que obtiene la cantidad de veces que se repite un valor
#Luego se aplica un contador para saber cuantas veces esta este valor en la lista 
#Se utilizan las funciones map() y zip() para combinar los valores y dict() para pasarlos a un diccionario
#Se generan casos de prueba con letras, numeros, vacia y caracteres especiales para verificar que siempre cuenta las apariciones de cada caracter.
def ContadorApariciones(string):
    Lista = []
    i=0
    x = len(string)
    for i in range (0, x):
        Lista.append(string[i])
    resultado = dict(zip(Lista,map(lambda x: Lista.count(x),Lista)))
    print(resultado)
    return

ContadorApariciones("papaya")
ContadorApariciones("678943")
ContadorApariciones("-9-9-9-9-4-4/5/5")
ContadorApariciones("")
ContadorApariciones("@#$##%^&^^")