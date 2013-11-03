# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import os
filename = '../functions.py'
if os.path.exists(filename):
        execfile(filename)

def is_prime(number,sieve):
	if (sieve[number] == 0):
		return 1
	return 0

def rotate_digits(number,digits_to_rotate):
	NumList = list(str(number))	
	for i in range(0,digits_to_rotate):
		NumList.append(NumList.pop(0))	# Takes first digit and rotates to end
	return int(''.join(NumList))

sieve = create_sieve(1000000)
count = 0

for i in range(2,1000000):
	isCircPrime = 1
	for j in range(0,len(str(i))):
		if is_prime(rotate_digits(i,j),sieve) == 0:	# If the rotated number is not prime, end for loop
			isCircPrime = 0
			break
	if isCircPrime == 1:
		count += 1

print count

# Note:
# Re-write this using generators?				



