# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# 36: 1,2,3,4,9,12,18,36
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

import math

def get_divisors(number):
	small_divisors = [1]
	large_divisors = [number]
	h = 1
	while (h < large_divisors[len(large_divisors)-1]):   # Check that all divisors are less than large divisors, large_divisors will be descending
		if (number%h == 0):
			small_divisors.append(h)
			large_divisors.append(number/h)
		h += 1
	return len(small_divisors) + len(large_divisors)

divisors = 0
i = 1
sum = 0
while(divisors < 501):
	sum += i
	i += 1
	divisors = get_divisors(sum)
print sum

