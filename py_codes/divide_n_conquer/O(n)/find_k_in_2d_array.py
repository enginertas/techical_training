#!/usr/bin/env python

def find_k_in_2d_array(arr, m, n, k):
	if not arr:
		return None

	row, col = 0, n - 1
	while row < m and col >= 0:
		if arr[row][col] == k:
			return (row, col)
		elif arr[row][col] < k:
			row += 1
		else:
			col -= 1

	return None


if __name__ == "__main__":
	tests = [
		None,
		[],
		[[1]],
		[[1, 2], [3, 4]],
		[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
		[[1, 2, 7], [3, 5, 8], [4, 6, 9]],
		[[1, 3, 6, 8, 9, 10], [2, 4, 7, 11, 12, 15]],
		[
			[-6, 2, 3, 4, 5, 6, 7, 8],
			[-5, 3, 5, 7, 9, 11, 13, 15],
			[-4, 4, 7, 10, 13, 16, 19, 22],
			[-3, 5, 9, 13, 17, 21, 25, 29],
			[-2, 6, 11, 16, 21, 26, 31, 36],
			[-1, 7, 13, 20, 27, 34, 41, 48],
			[1, 8, 15, 22, 29, 36, 43, 50],
		]
	]

	for arr in tests:
		print "---------------------------"
		print "Set:", arr

		r, m, n = 3, 1, 1
		if arr:
			m, n = len(arr), len(arr[0])
			r = m * n + 3
		
		for i in xrange(1, r):
			print "index of", i, "->", find_k_in_2d_array(arr, m, n, i)