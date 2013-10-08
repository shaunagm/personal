# Starting in the top left corner of a 22 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom 
# right corner.

### SEE SCREENSHOT ###

# How many such routes are there through a 2020 grid?

def get_factorial(number):		# could use math.factorial(), but trying not to import things
	product = 1
	for p in range(1,number+1):
		product = product * p
	return product

height = 20
width = 20
print get_factorial(height+width)/(get_factorial(height) * get_factorial(width)) 


# Notes

# So we can conceptualize this as an order of steps, where you need to go X steps down and Y steps right.
# Each down step is interchangeable with other down steps, and right interchangeable with right.
# Looked up how to do permutation with duplicates here: http://math.stackexchange.com/questions/15884/permutation-with-duplicates
