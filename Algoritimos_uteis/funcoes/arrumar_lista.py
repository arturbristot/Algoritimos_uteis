import random

def checarLista(x):
    lista = 10 * [0]
    for i in x:
        lista[i] += 1
    maior = max(lista)
    if maior > (len(x)+1) // 2:
        return False
    else:
        return True
    
def arr_lista(bolas):
    if checarLista(bolas):
        for i in range(len(bolas)):
            if bolas[i] == bolas[i-1]:
                random.shuffle(bolas)
        return bolas
    else:
        return "impossivel!"
    
bolas = list(map(int, input().split()))

print(arr_lista(bolas))