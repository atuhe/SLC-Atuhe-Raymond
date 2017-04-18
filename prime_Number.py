def prime_number_generator(n):
    j = 2
    primes = []
    while j <= n:
        k = 2
        while not (k == j) and not (j % k == 0):
            k = k + 1
            if k == j:
                primes.append(j)
        j = j + 1
    return primes

print (prime_number_generator(15))