# n! means n x (n - 1)  ...  3 x 2 x 1
# For example, 10! = 10 x 9  ...  3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def product_of_factorial(number):
	product = 1
	for i in range(1,number):
		product = product * i
	return product

def sum_of_digits(number):
	sum = 0
	number = str(number)
	for i in range(0,len(number)):
		sum += int(number[i])
	return sum

print sum_of_digits(product_of_factorial(100))
