import numpy as np


def compress_vector(vector, coeff_size, q):
    n = len(vector)
    compressed_vector = np.zeros(n, dtype=object)
    for i in range(n):
        pol = vector[i]
        compressed_pol = np.zeros(256, dtype=int)
        for j in range(256):
            compressed_pol[j] = (
                (pol[j] * (1 << coeff_size) + q // 2) // q % (1 << coeff_size)
            )
        compressed_vector[i] = compressed_pol
    return compressed_vector
