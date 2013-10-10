# The Fibonacci sequence is defined by the recurrence relation:
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144

# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

import copy
import time

# simple solution
n_minus_2 = 1
n_minus_1 = 1
n = 2
list = [1,1]

while len(str(n)) < 1000:
	list.append(n)
	old_n = copy.copy(n)
	n_minus_2 = copy.copy(n_minus_1)
	n_minus_1 = copy.copy(old_n)	
	n = n_minus_1 + n_minus_2

list.append(n)
print len(list)
