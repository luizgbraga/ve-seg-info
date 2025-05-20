import numpy as np


def gen_psi_powers(q, n):
    psi = 17
    psi_powers = [1]
    for i in range(1, n):
        psi_powers.append((psi_powers[i - 1] * psi) % q)
    return psi_powers


def bit_reversal(a, n):
    result = np.zeros(n, dtype=int)
    for i in range(n):
        rev_i = 0
        for j in range(int(np.log2(n))):
            rev_i = (rev_i << 1) | ((i >> j) & 1)
        result[rev_i] = a[i]
    return result


def ntt_forward(a, q, psi_powers):
    n = len(a)
    result = bit_reversal(a, n)

    for stage in range(1, int(np.log2(n)) + 1):
        m = 2**stage
        m_half = m // 2
        for j in range(0, n, m):
            for k in range(m_half):
                idx = j + k
                idx2 = idx + m_half
                omega = psi_powers[k * (n // m)]

                t = (omega * result[idx2]) % q
                result[idx2] = (result[idx] - t) % q
                result[idx] = (result[idx] + t) % q

    return result


def ntt_inverse(a, q, psi_powers):
    n = len(a)
    result = a.copy()

    for stage in range(int(np.log2(n)), 0, -1):
        m = 2**stage
        m_half = m // 2
        for j in range(0, n, m):
            for k in range(m_half):
                idx = j + k
                idx2 = idx + m_half
                omega = psi_powers[(n - k * (n // m)) % n]

                t = result[idx]
                result[idx] = (t + result[idx2]) % q
                result[idx2] = (t - result[idx2]) % q
                result[idx2] = (result[idx2] * omega) % q

    result = bit_reversal(result, n)
    n_inv = pow(n, -1, q)
    for i in range(n):
        result[i] = (result[i] * n_inv) % q

    return result


def poly_mul(a, b, q):
    n = len(a)
    psi_powers = gen_psi_powers(q, n)

    a_ntt = ntt_forward(a, q, psi_powers)
    b_ntt = ntt_forward(b, q, psi_powers)

    c_ntt = [(a_ntt[i] * b_ntt[i]) % q for i in range(n)]

    c = ntt_inverse(c_ntt, q, psi_powers)

    return c


def multiply_matrix_vector(matrix, vector, q):
    k = len(vector)
    result = []
    for i in range(k):
        acc = np.zeros(256, dtype=int)
        for j in range(k):
            acc = (acc + poly_mul(matrix[i][j], vector[j], q)) % q
        result.append(acc)
    return np.array(result, dtype=object)
