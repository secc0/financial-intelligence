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