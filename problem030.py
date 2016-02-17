#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-

import sys

if sys.version_info >= (3,0):
	xrange = range

# Surprisingly there are only three numbers that can be written as the sum
# of fourth powers of their digits:

	# 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
	# 8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
	# 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴

# As 1 = 1⁴ is not a sum, it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth
# powers.

def is_digit_fifth_power(n):
	digits = str(n)
	
	digitTotal = 0
	
	for i in digits:
		digitTotal += int(i) ** 5
	
	return digitTotal == n

total = 0

for j in xrange(2, 999999):
	if is_digit_fifth_power(j):
		total += j

sys.stdout.write("Sum of digit fifth powers is: " + str(total) + '\n')
