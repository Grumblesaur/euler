import sys
import helper

# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see
# that the 6th prime number is 13. What is the 10,001st prime number?

helper.generate_primes(10001)

sys.stdout.write("The 10001st prime number is: ")
sys.stdout.write(str(helper.prime_list[len(helper.prime_list) - 1]) + '\n')
