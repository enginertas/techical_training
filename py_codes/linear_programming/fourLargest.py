#!/usr/bin/python

import sys

def giveFourLargest(nums):
    le1 = - sys.maxint - 1
    le2 = le1
    le3 = le1
    le4 = le1

    for num in nums:
	if num > le4:
		le4 = num

    	if num > le3:
	    	le4 = le3
	    	le3 = num

    	if num > le2:
	    	le3 = le2
	    	le2 = num

    	if num > le1:
	    	le2 = le1
	    	le1 = num

    return (le1, le2, le3, le4)

if __name__ == "__main__":
	integers = []
	integers.append([])
	integers.append([1])
	integers.append([-4, 1])
	integers.append([-7, 2, -3])
	integers.append([8, 0, 4, 7])
	integers.append([1, 5, 7, -2, 4, 20])
	integers.append([1, 5, 7, -2, 4, 20, 2, 12, 21, 24])
	integers.append([1, 5, 7, -2, 4, 20, 21, 21, 24, 24])
	integers.append([1, 5, 7, -2, 4, 21, 21, 21, 24, 24])
	integers.append([1, 5, 7, -2, 4, 24, 24, 24, 24, 24])

	for int_list in integers:
		print "--------------------------"
		print "Integers:"
		print int_list
		print "Four Largest Integers: "
		print giveFourLargest(int_list)
