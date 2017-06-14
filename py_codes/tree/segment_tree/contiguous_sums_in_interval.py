#!/usr/bin/env python

MAX_INT = 1 << 64

class SegmentTree():
	def __init__(self, min_sum, max_sum):
		self._left_bound = min_sum
		self._right_bound = max_sum
		self._left = None
		self._right = None
		self._range_count = 0

	def addNode(self, x):
		if self._left_bound <= x and self._right_bound >= x:
			self._range_count += 1

			if self._left_bound == x and self._right_bound == x:
				return

			mid = (self._left_bound + self._right_bound) / 2

			if not self._left:
				self._left = SegmentTree(self._left_bound, mid)
				self._right = SegmentTree(mid + 1, self._right_bound)

			if x <= mid:
				self._left.addNode(x)
			else:
				self._right.addNode(x)


	def queryRange(self, l, r):
		if self._left_bound >= l and self._right_bound <= r:
			return self._range_count

		count = 0
		mid = (self._left_bound + self._right_bound) / 2
		
		if self._left:
			if l <= mid:
				if r > mid:
					count += self._left.queryRange(l, mid)
				else:
					count += self._left.queryRange(l, r)

			if r > mid:
				if l <= mid:
					count += self._right.queryRange(mid + 1, r)
				else:
					count += self._right.queryRange(l, r)

		return count


def getMinMaxSum(arr):
	cur_sum = 0
	min_sum, max_sum = MAX_INT, -MAX_INT
	for a in arr:
		cur_sum += a
		if cur_sum > max_sum:
			max_sum = cur_sum
		if cur_sum < min_sum:
			min_sum = cur_sum
	return min_sum, max_sum

def solveOptimal(arr, low, hi):
	if not arr:
		return 0

	min_sum, max_sum = getMinMaxSum(arr)
	segment_tree = SegmentTree(min_sum, max_sum)

	range_count, cur_sum = 0, 0
	for a in arr:
		cur_sum += a
		if cur_sum >= low and cur_sum <= hi:
			range_count += 1
		range_count += segment_tree.queryRange(cur_sum - hi, cur_sum - low)		 
		segment_tree.addNode(cur_sum)

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
		[[25, 2, -8, -7, -9, 25, 28, 12, 9, -6], 10, 20],
		[[25, 2, -8, -7, -9, 25, 28, 12, 9, -6], -24, 77],
		[[-4, 8, 0, 0, -4, 8], -4, 8]
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
