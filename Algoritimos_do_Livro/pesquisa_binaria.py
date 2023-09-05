lista = range(500)

def search(lista, item):
    menor = 0
    maior = len(lista)

    while (menor<=maior):
        meio = (menor+maior)//2
        if item == lista[meio]:
            return lista[meio]
        if  item < lista[meio]:
            maior = meio
        if item > lista[meio]:
            menor = meio
    return None

busca = int(input())
print(search(lista, busca))