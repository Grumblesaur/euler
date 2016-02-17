import sys
from math import sqrt
import helper

if sys.version_info >= (3,0):
	xrange = range

# The number 197 is called a circular prime because all rotations of the
# digits: 197, 971, 719, are themselves prime. There are thirteen such
# primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

# Variable to track number of circular primes
count = 0

for i in xrange(2, 1000000):
	# Variables to track rotations of i
	temp = str(i)
	rotations = 0
	length = len(temp)
	# Rotate number until we either find a non-prime or
	# rotate all the way around to start again.
	while helper.is_prime(int(temp)) and rotations < length:
		temp = temp[1:] + temp[0]
		rotations += 1
	# Increment the count if we find a circular prime
	if rotations == length:
		count += 1

sys.stdout.write("There are " + str(count))
sys.stdout.write(" circular primes below 1,000,000. \n")
