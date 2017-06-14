#!/usr/bin/env python

import bisect 

class BITree:
	def __init__(self, n):
		self._len = n
		self._tree = [0] * (self._len  + 1)

	def count(self, x):
	    count = 0
	    while x:
	        count += self._tree[x]
	        x -= (x & -x)
	    return count

	def add(self, x):
	    while x <= self._len:
	        self._tree[x] += 1
	        x += (x & -x)

def solveOptimal(arr, low, hi):
	if not arr:
		return 0

	# Create a sum array and create a sorted copy
	sum_arr = [arr[0]]
	for i in xrange(1, len(arr)):
	    sum_arr.append(sum_arr[-1] + arr[i])
	sorted_sum_arr = sorted(sum_arr)

	# Initialize binary index tree
	bitree = BITree(len(sum_arr))

	range_count = 0
	for cur_sum in sum_arr:
		if cur_sum >= low and cur_sum <= hi:
			range_count += 1
		range_count += bitree.count(bisect.bisect_right(sorted_sum_arr, cur_sum - low)) 
		range_count -= bitree.count(bisect.bisect_left(sorted_sum_arr, cur_sum - hi))
		bitree.add(bisect.bisect_left(sorted_sum_arr, cur_sum) + 1)
	
	return range_count

def solveBruteForce(arr, low, hi):
	if not arr:
		return 0

	range_count = 0
	for i in xrange(len(arr)):
		count = 0 
		for j in xrange(i, len(arr)):
			count += arr[j]
			if count >= low and count <= hi:
				range_count += 1
	
	return range_count


if __name__ == "__main__":
	tests = [
		[None, 1, 1],
		[[], 5, 66],
		[[8], 5, 66],
		[[-3], 5, 66],
		[[8], 5, 5],
		[[8], 8, 8],
		[[-3], -7, -7],
		[[-3], -3, -3],
		[[-4], -4, 3],
		[[8], 8, 12],
		[[-4, 8], -4, 4],
		[[-4, 8], -4, 8],
		[[-4, 8, 0, 0, -4, 8], -4, 8],
		[[25, 2, -8, -7, -9, 25, 28, 12, 9, -6], 10, 20],
		[[25, 2, -8, -7, -9, 25, 28, 12, 9, -6], -24, 77]
	]

	
	test_i = 1
	for arr, low, hi in tests:
		print "---------------- Test %s ------------------" % test_i
		print "Arr:", arr, "low:", low, "hi:", hi
		optimal = solveOptimal(arr, low, hi)
		bruteforce = solveBruteForce(arr, low, hi)
		print "Optimal:", optimal, "Brute Force:", bruteforce
		assert optimal == bruteforce
		print "OK"
		test_i += 1
