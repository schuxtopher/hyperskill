prime_numbers = [n for n in range(2, 1001) if all(n % d for d in range(2, n))]
