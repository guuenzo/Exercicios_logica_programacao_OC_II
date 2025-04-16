# 6. Dado um array de números e um valor, retorne dois números do vetor cuja soma
# seja igual ao número, ou 0 caso não exista.

vetor = [3, 2, 1]
numero = [6]

def retornarSomaNumero():
    n1 = numero[0]
    contador = 0

    for v in vetor:
        contador += 1

    index = 0
    while index < contador:
        j = index + 1
        while j < contador:
            if vetor[index] + vetor[j] == n1:
                resultado = []
                resultado.append(vetor[index])
                resultado.append(vetor[j])
                return resultado

            j += 1
        index += 1
    return 0
        
print(retornarSomaNumero())