import math

def largest_prime_factor(n):
    i = 2
    # Find a factorization then recursively find largest prime factors
    while i <= math.sqrt(n):
        if n % i == 0:
            return max(largest_prime_factor(i), largest_prime_factor(n/i))
        i += 1
    # Base case: n is a prime number
    return n