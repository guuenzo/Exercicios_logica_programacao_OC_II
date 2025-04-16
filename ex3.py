# 3. Dado um array de caracteres, verifique se ele forma um palíndromo (lê-se da mesma
# forma de frente para trás e de trás para frente.

array = ['r', 'a', 'd', 'a', 'r']

def verificarArrayPalindromo():
    print(array)

    tamanho = 0
    for a in array:
        tamanho += 1

    indexFinal = tamanho - 1
    indexComeco = 0

    while indexComeco < tamanho:
        if array[indexComeco] != array[indexFinal]:
            return 'Não é um palíndromo.'
        
        indexComeco += 1
        indexFinal -= 1

    return 'É um palíndromo.'

print(verificarArrayPalindromo())