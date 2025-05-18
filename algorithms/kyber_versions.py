from algorithms.kyber import Kyber

class Kyber512(Kyber):
    def __init__(self):
        super().__init__(2, 2, 3329, 10)

class Kyber768(Kyber):
    def __init__(self):
        super().__init__(3, 2, 3329, 10)

class Kyber1024(Kyber):
    def __init__(self):
        super().__init__(4, 2, 3329, 11)