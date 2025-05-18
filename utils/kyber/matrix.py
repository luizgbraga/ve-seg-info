import hashlib
import numpy as np

def gen_random_pol(seed, i, j, q):
    seed_i_j = seed + (i).to_bytes(1, 'little') + (j).to_bytes(1, 'little') 
    shake = hashlib.shake_128()
    shake.update(seed_i_j)
    pol = np.zeros(256, dtype=int)
    unfilled_coefficients = 0
    
    while unfilled_coefficients < 256:
        extracted_bytes = shake.digest(384)
        idx = 0
        
        while idx < len(extracted_bytes) and unfilled_coefficients < 256:
            if idx + 1 >= len(extracted_bytes):
                break
                
            d1 = extracted_bytes[idx]
            d2 = extracted_bytes[idx + 1]
            idx += 2
            
            val = (d1 << 8) | d2
            
            if val < 19 * q:
                coef = val % q
                pol[unfilled_coefficients] = coef
                unfilled_coefficients += 1
    
    return pol

def gen_random_matrix(k, rho, q):
    matrix = np.zeros((k, k), dtype=object)
    for i in range(k):
        for j in range(k):
            matrix[i][j] = gen_random_pol(rho, i, j, q)
    return matrix