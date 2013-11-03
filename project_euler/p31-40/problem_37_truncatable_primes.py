# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 
# 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import os
filename = '../functions.py'
if os.path.exists(filename):
        execfile(filename)

def is_prime(number):
        if (sieve[number] == 0):
                return 1
        return 0

def truncate_and_test(number):					# yo this parameter is string
	if not is_prime(int(number)):
		return 0
	for i in range(1,len(number)):
		if not (is_prime(int(number[i::])) and is_prime(int(number[:-i]))):	# truncates from left & right
			return 0
	return 1			

sieve = create_sieve(1000000)
sum = 0
count = 0
currentNumber = 9

while count < 11:
	currentNumber += 1
	if truncate_and_test(str(currentNumber)):
		sum += currentNumber
		count += 1
print sum
