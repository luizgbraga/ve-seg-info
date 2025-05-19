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
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Make sure you have pip installed. Then, run the following command in the project's root directory (where `requirements.txt` is located):
    ```bash
    pip install -r requirements.txt
    ```
    The required dependencies are:
    - `memory-profiler`
    - `numpy`
    - `psutil`

4.  **Run the project:**
    Execute the main script:
    ```bash
    python main.py
    ```
    This will generate RSA and Kyber512 keys and print the time taken for each. RSA keys will be saved in the `keys/` directory. The location of Kyber keys depends on its `save_keys()` implementation.

## Discussion

This project serves as a practical example of implementing and comparing two different types of public-key cryptographic algorithms:
-   **RSA:** A traditional algorithm based on the difficulty of factoring large integers.
-   **Kyber:** A Key Encapsulation Mechanism (KEM) selected by NIST for post-quantum cryptography standardization, based on the hardness of solving learning with errors (LWE) problems over module lattices.

The `main.py` script provides a basic benchmark for the key generation phase of RSA and Kyber512. This is an interesting comparison point, as key generation performance can be a significant factor in the practical application of cryptographic schemes.
