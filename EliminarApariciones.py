#Definimos la funcion con los 2 argumentos, la lista y el elemento de la lista que se quiere eliminar
#Generamos una lista vacia
#Primero comprobamos que el elemento que se esta poniendo se encuentre dentro de la lista, sino lo esta, se envia un mensaje de error
#Si el elemento se encuentra en la lista dada en el argumento:
###Se genera un ciclo for que tome cada elemento de la lista y lo compare con el elemento que se dio en el argumento
###Si es diferente se agrega el elemento a la lista vacia, de esta forma solo se agregan los valores que sean diferentes al argumento dado en la funcion
###Se imprime la lista con los valores de la lista del argumento excepto el elemento definido en el argumento de la funcion
def EliminarApariciones(lista, elemento):
    lista_vacia = []
    if elemento not in lista:
        print("El elmento no se encuentra en la lista")
    elif elemento in lista:
        for item in lista:
            if item != elemento:
                lista_vacia.append(item)
        print(lista_vacia)

    return

lista = [20, 30, 40, 20, 5, 100, 5, 20] 
EliminarApariciones(lista, 20)
# EliminarApariciones(lista, 55)
 
#lista = ['perro', 'gato', 'sombrero', 'gato', 'zanahoria']
# EliminarApariciones(lista, 'gato')

#lista = []
#lista = [1,1,1,1,1,1,1,1,1]
#EliminarApariciones(lista, 1)
# lista = [2,3,4,55,66,'f','g','h','h']
# EliminarApariciones(lista, 'h')



          