def matrixMultiplication(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Os valores precisam ter o mesmo tamanho")
    resultMatrix = []
    for i in range(len(a)):
        resultMatrixj = []  
        for j in range(len(b[0])):
            resultj = 0
              
            for k in range(len(b)):
                resultj += a[i][k] * b[k][j]

            resultMatrixj.append(resultj)

        resultMatrix.append(resultMatrixj)
    return resultMatrix        



    
a = [
    [2, 3, 4],
    [5, 6, 7],
    [2, 3, 4],
    [5, 6, 7],
    [2, 3, 4],
    [5, 6, 7],
    [2, 3, 4],
    [5, 6, 7],
    [2, 3, 4],
    [5, 6, 7],
    [2, 3, 4],
    [5, 6, 7]
]

b = [
    [1, 2,3,5,6,7,4,5,7,8,5,3],
    [1, 2,3,5,6,7,4,5,7,8,5,3],
    [1, 2,3,5,6,7,4,5,7,8,5,3]
]

print(matrixMultiplication(a, b))