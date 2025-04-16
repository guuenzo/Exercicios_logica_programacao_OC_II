# 4. Dado dois arrays de mesmo tamanho, retorne um novo vetor intercalando os
# elementos

vetorA = [1, 3, 5]
vetorB = [2, 4, 6]

def intercalacaoArrays():
    tamanho = 0
    for a in vetorA:
        tamanho += 1

    resultado = []
    i = 0
    while i < tamanho: 
        resultado += [vetorA[i]]
        resultado += [vetorB[i]]

        i += 1

    return resultado

print(intercalacaoArrays())