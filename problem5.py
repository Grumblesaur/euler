import sys

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder. What is the smallest
# positive number that is evenly divisible by all of the numbers
# from 1 to 20?

# Use the 1-10 solution as a start point, as 1-20's solution
# will have to be divisible by it.
i = 2520

# Use non-redundant factors.
factors = [11, 13, 14, 16, 17, 18, 19, 20]

# Create variable for loop termination
found = False

# Initiate variable for smallest number divisible by 1-20.
smallest = 0

# Loop to find solution
while found == False:
	for j in range(0, len(factors)):
		# If the current number is divisible by a factor,
		# try the next factor.
		if i % factors[j] == 0:
			found = True
		# If the current number isn't divisible by a factor,
		# try the next number.
		elif i % factors[j] != 0:
			found = False
			break
	if found == True:
		smallest = i
	elif found == False:
		# Increment by a number that's guaranteed to be divisible
		# by numbers 1-10, which a number divisible by 1-20 must
		# also be.
		i += 2520

# It's safe to lose the additional while-loop condition since
# the program is mathematically guaranteed to exit.

sys.stdout.write("The smallest number divisible by all numbers 1-20 is: ")
sys.stdout.write(str(smallest))
