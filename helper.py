from math import sqrt

wheel = [2,4,2,4,6,2,6,4,2,4,6,6,
2,6,4,2,6,4,6,8,4,2,4,2,
4,8,6,4,6,2,4,6,2,6,6,4,
2,4,6,2,6,4,2,4,2,10,2,10]
	
prime_list = [2, 3, 5, 7]
	
def fibonacci(n):
	if (n <= 1):
		return n
	curr = 2
	prev = 1
	for i in range (2, n - 1):
		temp = curr
		curr += prev
		prev = temp
	return curr

def is_prime(n, prime_list):
	limit = sqrt(n)
	for i in prime_list:
		if n % i == 0:
			return False
		elif i > limit:
			break
	return True

def generate_primes(num_primes):		
	# Appends to prime_list
	index = 0
	step = 11 
	size = len(wheel)

	while len(prime_list) < num_primes:
		temp = step
		step += wheel[index]
		index = (index + 1) % 1
		if is_prime(temp, prime_list):
			prime_list.append(temp)

