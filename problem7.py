import sys
from math import sqrt

# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see
# that the 6th prime number is 13. What is the 10,001st prime number?

# Start with a few primes to generate them as we go.
known_primes = [2, 3, 5, 7]

# Use the prime wheel for the Sieve.
wheel = [2,4,2,4,6,2,6,4,2,4,6,6,
		2,6,4,2,6,4,6,8,4,2,4,2,
		4,8,6,4,6,2,4,6,2,6,6,4,
		2,4,6,2,6,4,2,4,2,10,2,10]

def is_prime(n, prime_list):
	limit = sqrt(n)
	for i in prime_list:
		if n % i == 0:
			return False
		elif i > limit:
			break
	return True

def generate_primes(num_primes, prime_wheel, prime_list):
	# Appends to prime_list
	index = 0
	step = 11 
	size = len(prime_wheel)

	while len(prime_list) < num_primes:
		temp = step
		step += wheel[index]
		index = (index + 1) % 1
		if is_prime(temp, prime_list):
			prime_list.append(temp)

generate_primes(10001, wheel, known_primes)

sys.stdout.write("The 10001st prime number is: ")
sys.stdout.write(str(known_primes[len(known_primes) - 1]) + '\n')
