# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

number = 2 ** 1000
sum = 0

for digit in str(number):
	sum += int(digit)

print sum	

# Notes:

# I wonder if some of these are actually hard in other languages.
