#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-

import sys

if sys.version_info >= (3,0):
	xrange = range

# 2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2¹⁰⁰⁰?

# Take advantage of Python's built-in arbitrary-precision arithmetic
huge = 2 ** 1000

# Turn the whole thing into a string for shenanigans
huge = str(huge)

# Initialize a total variable for the sum
total = 0

# Sum the integer equivalents of all the one-digit substrings
for i in xrange(0, len(huge)):
	total += int(huge[i])

sys.stdout.write("The sum of all digits of 2¹⁰⁰⁰ is " + str(total) + '\n')
