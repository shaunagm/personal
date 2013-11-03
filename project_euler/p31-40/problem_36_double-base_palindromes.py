# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(number):		# parameter number is actually a string
	for i in range(0,len(number)):
		if number[i] != number[::-1][i]:	# indexes into the number forwards and the number reversed
			return 0
	return 1	

sum = 0

for i in range(0,1000000):
	if is_palindrome(str(i)):				# Check base 10 first because presumably there are fewer palindromic base 10 #s
		if is_palindrome('{:b}'.format(i)):		# Thanks StackOverflow http://stackoverflow.com/questions/2434806/how-i-can-convert-integer-in-to-binary-in-python
			sum += i

print sum
