## A set of functions for use in analyze.py

# Iterate through data and delete duplicates.
def removeDupes(data):
	print "Removing duplicates."
	newData = []
	for i in range(0,len(data)):
		if data[i] not in newData:
			newData.append(data[i])
		else:
			print "Deleting duplicate data:\n"
			print data[i]
	return newData

# Iterate through and delete dicts with missing data.
def removeBlanks(data):
	print "Removing items with missing data."
	newData = []
	for i in range(0,len(data)):
		delete = 0
		for k,v in data[i].iteritems():		# Iterate through each item in each dict
			if v == '':
				delete = 1
		if delete == 0:
			newData.append(data[i])	
		else:
			print "Deleting item with missing data:\n"
			print data[i]

	return newData

# Provide basic summary statistics
# To do - deal with rounding errors in calculations
def summarize(choice,data):
	print "Minimum ",choice,": ", min(item[choice] for item in data)
	print "Maximum ",choice,": ", max(item[choice] for item in data)
	sum = 0
	count = 0
	for dict in data:
		sum += float(dict[choice])
		count += 1
	mean = sum/count
	print "Mean ",choice,": ",mean		
	# Get standard deviation by calculating the sum of the squared differences from the mean, then take square root
	sum_of_squares = 0
	for dict in data:
		sum_of_squares += ((mean - float(dict[choice])) * (mean - float(dict[choice])))
	sd = pow(sum_of_squares/(count-1),.5)		# Get square root by raising to power of 1/2.
	print "Sample (not population) standard deviation of ",choice,": ",sd
	# Calculate outliers
	print "Assuming your data is normally distributed, the following items are more than two standard deviations from the mean, and may therefore be considered outliers:\n"
	for dict in data:
		deviation = abs(mean - float(dict[choice]))
		if deviation > (sd * 2):
			print dict		
