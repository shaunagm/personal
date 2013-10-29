# In England the currency is made up of pound, E and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
# It is possible to make E2 in the following way:

# 1xE1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can E2 be made using any number of coins?

import time

# Breaks down a given number into its greatest possible constituents
def make_change(number):
	if number == 200:
		return [100,100]
	if number == 100:
		return [50,50]
	if number == 50:
		return [20,20,10]
	if number == 20:
		return [10,10]
	if number == 10:
		return [5,5]
	if number == 5:
		return [2,2,1]
	if number == 2:
		return [1,1]
	if number == 1:	
		return [0]
	print "Error: a non-currency number has been created somehow."
	return
	

current_number = 200
coin_array = [current_number]
count = 1

while len(coin_array) < 200:
	for i in reversed(range(0,len(coin_array))):
		time.sleep(2)
		temp_array = make_change(coin_array[i])
		print "change made? ",temp_array
		if temp_array[0] != 0:				# If the number fed in wasn't 1, replace # fed in with returned array. 
			print "count before: ",count
			count += 1
			print "count after: ",count
			coin_array.pop(i)
			for j in range(0,len(temp_array)):
				coin_array.append(temp_array[j])
			print "new array ",coin_array
			break
	
print count 							# Kinda hacky, but I want an easy while loop exit, but to still count the last change-making

#### WHY THIS ISN'T CURRENTLY WORKING

# Consider the case of 100 + 50 + 20 + 20 + 10
# The algorithm currently sees 10 first and replaces with 5 + 5
# So there's never the opportunity to try 100 + 50 + 20 + 10 + 10 + 10
# There needs to be more structure in what gets broken down how... or things need to be able to be put back together again


## What do we know?

## In each set, there will be no less than 1 and no more than 200 coins.
## 100p + 100p == 100p + 100p -- that is, order doesn't matter.
## We can tell ahead of time which things can be broken down into other things, ie
## A 2 can be broken down into to 1s
## A 5 can be broken down into two 2s and a 1
## A 10 can be broken down into two 5s
## A 20 can be broken down into two 10s, etc
