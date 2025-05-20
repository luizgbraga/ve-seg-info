# RSA and Kyber Implementation

Implementation of RSA and Kyber (Kyber512, Kyber768, Kyber1024) cryptographic algorithms in Python, focusing on key generation performance analysis.

## Quick Start

### Direct Execution
```bash
python main.py --rsa_bits 3072 --kyber_level 128
```
Args:
- `--rsa_bits`: RSA key size (default: 3072)
- `--kyber_level`: Kyber security level in bits (128, 192, or 256)

### Run Experiments
```bash
./job.sh
```
Runs multiple iterations comparing RSA (3072, 7680 bits) with Kyber (128, 192 bits).

## Implementation Details

### RSA
- Implementation based on integer factorization
- Key generation involves:
  - Generation of large prime numbers (`p` and `q`)
  - Computation of modular inverse for private exponent
  - Operations on large integers (3072+ bits)

### Kyber
- Lattice-based KEM implementation
- Key generation involves:
  - Random matrix generation
  - Noise vector sampling
  - Polynomial arithmetic operations
  - NTT (Number Theoretic Transform) optimizations

## Performance Analysis

### Key Generation Time
- RSA 3072: 15.83s
- Kyber 512: 0.38s
- Kyber is ~42x faster than RSA for key generation

The performance gap stems from the fundamental differences in mathematical operations:
- RSA: Computationally intensive prime generation and modular inverse calculations
- Kyber: Efficient polynomial arithmetic and NTT optimizations

### Memory Usage
- RSA 3072: 
  - Peak: 60.3 MiB
  - Post-generation: 45.2 MiB
  - Variation: -8.6 MiB (likely due to garbage collection)
- Kyber 512:
  - Peak: 48 MiB
  - Base: 46.3 MiB
  - Variation: +0.5 MiB

Kyber demonstrates more stable memory allocation patterns compared to RSA's more volatile usage.

## Project Structure
```
.
├── algorithms/
│   ├── rsa.py
│   ├── kyber.py
│   └── kyber_versions.py
├── utils/
│   ├── kyber/
│   └── rsa/
├── keys/
├── main.py
└── job.sh
```
