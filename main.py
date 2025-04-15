from time import time

from algorithms.rsa import RSA
from utils.files import save_to

P = 104677
Q = 86729
e = 19

start_time = time()

rsa = RSA(P, Q, e)
save_to("keys/rsa_pk.txt", rsa.public_key)
save_to("keys/rsa_sk.txt", rsa.private_key)

end_time = time()

print(f"RSA time: {end_time - start_time:.6f} seconds")
