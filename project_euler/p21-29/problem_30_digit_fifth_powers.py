# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44

# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math

def get_sum(number):
	sum = 0
	for i in range(0,len(str(number))):
		fifth = math.pow(int(str(number)[i]),5)
		sum += fifth
	return sum
	

total_sum = 0

for number in range(2,999999):	# What should the cut-off be?
	sum = 0
	sum = get_sum(number)
	if sum == number:
		total_sum += sum

print total_sum