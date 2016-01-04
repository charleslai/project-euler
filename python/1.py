
def sum_of_multiples(n):
	s = 0
	for i in range(n):
		if (i % 3 == 0) or (i % 5 == 0):
			s += i
	return s

print sum_of_multiples(1000)
