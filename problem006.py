#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-

import sys

# Sum square difference
# The sum of the squares of the first ten natural numbers is
	# 1² + 2² + ... + 10² = 385

# The square of the sum of the first ten natural numbers is
	# (1 + 2 + ... + 10)² = 55² = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares and the square
# of the sum of the first hundred natural numbers (1-100).

def sum_of_squares(x):
	sumsquares = 0
	for i in range(1, x + 1):
		sumsquares += (i * i)
	return sumsquares

def square_of_sum(x):
	squaresum = 0
	for j in range(1, x + 1):
		squaresum += j
	squaresum *= squaresum
	return squaresum

num = 100

difference = square_of_sum(num) - sum_of_squares(num)

sys.stdout.write("The sum square difference of numbers 1-")
sys.stdout.write(str(num))
sys.stdout.write(" is ")
sys.stdout.write(str(difference))
sys.stdout.write('\n')
