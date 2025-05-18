from time import time

from algorithms.kyber_versions import Kyber512, Kyber768, Kyber1024
from algorithms.rsa import RSA
from utils.rsa.files import save_to

rsa_start_time = time()

rsa = RSA()

rsa_end_time = time()

save_to("keys/rsa_pk.txt", rsa.public_key)
save_to("keys/rsa_sk.txt", rsa.private_key)


## Kyber
kyber_start_time = time()

kyber = Kyber512()

kyber_end_time = time()

kyber.save_keys()


print(f"RSA time: {rsa_end_time - rsa_start_time:.6f} seconds")
print(f"Kyber time: {kyber_end_time - kyber_start_time:.6f} seconds")
