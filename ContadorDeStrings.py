#Definimos una funcion que reciba de argumento un string

def ContadorDeStrings(string):

#Generamos listas para luego guardar los numeros, letras y caracteres especiales
    lista = list(string)
    numeros = []
    letras = []
    caracteres_especiales = []
#Se recorre la string en busca de caracteres alfabeticos con la funcion isalpha()
#Si el caracter es alfabetico se agrega a la lista Letras
#Para crear el caso en que no hayan letras en esta string, se guarda en una variable la longitud de la lista Letras
#Si la longitud es igual a cero, es porque no hay letras presentes en la string, por lo que devolvera un valor de cero.
#En caso contrario, si hay letras presentes en la string, devolvera la longitud de la lista Letras, es decir, la 
# cantidad de letras que hay en la string
    for elemento in string:
        if elemento.isalpha():
            letra = elemento
            letras.append(letra)
    cantidad_letras = len(letras)
    if cantidad_letras == 0:
        print("Letras = 0")
    else:
        print("Letras = " + str(cantidad_letras))

#Se recorre la string en busca de caracteres numericos con la funcion isnumeric()
#Si el caracter es numerico se agrega a la lista Numeros
#Para crear el caso en que no hayan numeros en esta string, se guarda en una variable la longitud de la lista Numeros
#Si la longitud es igual a cero, es porque no hay numeros presentes en la string, por lo que devolvera un valor de cero.
#En caso contrario, si hay numeros presentes en la string, devolvera la longitud de la lista Numeros, es decir, la 
# cantidad de numeros que hay en la string
    for elemento in string:
        if elemento.isnumeric():
            numero = elemento
            numeros.append(numero)
    cantidad_numeros = len(numeros)
    if cantidad_numeros == 0:
        print("Numeros = 0")

    else:
        print("Numeros = " + str(cantidad_numeros))

#Para averiguar la cantidad de caracteres especiales, generamos una lista que contenga los valores de las listas anteriores
#Es decir, se agrega en una sola lista las listas Letras y Numeros
#Se recorre los elementos de la string y si no esta en la lista con las letras y numeros, se agrega a la lista caracteres_especiales
#Para saber si la string no contiene caracteres especiales, se hace lo mismo, si la longitud de esta lista es igual a cero, 
#es porque no hay caracteres especiales presentes en la string, por lo que devolvera un valor de cero.
#En caso contrario, si hay caracteres especiales presentes en la string, devolvera la longitud de la lista caracteres_especiales, es decir, la 
# cantidad de caracteres especiales que hay en la string
    numeros_letras = letras + numeros    
    for elemento in string:
        if elemento not in numeros_letras:
            caracteres_especiales.append(elemento)
    cantidad_caracteres_especiales = len(caracteres_especiales)
    if cantidad_caracteres_especiales == 0:
        print("Caracteres especiales = 0")
    else:
        print("Caracteres especiales = " + str(cantidad_caracteres_especiales))

    return  

ContadorDeStrings("P@#yn26at^&i5ve") #Caso en el que tiene letras, numeros y caracteres especiales
ContadorDeStrings("@#26^&5") #Caso sin letras
ContadorDeStrings("P@#ynat^&ive") #Caso sin numeros
ContadorDeStrings("Pyn26ati5ve") #Caso sin caracteres especiales
ContadorDeStrings("") #String vacia


