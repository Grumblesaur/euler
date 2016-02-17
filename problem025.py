import sys
import helper
# The Fibonacci sequence is defined by the recurrence relation:
	# F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.

# Hence the first twelve terms will be:
	# F_1 = 1
	# F_2 = 1
	# F_3 = 2
	# F_4 = 3
	# F_5 = 5
	# F_6 = 8
	# F_7 = 13
	# F_8 = 21
	# F_9 = 34
	# F_10 = 55
	# F_11 = 89
	# F_12 = 144

# The 12th term, F_12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

term = 1
found = False

while found == False:
	if len(str(helper.fibonacci(term))) >= 1000:
		found = True
	else:
		term += 1

term = str(term)

sys.stdout.write("The first term in the Fibonacci sequence to contain ")
sys.stdout.write("1000 digits\nis term " + term + ".\n")
