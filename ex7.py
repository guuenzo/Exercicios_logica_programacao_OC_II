# 7. Dado um array ordenado, encontre a mediana dos elementos.

vetor = [1,2,3,4,5,6]

def encontrarMedianaElementos():
    contadorElementos = 0
    somaElementos = 0

    for v in vetor:
        contadorElementos += 1
        somaElementos += v

    resultado = somaElementos / contadorElementos
    
    return resultado

print(encontrarMedianaElementos())