def inverter_lista(lista):
    menor = 0
    maior = len(lista)-1
    while (menor < maior):
        temp = lista[menor]
        lista[menor] = lista[maior]
        lista[maior] = temp

        menor +=1
        maior -=1
    return lista