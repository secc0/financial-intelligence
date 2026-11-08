def dotProduct(x, w):

    if len(x) != len(w):
        raise ValueError("Os valores precisam ter o mesmo tamanho")

    result = 0
    for i in range(len(x)):
        result += float(x[i] * w[i])
    return result

x = [2, 3, 4]
w = [0.5, 0.2, 0.1]

print(dotProduct(x, w))