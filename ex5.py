# 5. Dado dois arrays, retorne a intercalação entre eles (os elementos em comum entre
# os dois arrays, em qualquer ordem):

vetorA = [1,2,2,1]
vetorB = [2,2]

def retornarIntercalacaoArrays():
    resultado = []
    contadorA = 0
    contadorB = 0

    for v in vetorA:
        contadorA += 1

    for v in vetorB:
        contadorB += 1

    index = 0
    while index < contadorA:
        j = 0
        while j < contadorB:
            if vetorA[index] == vetorB[j]:
                resultado.append(vetorA[index])
                vetorB[j] = -9999
            j += 1
        index += 1

    return resultado

print(retornarIntercalacaoArrays())