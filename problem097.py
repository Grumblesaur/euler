#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-
import sys

if sys.version_info >= (3,0):
	xrange = range

# The first known prime found to exceed one million digits was discovered
# in 1999, and is a Mersenne prime number of the form 2⁶⁹⁷²⁵⁹³ - 1; it
# contains exactly 2,098,960 digits. Subsequently, other Mersenne primes of
# the form 2^p - 1, have been found to contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which
# contains 2,357,207 digits: 28433 * 2⁷⁸³⁰⁴⁵⁷ + 1.

# Find the last ten digits of this prime number.

n = 2

# Brute force it the smart way, don't overdo it with Python's bignums
for i in xrange(7830456):
	n = (n * 2) % 10000000000

# Tack on those extra numbers that don't involve insane exponentiation
n = str(n * 28433 + 1)
# Grab  the important slice of the string.
n = n[len(n) - 10:]

sys.stdout.write("The last ten digits of this number are " + n)
sys.stdout.write('\n')
