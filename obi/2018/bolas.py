def checarLista(x):
    lista = 10 * [0]
    for i in x:
        lista[i] += 1
    maior = max(lista)
    if maior > (len(x)+1) // 2:
        return False
    else:
        return True

bolas = list(map(int, input().split()))
if checarLista(bolas):
    print("S")
else:
    print("N")