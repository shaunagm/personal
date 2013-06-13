# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math

def get_factors(factors):
	i = 2					# start at 2, as 1 is a factor of all numbers
	number = factors[len(factors)-1]	# take the most recently added number in list factors
	while (i <= number/2):
		if (number%i == 0):   			# if i is a factor of number
			factors[len(factors)-1] = i		# replace old number with found factor
			factors.append(number/i)		# append new "remainder" number to still be factored
			factors = get_factors(factors)		# call factors on the new remainder number
			break
		i += 1
	return factors

factors = [600851475143]  		# base number to factor
print get_factors(factors)





