#!/usr/bin/env python

def find_index_of_max(arr):
	if (not arr) or len(arr) < 3:
		return -1

	l, r = 1, len(arr) - 2
	while l <= r:
		mid = (l + r) / 2
		if arr[mid] > arr[mid - 1]:
			if arr[mid] > arr[mid + 1]:
				return mid
			else:
				l = mid + 1
		else:
			r = mid - 1

	return -1


if __name__ == "__main__":
	tests = [None, [], [1], [2], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 1], [2, 1], 
				[3, 2, 1], [8, 4], [1, 8, 4], [4, 8, 4], [9, 14, 17, 8],
				[1, 2, 5, 9, 16, 17, 4, 3]]

	for t in tests:
		i = find_index_of_max(t)
		val = None
		if i != -1: 
			val = t[i]
		print t, i, val
