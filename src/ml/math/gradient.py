from .forward import forward
from .loss import lossFunc
def gradient(inputs, weights, biases, expected, originalLoss):
    forwards = []
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            for k in range(len(weights[i][j])):
                weights[i][j][k] += 0.01
                result = forward(inputs, weights, biases)
                loss = lossFunc(expected, result)
                grad = (loss - originalLoss) / 0.01
                weights[i][j][k] -= 0.01
                forwards.append(grad)
    return forwards