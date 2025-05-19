import argparse
from time import time

from algorithms.kyber_versions import Kyber512, Kyber768, Kyber1024
from algorithms.rsa import RSA
from utils.rsa.files import save_to

# Added: Argument parsing
parser = argparse.ArgumentParser(description="Run RSA and Kyber key generation.")
parser.add_argument('--rsa_bits', type=int, default=3072, help='RSA key size in bits.')
parser.add_argument('--kyber_level', type=int, default=128, choices=[128, 192, 256], help='Kyber security level in bits (128, 192, or 256).')
args = parser.parse_args()

rsa_start_time = time()

rsa = RSA(bits=args.rsa_bits)

rsa_end_time = time()

save_to("keys/rsa_pk.txt", rsa.public_key)
save_to("keys/rsa_sk.txt", rsa.private_key)


## Kyber
kyber_start_time = time()

if args.kyber_level == 128:
    kyber = Kyber512()
    kyber_bit_label = 128
elif args.kyber_level == 192:
    kyber = Kyber768()
    kyber_bit_label = 192
elif args.kyber_level == 256:
    kyber = Kyber1024()
    kyber_bit_label = 256
else:
    print(f"Warning: Invalid Kyber level {args.kyber_level}. Defaulting to Kyber512 (128 bits).")
    kyber = Kyber512()
    kyber_bit_label = 128


kyber_end_time = time()

kyber.save_keys()


print(f"RSA ({args.rsa_bits} bits) time: {rsa_end_time - rsa_start_time:.6f} seconds")
print(f"Kyber ({kyber_bit_label} bits) time: {kyber_end_time - kyber_start_time:.6f} seconds")
