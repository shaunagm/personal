# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 	=	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.



# Find recurring cycle - won't this run into irrational number issues?
def find_recur(number):
	# How can you do num to string of a float?  Or, how can you analyze without turning it into a string?

current_longest = 0
current_longest_length = 0

for i in (1,1000):	# iterate through the first 1000 #s
	result,cycle_length = find_recur(1/i)
	if cycle_length > current_longest_length:
		current_longest = result
	
	
