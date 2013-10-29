# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and 
# product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def is_pandigital(multiplicand,multiplier,product):
	charList = list(str(multiplicand) + str(multiplier) + str(product))
	if len(charList) == len(set(charList)):			# Set returns only unique elements.
		return 1
	return 0

	


print "unique: ", is_pandigital(12,345,678)
print "not unique: ", is_pandigital(12,145,678)


## Notes:

## The upper limit can be determined by the size limits -> there can't be more than 9 digits total between the three numbers.

