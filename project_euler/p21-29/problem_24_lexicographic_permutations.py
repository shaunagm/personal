# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic 
# permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# This program works by considering the number of permutations which exist with a given character in a given digit.  This is easiest to 
# grasp when thinking of the first digit, which is all the possible permutations divided by 10.  get_digit, as explained below, finds both
# the dividend when dividing the remainder by the possible # of permutations (named "group") as well as the modulo, which becomes the 
# remainder for the next iteration.  Once we run out of remainder we simply append the remaining digits in increasing size order.

import math

digits = [0,1,2,3,4,5,6,7,8,9]
answer = []
remainder = 999999
skip = 0

def get_digit(digit,remainder):
	group = math.factorial(digit)/digit				# Determine total # of permutations possible
	count = remainder/group						# Determine how many times that goes into the remainder
	remainder = remainder%group					# Make a new remainder using mod
	if remainder == 0:
		return count,remainder,1
	else:	
		return count,remainder,0

for i in range(0,10):
	if skip < 1:
		[count,remainder,skip] = get_digit(10-i,remainder)
		popped = digits.pop(count)				# Pop the number in that index position, not the value itself
		answer.append(popped)
	else:
		for i in range(0,len(digits)):				# Just add the rest in order of increasing size.
			answer.append(digits.pop(0))

print answer

