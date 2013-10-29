# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
### SEE SCREENSHOT ###
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:
### SEE SCREENSHOT ###
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge 
# with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
import time

triangle = [
	[75],
	[95, 64],
	[17, 47, 82],
	[18, 35, 87, 10],
	[20, 4, 82, 47, 65],
	[19, 1, 23, 75, 3, 34],
	[88, 2, 77, 73, 7, 63, 67],
	[99, 65, 4, 28, 6, 16, 70, 92],
	[41, 41, 26, 56, 83, 40, 80, 70, 33],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


# for each row, gets the maximum possible you could be off by
def list_of_diffs():
	diff_list = []
	for i in range(0,len(triangle)):
		diff_list.append(max(triangle[i]) - min(triangle[i]))
	return diff_list

# gets highest possible sum you get
def max_sum():
	max_sum = 0
	for i in range(0,len(triangle)):
		max_sum += max(triangle[i])

# Goes through tree getting highest of remainder
def get_child(row,col,sum):
	if triangle[row+1][col] > triangle[row+1][col + 1]:
		sum += triangle[row+1][col]
	else:
		sum += triangle[row+1][col+1]
		col += 1
	if row+1 == 14:
		return sum
	else:
		return get_child(row+1,col,sum)


max_sum = max_sum()
list = list_of_diffs()

while something = something:

	best_sum = get_child(0,0,75)

sum = get_child(0,0,75)




print sum


	



# Okay, what do we know about the correct solution?

# We know its bounds - we know a number it can't be lower than and a number it can't be higher than.
# We know that at the last level we simply pick the highest of the two it can reach.
# We know that it starts with 75.
# We know that it's the sum of 15 numbers.
# We don't know 14 of the numbers.

# Try recursion:
# For each item, if it is the last line, end, if it is not, choose 
