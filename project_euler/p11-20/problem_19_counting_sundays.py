# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.  All the rest have thirty-one, Saving February alone, Which has twenty-eight.
# (And on leap years, twenty-nine.)
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def is_sunday(date):
	# Day 0 is a Monday, so date%7 == 0 means it's a Monday, date%7 == 1 means it's a Tuesday, etc.
	if (date%7 == 6):  # if it's a Sunday
		return 1
	return 0

def days_in_month(month,year):
	# Month 0 is January, so month%12 == 0 means it's January.
	if (month%12 in [0,2,4,6,7,9,11]):  # if Jan, Mar, May, Jul, Aug, Sept, Oct, Dec
		return 31
	if (month%12 in [3,5,8,10]):   # if Apr, Jun, Sep, Nov
		return 30
	if (month%12 == 1):
		leapYear = is_leap_year(year)
		if (leapYear):
			return 29
		else:
			return 28

def is_leap_year(year):
	if (year%4 == 0):   
		if (year%100 == 0):  
			if (year%400 == 0):
				return 1	# if year is divisible by 4, 100 and 400 (such as 1600, 2000) it's a leap year
			return 0		# if a year is divisible by 4 and 100 but not 400 (such as 1700, 1800) it's not a leap year
		return 1			# if a year is divisible by 4 only (such as 1786, 1780) it's a leap year

def is_counted(day,month,year,count):
	if (count == 0):
		if (year >= 1901):			# change year here to change the start year
			if (month%12 >= 0):		# change month here to change the start month
				return 1
		return 0
	if (count == 1):
		if (year > 2000) or (year == 2000 and month%12 > 11):	# change year and month here to change the start/end year
			return 2
		return 1

# Starts iterating from Mon, Jan 1st 1900
day = 0
month = 0
year = 1900

count = 0
firstMonthSundays = 0

while (count < 2):
	if is_sunday(day):
		count = is_counted(day,month,year,count)
		if (count == 1):
			firstMonthSundays += 1
	day += days_in_month(month,year)
	month += 1
	if(month%12 == 0):
		year += 1

print firstMonthSundays

# Notes:

# I dislike that you can't input, say, June 15th, 1920 (as opposed to June 1st 1920, which you can) as your "start counting" date or "end
# counting" date.  
# Or that it's designed to work forward from 1/1/1900 generally.  It goes on the list to come back and fix, for flexibility as opposed to 
# efficiency reasons.
