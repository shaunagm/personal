# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

prime_list = [2]
i = 3

while (len(prime_list) < 10001):
	flag = 0
	for x in prime_list:
		if (i%x == 0):
			flag = 1
	if (flag == 0):
		prime_list.append(i)
	i+= 2 		

print prime_list[10000]

# Notes

# Could maybe be more efficient?  Takes around 20 seconds to produce the result.
# Also, this is neat: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
