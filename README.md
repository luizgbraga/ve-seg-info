# RSA and Kyber Implementation

## Introduction

This project provides Python implementations of the RSA and Kyber (specifically Kyber512, Kyber768, and Kyber1024) cryptographic algorithms. The primary focus is on key generation for these algorithms, and the `main.py` script measures and compares the time taken for this process for RSA and Kyber512.

The project is structured as follows:
- `main.py`: The main script that runs the key generation for RSA and Kyber512 and prints the execution time.
- `algorithms/`: Contains the implementations of the cryptographic algorithms.
    - `rsa.py`: Implementation of the RSA algorithm.
    - `kyber.py`: Base implementation of the Kyber algorithm.
    - `kyber_versions.py`: Defines specific Kyber versions (Kyber512, Kyber768, Kyber1024) based on the base Kyber implementation.
- `utils/`: Contains utility functions, likely for supporting the algorithm implementations (e.g., file operations, mathematical operations).
    - `kyber/`: Utilities specific to Kyber.
    - `rsa/`: Utilities specific to RSA, including file saving for keys.
- `keys/`: This directory is used to store the generated cryptographic keys. By default, RSA public and private keys are saved here.
- `requirements.txt`: Lists the Python dependencies for this project.

## Installation Guide

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/luizgbraga/ve-seg-info
    cd ve-seg-info
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    Or, on windows use:
    ```bash
    python3 -m venv venv
    venv\Scripts\activate
    ```

4.  **Install dependencies:**
    Make sure you have pip installed. Then, run the following command in the project's root directory (where `requirements.txt` is located):
    ```bash
    pip install -r requirements.txt
    ```
    The required dependencies are:
    - `memory-profiler`
    - `numpy`
    - `psutil`

5.  **Run the project:**
    Execute the benchmark script:
    ```bash
    bash job.sh
    ```
    This script will run a series of benchmarks, testing RSA with different key sizes (3072, 7680, 15360 bits) and pairing them with corresponding Kyber security levels (128, 192, 256 bits respectively). It will perform multiple iterations and print the key generation time for each algorithm and configuration. The generated keys will be saved in the `keys/` directory.

## Discussion

This project serves as a practical example of implementing and comparing two different types of public-key cryptographic algorithms:
-   **RSA:** A traditional algorithm based on the difficulty of factoring large integers.
-   **Kyber:** A Key Encapsulation Mechanism (KEM) selected by NIST for post-quantum cryptography standardization, based on the hardness of solving learning with errors (LWE) problems over module lattices.

The `main.py` script provides a basic benchmark for the key generation phase of RSA and Kyber512. This is an interesting comparison point, as key generation performance can be a significant factor in the practical application of cryptographic schemes.

The performance difference observed (e.g., RSA taking significantly longer than Kyber for key generation) is characteristic of these two cryptographic algorithms. Here's a breakdown of why Kyber generally outperforms RSA in operations like key generation:

1.  **Underlying Mathematical Problems:**
    *   **RSA:** Relies on the difficulty of integer factorization. Operations like modular exponentiation with very large numbers (e.g., 3072-bit moduli) are computationally intensive. Generating keys involves finding large prime numbers and performing several modular arithmetic operations.
        The core of RSA's computational cost in key generation lies in finding these large prime numbers and subsequently calculating the modular inverse for the private exponent. In `algorithms/rsa.py`, the `_generate_keys` method highlights this:
        ```python
        # from algorithms/rsa.py
        # ...
            def _generate_keys(self, bits: int):
                half_bits = bits // 2
                while True:
                    self._p = getStrongPrime(half_bits, e=self.e) # Computationally intensive prime generation
                    self._q = getStrongPrime(half_bits, e=self.e) # Computationally intensive prime generation
                    if self._p != self._q:
                        break

                self.n = self._p * self._q
                self.phi = (self._p - 1) * (self._q - 1)
                self._ensure_valid_e(self.e)
                self._d = find_mod_inv(self.e, self.phi) # Computationally intensive modular inverse
        # ...
        ```
    *   **Kyber:** Is a key-encapsulation mechanism (KEM) based on the hardness of solving Learning With Errors (LWE) problems over module lattices. The core operations in Kyber involve polynomial arithmetic (multiplication, addition) in a polynomial ring, often implemented using Number Theoretic Transform (NTT) for efficiency. These operations are significantly faster than the large number arithmetic required by RSA for equivalent security levels.
        In `algorithms/kyber.py`, the key generation involves generating a random matrix, sampling noise vectors (polynomials with small coefficients), and performing matrix-vector multiplications and additions:
        ```python
        # from algorithms/kyber.py
        # ...
            def generate_keys(self):
                rho = secrets.token_bytes(32)
                matrix = gen_random_matrix(self.k, rho, self.q) # Involves hashing and polynomial generation

                s = gen_noise(self.k, self.eta) # Sampling small coefficient polynomials
                e = gen_noise(self.k, self.eta) # Sampling small coefficient polynomials

                t = multiply_matrix_vector(matrix, s, self.q) # Polynomial matrix-vector multiplication
                for i in range(self.k):
                    t[i] = (t[i] + e[i]) % self.q # Polynomial addition
        # ...
        ```

2.  **Key Sizes and Operational Complexity:**
    *   RSA requires very large keys (e.g., 3072 bits or more) for strong security.
    *   Kyber can achieve comparable or higher security levels with much smaller key sizes. The operations in Kyber (sampling from distributions, polynomial additions, and multiplications) are inherently less complex per bit of security compared to RSA's modular exponentiations.

3.  **Optimization for Modern Processors:**
    *   Lattice-based cryptography, including Kyber, often involves operations that can be highly optimized and parallelized on modern computer architectures. Polynomial arithmetic, especially when implemented with NTT, maps well to processor capabilities.

4.  **Post-Quantum Security Context:**
    *   Kyber was selected by NIST as a standard for post-quantum cryptography because it is believed to be resistant to attacks by future large-scale quantum computers, which would easily break RSA. This has spurred intense research and optimization in algorithms like Kyber.

In summary, Kyber's speed advantage comes from its foundation in lattice-based cryptography, which employs more computationally efficient mathematical operations (polynomial arithmetic) compared to RSA's reliance on number theory problems requiring operations on very large integers.
