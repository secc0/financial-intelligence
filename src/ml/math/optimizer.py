def updateWeights(weights, gradients, learningRate):
    newW = []
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            for k in weights[i][j]:
                newW.append(k - (gradients[j] * learningRate))
    return newW