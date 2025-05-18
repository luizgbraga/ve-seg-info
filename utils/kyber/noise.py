import random

import numpy as np


def gen_noise(k, eta):
    noise_vector = np.zeros((k, 256), dtype=int)
    for i in range(k):
        for j in range(256):
            noise = 0
            for _ in range(eta):
                bit_a = random.getrandbits(1)
                bit_b = random.getrandbits(1)
                noise += bit_a - bit_b
            noise_vector[i][j] = noise
    return noise_vector
