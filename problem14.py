import sys

if sys.version_info >= (3,0):
	xrange = range

# The following iterative sequence is defined for the set of positive
# integers:
	
	# n -> n / 2 where n is even
	# n -> 3n + 1 where n is odd

# Using the rule above and starting with 13, we generate the following
# sequence:
	
	# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proven yet (the Collatz
# Problem), it is thought that all starting numbers finish at 1.

# Which starting number below one million produces the longest chain?

# NOTE: Once the chain starts, the terms are allowed to surpass one million.

def collatz(start):
	curr = start
	
	sequenceLength = 1
	
	while (curr > 1):
		if (curr % 2 == 0):
			curr //= 2
			sequenceLength += 1

		elif (curr % 2 != 0):
			curr *= 3
			curr += 1
			sequenceLength += 1
	
	# increment length upon reaching 1
	sequenceLength += 1
	
	return sequenceLength

bestStart = 2
bestLength = 2

for i in xrange(2, 1000000):
	currentLength = collatz(i)
	if (currentLength > bestLength):
		bestLength = currentLength
		bestStart = i

sys.stdout.write("The longest Collatz sequence with a starting value \n")
sys.stdout.write("below 1,000,000 begins with "+ str(bestStart) +" and \n")
sys.stdout.write("has length " + str(bestLength) + '\n')
