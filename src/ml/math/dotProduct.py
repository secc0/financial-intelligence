def dotProduct(x, w):

    if len(x) != len(w):
        raise ValueError("Os valores precisam ter o mesmo tamanho")

    result = 0
    for i in range(len(x)):
        result += float(x[i] * w[i])
    return result