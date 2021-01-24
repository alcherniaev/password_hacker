prime_numbers = [i for i in range(2, 1001) if all([i % i == 0, i % 1 == 0]) and all(i % n != 0 for n in range(2, i-1))]

