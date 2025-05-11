from time import time

from algorithms.rsa import RSA
from utils.rsa.files import save_to
from algorithms.kyber import Kyber

## RSA
P = 104677
Q = 86729
e = 19

rsa_start_time = time()

rsa = RSA(P, Q, e)
save_to("keys/rsa_pk.txt", rsa.public_key)
save_to("keys/rsa_sk.txt", rsa.private_key)

rsa_end_time = time()

## Kyber
k = 2  
eta = 2
q = 3329
d_t = 11

kyber_start_time = time()

kyber = Kyber(k, eta, q, d_t)
kyber.save_keys()

kyber_end_time = time()

print(f"RSA time: {rsa_end_time - rsa_start_time:.6f} seconds")
print(f"Kyber time: {kyber_end_time - kyber_start_time:.6f} seconds")