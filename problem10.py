import sys
from math import sqrt

if sys.version_info >= (3,0):
	xrange = range

# The sum of the primes below 10 is 2 + 3  + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(n):
	if n <= 3:
		return n >= 2
	if (n % 2 == 0 or n % 3 == 0):
		return False
	for k in xrange(5, int(sqrt(n)) + 1, 6):
		if n % k == 0 or n % (k + 2) == 0:
			return False
	return True

total = 0

for i in xrange(0, 2000000):
	if is_prime(i):
		total += i

sys.stdout.write("The sum of the primes below two million is: ")
sys.stdout.write(str(total) + '\n')
