# Euler discovered the remarkable quadratic formula:
# n2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 412 + 41 + 41 is clearly divisible by 41.
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# Sieve of Eratosthenes from problem 10 
sieve = [0] * 2000000
for x in range(2,len(sieve)):
        if (sieve[x] == 0):
                y = x
                for y in range(x*2,len(sieve),x):
                        sieve[y] = 1

# Iterates through n, counting the number which are primes and returning the total
def test_a_b(a,b):
	is_composite = 0
	count = 0
	n = 0
	while (is_composite == 0):
		result = (n * n) + (a * n) + b
		is_composite = sieve[result]		# Checks the seive under that number
		if is_composite == 0:
			count += 1
		n += 1
	return count


current_max = [0,0,0]
for a in range(-999,1000):
	for b in range(-999,1000):
		count = test_a_b(a,b)
		if count > current_max[0]:
			current_max = [count,a,b]

print current_max[1] * current_max[2]
