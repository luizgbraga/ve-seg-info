#!/bin/bash

export PYTHONPATH="${PYTHONPATH}:$(pwd)"

RSA_BITS_LEVELS=(3072 7680)
SECURITY_LEVELS=(128 192)

NUM_ITERATIONS=5

echo "=============================================="
echo " Starting Key Generation Benchmark"
echo "=============================================="
echo ""

for i in $(seq 1 $NUM_ITERATIONS)
do
  echo "=============================================="
  echo "---------------- Iteration $i ----------------"
  echo "=============================================="
  for idx in ${!RSA_BITS_LEVELS[@]}
  do
    bits=${RSA_BITS_LEVELS[$idx]}
    security=${SECURITY_LEVELS[$idx]}
    echo " "
    echo " "
    echo "--- Running for RSA ${bits} bits & Kyber ${security} bits security ---"
    echo " "
    echo " "
    python main.py --rsa_bits $bits --kyber_level $security
  done
  echo "--------------------------------------------"
  echo ""
done

echo "=============================================="
echo " All experiments finished."
echo "==============================================" 