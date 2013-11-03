# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import os
filename = '../functions.py'
if os.path.exists(filename): 
        execfile(filename)

sum = 0
sieve = create_sieve(2000000)

for z in range(2,len(sieve)):			# python is zero-indexed
	if (sieve[z] == 0):
		sum += z

print sum


# Notes

# Started with a modified version from problem 7, but it's wildly inefficient at this scale.  Luckily this problem was solved a few
# millenia ago.  Thanks, eratosthenes (and wikipedia!)

# Rewritten to use function.py (view commit 31933032c96140f4093014d1f9c1d55da0442ea9 to see original version)
