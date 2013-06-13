# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
	if (number == int(str(number)[::-1])):
		return 1
	return 0

def is_3_by_3(number):
	for x in range (100,999):
		if (number%x == 0): 
			if (len(str(number/x)) == 3):
				return 1
	return 0

i = 999 * 999
while (i > 0):
	if is_palindrome(i):
		if is_3_by_3(i):
			print i
			break
	i -= 1



# Notes:
# 
# I tried to come up with an algorithm to iterate down from 999 * 999 such that the next product was always smaller than the last, but I
# didn't quite figure it out, and the above works in < 1 sec so this seems like a reasonable solution.
