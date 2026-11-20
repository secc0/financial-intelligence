from .forward import forward
def gradient(inputs, weights, biases, expected, prediction):
    forwards = []
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            for k in range(len(weights[i][j])):
                weights[i][j][k] += 0.01
                result = forward(inputs, weights, biases)
                weights[i][j][k] -= 0.01
                forwards.append(result)
    print(forwards)
    return forwards