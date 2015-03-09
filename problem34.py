import sys
from math import factorial

if sys.version_info >= (3,0):
	xrange = range

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all the numbers which are equal to the sum of the
# factorial of their digits.

# arbitrary upper limit, since exceptionally large numbers' factorial sums
# grow too quickly to fall under this range

LOOP_MAX = 1000000

total = 0

for i in xrange(3, LOOP_MAX):
	# create string of current number
	digits = str(i)
	
	# create list of factorials of digits
	digitFactorials = []
	
	# create total-of-digit-factorials variable
	factTotal = 0
	
	# append factorial values to list
	for j in xrange(0, len(digits)):
		digitFactorials.append(factorial(int(digits[j])))
	
	# sum factorials
	for k in xrange(0, len(digitFactorials)):
		factTotal += digitFactorials[k]
	
	# add to total if the number is like 145
	if i == factTotal:
		total += i
	
total = str(total) + '\n'
sys.stdout.write("The sum of all digit factorial numbers is: " + total)

