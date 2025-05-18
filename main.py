from time import time

from algorithms.kyber import Kyber
from algorithms.rsa import RSA
from utils.rsa.files import save_to

rsa_start_time = time()

rsa = RSA()

rsa_end_time = time()

save_to("keys/rsa_pk.txt", rsa.public_key)
save_to("keys/rsa_sk.txt", rsa.private_key)


## Kyber
k = 2
eta = 2
q = 3329
d_t = 11

kyber_start_time = time()

kyber = Kyber(k, eta, q, d_t)

kyber_end_time = time()

kyber.save_keys()


print(f"RSA time: {rsa_end_time - rsa_start_time:.6f} seconds")
print(f"Kyber time: {kyber_end_time - kyber_start_time:.6f} seconds")
