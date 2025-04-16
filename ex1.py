# 1. Dado um array de números, coloque o array em ordem crescente.

import random

## Função que gera um array de 1 dimensão
def generate_array(n,min_val=0,max_val=1):
  random_array = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(random_array)
  return random_array

## Chama da função
numeros = generate_array(10,0,11500)

def colocarArrayCrescente():
    print(numeros)

    tamanho = 0
    for n in numeros:
        tamanho += 1

    index = 0
    while index < tamanho:
        indexMenor = 0
        while indexMenor < tamanho - index - 1:
            if numeros[indexMenor] > numeros[indexMenor + 1]:
                numeros[indexMenor], numeros[indexMenor + 1] = numeros[indexMenor + 1], numeros[indexMenor]

            indexMenor += 1
        index += 1

    print('\nArray dado acima mas em ordem crescente:')
    print(numeros)

colocarArrayCrescente()