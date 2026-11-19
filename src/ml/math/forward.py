from .dotProduct import dotProduct
from .activations import relu

def forward (inputs, weights, biases):
    for i in range(len(weights)):
        inputs = forwardLayer(inputs, weights[i], biases[i])

    return inputs

def forwardLayer (inputs, weights, bias):
    layer = []
    for i in range(len(weights)):
        layer.append(relu((dotProduct(inputs, weights[i]) + bias[i])))
    return layer