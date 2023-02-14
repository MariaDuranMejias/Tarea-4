#Se define una funcion que genere tupla y lista de una secuencia de numeros que sea ingresada por el usuario
#Se le pide al usuario que ingrese una secuencia de numeros que sea separada por comas
#Esta funcion debe fallar cuando se detecte que los numeros esten separados por comas
#Para definir la condicion de error, primero se convirtio el input que ingreso el usuario en una tupla
#Se cuenta cuantas veces aparece la coma dentro de esta tupla
#Se convierte el input que ingreso el usuario en una lista para saber la longitud del input ingresado por el usuario
#Se hace un condicional con if, si la cantidad de comas es igual a la longitud del input menos un digito, divido entre 2
#Si el resultado es igual y diferente de cero, entonces se entra en un ciclo for donde se recorre la palabra digito por digito
#Entonces si el digito es diferente de cero se agrega a una lista
#Se genera una tupla a partir de la lista
def GeneradorDeTuplasYListas():
    secuencia = input("Ingrese la secuencia de numeros separada por comas (') con la que desea generar una lista y una tupla: \n")
    Lista = []
    Tupla_con_comas = tuple(secuencia)
    n = Tupla_con_comas.count(',')
    Lista_con_comas = list(secuencia)
    y = len(Lista_con_comas)
    tupla = ()
    i=0
    x = len(secuencia)
    a = secuencia[i]

    if n == ((y-1)/2) and (y-1) != 0:
        for i in range (0, x):
            if secuencia[i] != ',':
                Lista.append(secuencia[i])
                Tupla = tuple(Lista)
    print("Resultado:")
    print("Lista: ", Lista)
    print("Tupla:", Tupla) 

    if n != (y-1)/2 or y-1==0:
        print("La secuencia no contiene numeros separados por comas")

        
    return

GeneradorDeTuplasYListas()