def pesquisa(lista, item, menor, maior):
    if menor<=maior:
        meio = (maior+menor)//2
        if lista[meio] == item:
            return meio
        if lista[meio] < item:
            return pesquisa(lista, item, meio, maior)
        else:
            return pesquisa(lista, item, menor, meio)
    return None
    
lista = range(500)
item = int(input(": "))
print(pesquisa(lista, item, 0, len(lista)))