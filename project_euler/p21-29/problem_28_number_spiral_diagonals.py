# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#	*21* 22 23 24 *25*
#	20  *7*  8  *9* 10
#	19  6  *1*  2 11
#	18  *5*  4  *3* 12
#	*17* 16 15 14 *13*

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

layer = 1
last_count = 1
sum_of_diagonals = 1

def get_diags(list):
	sum = 0
	for i in range(1,5):
		sum += list[(len(list)/4)*i-1]
	return sum	

while layer < 501:  		 # There are 500 layers in a 1001 x 1001 square
	layer += 1
	added_numbers = range(last_count+1,last_count+(8*(layer-1))+1)	# +1 since range is (X-inclusive,Y-exclusive) 
	sum_of_diagonals += get_diags(added_numbers)
	last_count = added_numbers[len(added_numbers)-1]	# Grabs the last item of the newly added #s


print sum_of_diagonals
	

## REASONING:

# Row		Total Added	Total N		New dim		# of N before Starred N
# Row 1		n = 1		1		(1 x 1)		0
# Row 2		n = 8		9		(3 x 3)		1
# Row 3		n = 16 		25		(5 x 5)		3
# Row 4		n = 24 		49		(7 * 7)		5
# Row 5		n = 32		71		(9 * 9)		7

# Total added = 8*(row#-1)

# Pattern - each new row adds n+8 items, where n = the number of items added last time
# There are always four starred things, to figure out which is starred divide n+8 by four, evenly spaced with the last one always starred

