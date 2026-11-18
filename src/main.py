from ml.math.dotProduct import dotProduct
from ml.math.activations import relu
def main():
    inputs = [2, 3]
    weights = [[0.5, 0.8],[0.2, 0.4] ]
    bias = [1, 0.5]

    layer1Output = []

    for i in range(len(weights)):
        layer1Output.append(relu((dotProduct(inputs, weights[i]) + bias[i])))
    print(layer1Output)
if __name__ == "__main__":
    main()