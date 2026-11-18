def matrixTrasnspose(a):
    matrixT = []
    for i in range(len(a[0])):
        matrixj = []
        for j in range(len(a)):
            matrixj.append(a[j][i])
        matrixT.append(matrixj)
    return matrixT
