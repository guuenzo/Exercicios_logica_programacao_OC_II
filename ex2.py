# 2. Dado um array de caracteres, inverta os caracteres.

array = ['d', 'i', 'a']

def inverterCaracteres():
    print(array)

    tamanho = 0
    for a in array:
        tamanho += 1

    indexComeco = 0
    indexFinal = tamanho - 1

    while indexComeco < indexFinal:
        e = array[indexComeco]
        array[indexComeco] = array[indexFinal]
        array[indexFinal] = e

        indexComeco += 1
        indexFinal -= 1
    
    print(array)

inverterCaracteres()