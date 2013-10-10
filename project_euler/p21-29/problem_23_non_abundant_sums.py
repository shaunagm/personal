# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of 
# the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
# numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import time 

# Checks to see if a number is abundant
def is_abundant(number):
	sum = 1									# Assume 1, since it's a divisor of everything.
	current_num = 2		
	lowest_num = number/2
	while current_num < lowest_num	:					# This is never entered for numbers < 4 which is fine, since 1-4 are primes and therefore not abundant anyway
		if number%current_num == 0:					# If it's a divisor...
			sum += current_num					# Add to sum
			if current_num != number/current_num:			# Takes care of squares, roots of which do not apparently count twice as advisors THANKS FOR SPECIFYING THAT, PROJECT EULER :(
				sum += number/current_num
			lowest_num = number/current_num				# Saves time by only having to find the first half of the divisors
		current_num += 1
	if sum > number:
		return 1
	return 0

abundant_list = [0] * 28124
final_sum = 0

for i in range(1,28124):	
	abundant_list[i] = is_abundant(i)					# Makes an array marking abundant or not.  Does not need to be populated past i
	count = 1
	for q in range(1,i/2+1):
		if abundant_list[q] + abundant_list[i-q] == 2:			# If two #s are marked in array as 1, they are both abundant
			count = 0
			break
	if count == 1:
		final_sum += i
		
print final_sum	
	
		

