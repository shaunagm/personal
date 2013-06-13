# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

sum = 0
sieve = [0] * 2000000

# Algorithm from sieve of eratosthenes (well, a less efficient version) 
for x in range(2,len(sieve)):
	if (sieve[x] == 0):
		y = x
		for y in range(x*2,len(sieve),x):
			sieve[y] = 1

for z in range(2,len(sieve)):			# python is zero-indexed
	if (sieve[z] == 0):
		sum += z

print sum


# Notes

# Started with a modified version from problem 7, but it's wildly inefficient at this scale.  Luckily this problem was solved a few
# millenia ago.  Thanks, eratosthenes (and wikipedia!)

