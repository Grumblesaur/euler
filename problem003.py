import sys

# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of 600,851,475,143

composite = 600851475143

def largest_factor(n):
	list_of_factors = []
	i = 2
	while i * i <= n:
		while n % i == 0:
			list_of_factors.append(i)
			n //= i
		i += 1
	if n > 1:
		list_of_factors.append(n)

	largest = list_of_factors[0]

	for i in range(1, len(list_of_factors)):
		if list_of_factors[i] > list_of_factors[i - 1]:
			largest = list_of_factors[i]
	return largest

largest = largest_factor(composite)

sys.stdout.write("The largest prime factor of 600,851,475,143 is: ")
sys.stdout.write(str(largest) + '\n')
