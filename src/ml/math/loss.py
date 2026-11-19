def lossFunc (expected, prediction):
    result = 0
    if len(expected) != len(prediction):
        raise ValueError("Os valores precisam ter o mesmo tamanho")
    for i in range(len(prediction)):
        x = (expected[i] - prediction[i]) ** 2
        result += x
    result = result / len(prediction)
    return result