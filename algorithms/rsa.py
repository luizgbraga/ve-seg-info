import logging

from Crypto.Util.number import getStrongPrime
from memory_profiler import profile

from utils.rsa.arithmetic import find_mod_inv, gcd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RSA:
    @profile
    def __init__(self, bits: int = 3072, e: int = 65537):
        if bits < 3072:
            logger.warning(
                "RSA bit length is less than 3072; this might be unsafe for cryptographic use."
            )
        self.e = e
        self._generate_keys(bits)

    @profile
    def _generate_keys(self, bits: int):
        half_bits = bits // 2
        while True:
            self._p = getStrongPrime(half_bits, e=self.e)
            self._q = getStrongPrime(half_bits, e=self.e)
            if self._p != self._q:
                break

        self.n = self._p * self._q
        self.phi = (self._p - 1) * (self._q - 1)
        self._ensure_valid_e(self.e)
        self._d = find_mod_inv(self.e, self.phi)

    def _ensure_valid_e(self, e: int):
        if e <= 1 or e >= self.phi:
            raise ValueError("e must be between 1 and phi(n)")
        if gcd(e, self.phi) != 1:
            raise ValueError("e must be coprime to phi(n)")

    @property
    def public_key(self):
        return (self.e, self.n)

    @property
    def private_key(self):
        return (self._d, self.n)
