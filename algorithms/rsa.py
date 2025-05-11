from utils.rsa.arithmetic import find_mod_inv, gcd


class RSA:
    def __init__(self, p: int, q: int, e: int):
        self._p = p
        self._q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self._ensure_valid_e(e)
        self.e = e
        self._d = find_mod_inv(e, self.phi)

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
