# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by 
# sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its 
# alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
# name in the list. So, COLIN would obtain a score of 938  53 = 49714.
# What is the total of all the name scores in the file?

import csv

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
name_list = []

# Opens file & reads in data, making & sorting a list
namefile = open('names.txt', 'r')
namestring = namefile.read()
name_list = namestring.split(",")
name_list.sort()

total_sum = 0
name_sum = 0
for name_index in range(0,len(name_list)):						# For each name in the list
	char_sum = 0
	name = name_list[name_index].strip('"')						# Formatting!
	for char in range(0,len(name)):							# For each char in each name
		char_sum += alphabet.index(name[char]) + 1				# Find the index in alphabet + 1 'cause python 0-indexes
	name_sum = char_sum * (name_index + 1)
	total_sum += name_sum

print total_sum
		
