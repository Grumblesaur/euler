import sys

if sys.version_info >= (3,0):
	xrange = range

# Each new term in the Fibonacci sequence is generated by adding the two
# previous terms. By starting with 1 and 2, the first 10 terms will be:
	# 1, 2, 3, 5, 8, 13, 21, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed 4,000,000, find the sum of the even-valued terms.

# Total variable to track sum
total = 0

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

# Term iterator
val = 2
i = 1

while val <= 4000000:
	val = fibonacci(i)
	if val % 2 == 0:
		total += val
	i += 1

total = int(total) - 2 # extra 2 shows up in loop, get rid of it

sys.stdout.write("The sum of even Fibonacci terms below 4 million is: ")
sys.stdout.write(str(total) + "\n")	
