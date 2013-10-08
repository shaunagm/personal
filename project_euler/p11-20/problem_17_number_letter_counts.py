# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def get_standard(number):
	if (number == 0):
		return 0
	if (number in [1,2,6]):
		return 3
	if (number in [4,5,9]):
		return 4
	if (number in [3,7,8]):
		return 5

def get_teens(number):
	if (number == 10):	
		return 3
	if (number in [11,12]):
		return 6
	if (number in [15,16]):
		return 7
	if (number in [13,14,18,19]):
		return 8
	if (number == 17):
		return 9

def get_powers_of_ten(number):
	if (number in [4,5,6]):  # for forty, fifty, sixty
		return 5
	if (number in [2,3,8,9]):
		return 6
	if (number == 7):
		return 7

letterCount = 0

for x in range(1,1001):
	x = str(x)
	if (len(x) == 1) or (int(x[len(x)-2:]) < 10):  # if x is 1 digit long, or if the int version of the last two digits (eg 04) is under 10
		letterCount += get_standard(int(x[len(x)-1]))
	if (len(x) >= 2):
		if (int(x[len(x)-2]) == 1):
			letterCount += get_teens(int(x[len(x)-2:]))  	
		if (int(x[len(x)-2]) > 1):
			letterCount += get_powers_of_ten(int(x[len(x)-2]))
			letterCount += get_standard(int(x[len(x)-1]))
	if (len(x) == 3):
		letterCount += (get_standard(int(x[0])) + 7)  # 7 == "hundred"
		if (x[1:] != "00"):
			letterCount += 3  # 3 == "and"
print letterCount + 11   # 11 == "one thousand"

# Notes:

# The main function could probably be more elegant.  Which I feel like was the goal, as going to 1000 hardly taxes the processer.
# So maybe come back and make it more elegant?
