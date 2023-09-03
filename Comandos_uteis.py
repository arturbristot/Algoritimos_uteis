#----------------------------------------------------------#

# exemplo basico de recursividade :
def regressiva(n):
    if n < 1:
        return
    else:
        print(n)
        n = n-1
        regressiva(n)

#regressiva(5)
#imprimiria = 5, 4, 3, 2, 1

#----------------------------------------------------------#
#fatorial com recursividade :

def fat(x):
    if x == 1 :
        return x
    else:
        return x * fat(x-1)

# print(fat(5))

#----------------------------------------------------------#

def ordenar(lista):
    lista.sort()
    return lista

def ordenar_reverso(lista):
    lista.sort(reverse=True)
    return lista

#recebe uma lista e retorna a lista ordenada

#----------------------------------------------------------#

def eleminar_repetidos(lista):
    lista = (set(lista))
    return lista
#da de usar para contar quantas vezes um elemento aparece na lista

#----------------------------------------------------------#
#lista = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]
#print(lista.count(3))
#outra forma de verificar quantas vezes o numero 3 repete

#----------------------------------------------------------#