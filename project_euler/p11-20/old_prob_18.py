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


# Gets the path with the highest sum 
def get_ideal_path():
	path = []
	for i in range(0,len(triangle)):
		path.append(max(triangle[i]))
	return path

# Gets the next highest path which has not already been tested
def get_next_best(past_path):
	print "past before", past_path
	alt_path = []
	for i in range(0,len(triangle)):	# Creates an alt list containing the next highest # for each row
		alt_path.append(compare_nums(past_path[i], triangle[i]))
	print "alt_path",alt_path

	diff_path = []
	for j in range(0,len(triangle)):	# Creates a list of differences between past and alt path
		diff_path.append(past_path[j] - alt_path[j])
	print diff_path



	while min(diff_path) == 0:		# If one diff is 0 - that is, two items are identical - overwrites with 100 so not selected
		print diff_path
		print min(diff_path)
		diff_path[diff_path.index(min(diff_path))] = 100
		print "after ",diff_path	


	print past_path[diff_path.index(min(diff_path))]
	print alt_path[diff_path.index(min(diff_path))]

	past_path[diff_path.index(min(diff_path))] = alt_path[diff_path.index(min(diff_path))]  # makes smallest possible change
	print "past after", past_path

	return past_path

# Compares an int to a list and gets the item on the list that is next highest (DOESN'T DEAL WITH IDENTICAL INTS IN SAME LIST)
def compare_nums(current_high,triangle_row):
	copy_row = triangle_row[:]			# make a copy so you're not changing triangle (be careful to use [:] to actually make new values!)
	while (len(copy_row) > 0):
		max_num = max(copy_row)
		if max_num >= current_high:
			copy_row.remove(max_num)
		if max_num < current_high:
			return max_num
	return current_high

# Tests whether this path is a legitimate path
def test_path(current_path):
	index_list = []
	for i in range(0,len(triangle)):	# Makes list of indexes.
		index_list.append(triangle[i].index(current_path[i]))	# Finds the index of the path in triangle and adds it to a list.
	last_index = 1
	for j in range(0,len(index_list)+1):
		if last_index - index_list[j] > 1:
			return 0
		last_index = index_list[j]
	return 1

## Main program
current_path = get_ideal_path()
found = test_path(current_path)

while found == 0:
	current_path = get_next_best(current_path)
	found = test_path(current_path)
	time.sleep(.33)

print current_path


## NOTES:

# step 1: get the highest # in each row
# step 2: test to see if one can step between all of those
# step 3: if you can't, get the next highest ideal path
# step 4: test to see if you can step through it

# man this would be so much easier in R

# god damn copying in python
