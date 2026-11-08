def matrixTrasnspose(a):
    matrixT = []
    for i in range(len(a[0])):
        matrixj = []
        for j in range(len(a)):
            matrixj.append(a[j][i])
        matrixT.append(matrixj)
    return matrixT

a = [
    [2, 3, 4],
    [5, 6, 7],
    [2, 3, 4],
]


print(matrixTrasnspose(a))