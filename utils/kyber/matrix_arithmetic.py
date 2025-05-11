import numpy as np

def poly_mul(a, b, q):
    res = np.convolve(a, b) % q
    result = np.zeros(256, dtype=int)

    for i in range(256):
        result[i] = res[i]
    for i in range(256, len(res)):
        result[i - 256] = (result[i - 256] - res[i]) % q

    return result


def multiply_matrix_vector(matrix, vector, q):
    k = len(vector)
    result = []
    for i in range(k):
        acc = np.zeros(256, dtype=int)
        for j in range(k):
            acc = (acc + poly_mul(matrix[i][j], vector[j], q)) % q
        result.append(acc)
    return np.array(result, dtype=object)