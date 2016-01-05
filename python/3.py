import math

def largest_prime_factor(n):
	# Check up to sqrt(n) for factors
	i = 2
	while i <= math.sqrt(n):
		# Recursively find largest prime factors of factors
		if n % i == 0:
			return max(largest_prime_factor(i), largest_prime_factor(n/i))
		i += 1
	# If the loop finishes, then n is a prime number and largest_n = n
	return n