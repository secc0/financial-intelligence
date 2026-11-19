def elementWiseMultiply(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("as matrizes precisam ter o mesmo tamanho de vetor e quantidade de valores nos vetores")
    product = []
    for i in range(len(a)):
        vector = []
        for j in range(len(a[0])):
            vector.append(a[i][j] * b[i][j]) 
        product.append(vector)
    return product

def elementWiseAdd(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("as matrizes precisam ter o mesmo tamanho de vetor e quantidade de valores nos vetores")
    product = []
    for i in range(len(a)):
        vector = []
        for j in range(len(a[0])):
            vector.append(a[i][j] + b[i][j]) 
        product.append(vector)
    return product