# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 20
flag = 0

while (1):
	for x in range (1,21):
		if (i%x != 0):
			flag = 1
			break	
	if (flag == 0):
		print i
		break
	flag = 0
	i += 20

# Notes:

# Takes about 10 seconds to generate answer... maybe an easier way?  
