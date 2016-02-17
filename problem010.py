import sys
import helper

if sys.version_info >= (3,0):
	xrange = range

# The sum of the primes below 10 is 2 + 3  + 5 + 7 = 17.
# Find the sum of all the primes below two million.

total = 0

for i in xrange(0, 2000000):
	if helper.is_prime(i):
		total += i

sys.stdout.write("The sum of the primes below two million is: ")
sys.stdout.write(str(total) + '\n')
