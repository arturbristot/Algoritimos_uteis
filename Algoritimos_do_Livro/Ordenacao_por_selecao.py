def buscaMenor(lista):
    menor = lista[0]
    menor_indice = 0

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(lista):
    nvlista = []
    for i in range(len(lista)):
        menor = buscaMenor(lista)
        nvlista.append(lista.pop(menor)) #funcao pop retira da lista o menor valor (para o proximo loop)
    return nvlista

lista = [5, 3, 6, 2, 10]
a = (ordenacao_por_selecao(lista))
print(a)
print(a[0])