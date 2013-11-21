# This program loads, cleans, and does basic analysis of supplied data files.

import os
import supplementary as sup

#########
# Loading
# To do - handle other kinds of files
file = raw_input("Please specify a csv file to analyze: ")
f = open(file,"r")
headers = f.readline().strip("\n").split(",") # Saves header text separately
data = [] # initialize list to hold a dict for each line of data
for line in f:
	listLine = line.strip("\n").split(",")	# Strip must come before split since split returns list, not string
	dict = {}
	for i in range(0,len(listLine)):
		dict[headers[i]] = listLine[i]		# Create dict using header rows as keys
	data.append(dict)
f.close()


##########
# Cleaning
clean = ''
while clean != 'c':
	clean = raw_input("Data processing options: [d] check duplicate lines, [e] check blank lines, or [c] continue on without further processing.  Please choose:  ").lower()
	if clean == 'd':
		data = sup.removeDupes(data)
	if clean == 'e':
		data = sup.removeBlanks(data)

################
# Basic Analysis
print data

print "Select a variable to generate summary statistics (min, max, mean, standard deviation and outliers) for that variable, or type 'c' to continue."
for item in headers:
	print item
choice = ''
while choice != 'c':
	choice = raw_input("Please select a variable or type c to exit: ")
	if choice in headers:
		try:
			float(data[0][choice])
		except:
			print "One or more rows have non-numerical content for this variable, and therefore cannot be summarized."
		else:
			sup.summarize(choice,data)
	else:
		if choice == 'c':
			print "Goodbye!"
		else:
			print "The variable you entered does not match any of those listed above.  Please try again."

