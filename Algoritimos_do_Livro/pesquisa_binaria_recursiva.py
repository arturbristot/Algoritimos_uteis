def binare_search(lista, item, menor, maior):
    if menor<=maior:
        meio = (maior+menor)//2
        if lista[meio] == item:
            return meio
        if lista[meio] > item:
            return binare_search(lista, item, menor, meio)
        else:
            return binare_search(lista, item, meio, maior)
    return None

lista = range(500)
item = int(input(": "))
print(binare_search(lista, item, 0, len(lista)))