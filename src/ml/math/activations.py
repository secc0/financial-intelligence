import math

def relu(x):
    if x <= 0:
        return 0
    return x

def sigmoid(x):
    return 1 / (1 + math.exp(- x))

def tanh(x):
    return ((math.exp(x) - math.exp(- x)) / (math.exp(x) + math.exp(- x)))
