from ml.math.forward import forward
from ml.math.loss import lossFunc
from ml.math.gradient import gradient

def main():
    inputs = [2, 3]
    weights = [[[0.5, 0.8], [0.2, 0.4]],[[0.3, 0.7]]]
    biases = [[1, 0.5],[0.5]]
    expected = [5.0]

    prediction = forward(inputs, weights, biases)
    print("predicition",prediction)
    loss = lossFunc(expected, prediction)
    grad = gradient(inputs, weights, biases, expected, prediction)
if __name__ == "__main__":
    main()