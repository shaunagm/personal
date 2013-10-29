# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def get_proper_divisors(number):
    	i = 2
	small_divisors = [1]
        large_divisors = [number]
        while (i < large_divisors[len(large_divisors)-1]):   # Check that all divisors are less than large divisors, large_divisors $
                if (number%i == 0):
                        small_divisors.append(i)
                        large_divisors.append(number/i)
		i += 1
	return sum(small_divisors + large_divisors) - number	# ugly, but we need to populate number above to make the while loop condition work

sum_array = [0]
for i in range (1,10001):					# Create sum array where index = # and value = sum of proper divisors
	sum_array.append(get_proper_divisors(i))

amicable_numbers = []
for i in range(1,10001):				# Check if amicable #s
	j = sum_array[i]
	if ((j <= len(sum_array)) and (i == sum_array[j]) and (sum_array[i] != sum_array[j])):
		if i not in amicable_numbers:
			amicable_numbers.append(i)
			amicable_numbers.append(j)

print sum(amicable_numbers)
