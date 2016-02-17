import sys

# n! means n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the
# digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

# Find the sum of the digits in the number 100!

def factorial(n):
	if n == 0:
		return 1
	fact = 1
	while n > 1:
		fact *= n
		n -= 1
	return fact

total = sum(map(int, str(factorial(100))))

sys.stdout.write("The sum of the digits of 100! is " + str(total) + '\n')
