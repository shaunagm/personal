#  This document contains a number of basic functions created for past problems.  If the same function needs 
#  to be used again, I place it here.  (Implemented starting at problem 30, so may not be true of lower #s.)

def create_sieve(sieveLength):
	sieve = [0] * sieveLength			# Creates array of 0 the length of the sieve
	for x in range(2,sieveLength):			# For each item in the array
		if (sieve[x] == 0):			# If the item is prime
			for y in range(x*2,len(sieve),x):	# Go through sieve and label all multiples of the number...
				sieve[y] = 1			# as 1, which means not prime	
	return sieve

