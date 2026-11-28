def updateWeights(weights, gradients, learningRate):
    newW = []
    c = 0
    for i in range(len(weights)):
        wi = []
        newW.append(wi)
        for j in range(len(weights[i])):
            wj = []
            wi.append(wj)
            for k in weights[i][j]:
                wj.append(k - (gradients[c] * learningRate))
                c +=1
    return newW