import sys

# A palindromic number reads the same both ways. The largest palidromic
# number made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

largest = -1

for j in xrange(100, 999, 1):
	for k in xrange(100, 999, 1):
		check = j * k
		if str(check) == str(check)[::-1]: # gnarly syntax for reverse
			if check > largest:
				largest = check

sys.stdout.write("Largest palindromic product of two 3-digits ints is: ")
sys.stdout.write(str(largest) + "\n")
