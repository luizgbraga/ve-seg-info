import secrets
from utils.kyber.matrix import gen_random_matrix
from utils.kyber.noise import gen_noise
from utils.kyber.matrix_arithmetic import multiply_matrix_vector
from utils.kyber.compression import compress_vector

class Kyber:
    def __init__(self, k, eta, q, d_t):
        self.k = k
        self.eta = eta
        self.q = q
        self.d_t = d_t
        self.public_key = None
        self.secret_key = None
        self.generate_keys()
        
    def generate_keys(self):
        rho = secrets.token_bytes(32)  
        matrix = gen_random_matrix(self.k, rho, self.q)

        s = gen_noise(self.k, self.eta)
        e = gen_noise(self.k, self.eta)

        t = multiply_matrix_vector(matrix, s, self.q)
        for i in range(self.k):
            t[i] = (t[i] + e[i]) % self.q

        t_compressed = compress_vector(t, self.d_t, self.q)

        self.public_key = (t_compressed, rho)
        self.secret_key = s

    def save_keys(self):
        t_compressed, rho = self.public_key
        with open("keys/kyber_pk.key", 'wb') as f:
            f.write(rho)
            for poly in t_compressed:
                for coeff in poly:
                    f.write(int(coeff).to_bytes(2, 'little'))
        
        with open("keys/kyber_sk.key", 'wb') as f:
            for poly in self.secret_key:
                for coeff in poly:
                    f.write((int(coeff) % self.q).to_bytes(2, 'little'))