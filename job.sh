#!/bin/bash

export PYTHONPATH="${PYTHONPATH}:$(pwd)"

RSA_BITS_LEVELS=(3072 7680)
SECURITY_LEVELS=(128 192)

NUM_ITERATIONS=5

rsa_3072_total=0
rsa_7680_total=0
kyber_128_total=0
kyber_192_total=0

echo "=============================================="
echo " Starting Key Generation Benchmark"
echo "=============================================="
echo ""

for i in $(seq 1 $NUM_ITERATIONS); do
  echo "Running iteration $i/$NUM_ITERATIONS..."

  for idx in ${!RSA_BITS_LEVELS[@]}; do
    bits=${RSA_BITS_LEVELS[$idx]}
    security=${SECURITY_LEVELS[$idx]}

    OUTPUT=$(python main.py --rsa_bits $bits --kyber_level $security 2>&1)

    RSA_TIME=$(echo "$OUTPUT" | grep "\[RESULT\] RSA" | grep -o "[0-9]*\.[0-9]*")
    KYBER_TIME=$(echo "$OUTPUT" | grep "\[RESULT\] Kyber" | grep -o "[0-9]*\.[0-9]*")

    RSA_TIME=${RSA_TIME:-0}
    KYBER_TIME=${KYBER_TIME:-0}

    # Accumulate
    if [ "$bits" -eq 3072 ]; then
      rsa_3072_total=$(echo "$rsa_3072_total + $RSA_TIME" | bc)
    else
      rsa_7680_total=$(echo "$rsa_7680_total + $RSA_TIME" | bc)
    fi

    if [ "$security" -eq 128 ]; then
      kyber_128_total=$(echo "$kyber_128_total + $KYBER_TIME" | bc)
    else
      kyber_192_total=$(echo "$kyber_192_total + $KYBER_TIME" | bc)
    fi
  done
done

rsa_3072_mean=$(echo "scale=6; $rsa_3072_total / $NUM_ITERATIONS" | bc)
rsa_7680_mean=$(echo "scale=6; $rsa_7680_total / $NUM_ITERATIONS" | bc)
kyber_128_mean=$(echo "scale=6; $kyber_128_total / $NUM_ITERATIONS" | bc)
kyber_192_mean=$(echo "scale=6; $kyber_192_total / $NUM_ITERATIONS" | bc)

echo ""
echo "=============================================="
echo " Mean Key Generation Times (in seconds)"
echo "=============================================="
printf "%-15s %-10s\n" "Key Type" "Mean Time"
echo "-------------------------------"
printf "%-15s %-10s\n" "RSA 3072" "$rsa_3072_mean"
printf "%-15s %-10s\n" "RSA 7680" "$rsa_7680_mean"
printf "%-15s %-10s\n" "Kyber 128" "$kyber_128_mean"
printf "%-15s %-10s\n" "Kyber 192" "$kyber_192_mean"