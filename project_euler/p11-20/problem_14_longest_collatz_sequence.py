# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

mostSteps = 0
mostStepsNum = 0

for startNum in range(999999,1,-1):
	tempNum = startNum 
	steps = 0
	while (tempNum != 1):
		if (tempNum%2 == 0):
			tempNum = tempNum/2
		else:
			tempNum = (tempNum * 3) + 1
		steps += 1
	if (steps > mostSteps):
		mostSteps = steps
		mostStepsNum = startNum

print "Number: ", mostStepsNum, " number of steps: ", mostSteps

# Notes:

## This seems pretty hacky, but it finishes in < 60 seconds, so I guess I'll move on.  Putting it in the readme, though. 
	

