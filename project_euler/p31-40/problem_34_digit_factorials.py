# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

def factorialDigitSum(number):
	factorialSum = 0
	for i in str(number):
		factorialSum += math.factorial(int(i))
	return factorialSum

sumAll = 0

for i in range(3,99999):   
	if i == factorialDigitSum(i):
		sumAll += i

print sumAll

# Notes:

# It turns out there are only two numbers equal to the sum of their digits factorialized.
# They're both < 99999, so you can get the correct answer in seconds, but to truly rule out
# the others (since there's no upper bound given) it takes longer and longer until there's a
# memory error.  

