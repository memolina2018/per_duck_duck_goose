def pato(numero,lista_jugadores):
    numero=int(numero)
    for index,value in enumerate(lista_jugadores):
        index=index+1
        if index==numero:
            return("El jugador que es oca se llama: ", value)

lista=input("introduce una lista de jugadores: ")
lista= lista.split(",")
print(lista)
num=input("introduce un número: ")
print(pato(num,lista))
print("jajajajajjajqajajajajjajajajajajajajaja")

