from ml.math.forward import forward
from ml.math.loss import lossFunc


def main():
    inputs = [2, 3]

    weights = [
        [[0.5, 0.8], [0.2, 0.4]], 
        [[0.3, 0.7]]               
    ]

    biases = [
        [1, 0.5],
        [0.5]
    ]
    expected = [5.0]

    output = forward(inputs, weights, biases)
    print(output)
    
    
    loss = lossFunc(expected, output)
    print(loss)
if __name__ == "__main__":
    main()