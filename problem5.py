import sys, math

# 2050 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder. What is the smallest
# positive number that is evenly divisible by all of the numbers
# from 1 to 20?

inc = lambda x: x + 1

# stop upon reaching 20! since it's obviously divisible by all
# numbers 1 through 20, but is almost certainly not the smallest
loop_max = math.factorial(20)

# don't need to bother with the factor numbers
i = 2520

factors = [11, 13, 14, 16, 17, 18, 19, 20]

found = False

smallest = -1

while i < loop_max and found == False:
	for j in range(0, len(factors)):
		if i % factors[j] == 0:
			found = True
		elif i % factors[j] != 0:
			found = False
			break
	if found == True:
		smallest = i
	elif found == False:
		i += 2520

sys.stdout.write("The smallest number divisible by all numbers 1-20 is: ")

if smallest != -1:
	sys.stdout.write(str(smallest))
else:
	sys.stdout.write(str(loop_max))

sys.stdout.write("\n Program finished. \n")
