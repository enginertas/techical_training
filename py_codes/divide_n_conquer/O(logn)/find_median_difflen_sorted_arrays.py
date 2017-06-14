#!/usr/bin/env python

def findMedianSingleArray(arr):
	if len(arr) & 1 == 1:
		return arr[len(arr) / 2]
	else:
		return float(arr[len(arr) / 2] + arr[len(arr) / 2 - 1]) / 2


def medianEven2(el1, el2):
	return float(el1 + el2) / 2


def medianOdd3(el1, el2, el3):
	return el1 + el2 + el3 - max(el1, el2, el3) - min(el1, el2, el3)


def medianEven4(el1, el2, el3, el4):
	total = el1 + el2 + el3 + el4 - max(el1, el2, el3, el4) - min(el1, el2, el3, el4)
	return float(total) / 2


def findMedianTwoSortedArrays(A, B):
	if (not A) and (not B):
		return None
	if not A:
		return findMedianSingleArray(B)
	if not B:
		return findMedianSingleArray(A)

	if len(A) > len(B):
		A, B = B, A

	if len(A) == 1:
		if len(B) == 1:
			return medianEven2(A[0], B[0])
		elif len(B) & 1 == 1:
			return medianEven4(A[0], B[len(B) / 2], B[len(B) / 2 - 1], B[len(B) / 2 + 1])
		else:
			return medianOdd3(A[0], B[len(B) / 2], B[len(B) / 2 - 1])

	st_A, end_A = 0, len(A) - 1
	st_B, end_B =  0, len(B) - 1
	while end_A - st_A > 1:
		mid_A = (st_A + end_A) / 2
		mid_B = (st_B + end_B) / 2
		if A[mid_A] <= B[mid_B]:
			end_B -= (mid_A - st_A)
			st_A = mid_A
		else:
			if (end_A - st_A) & 1 == 1:
				st_B += (end_A - mid_A - 1)
				end_A = mid_A + 1
			else:
				st_B += (end_A - mid_A)
				end_A = mid_A		
	
	len_B = end_B - st_B + 1
	mid_B = (st_B + end_B + 1) / 2
	if len_B == 2:
		return medianEven4(A[st_A], A[end_A], B[st_B], B[end_B])
	elif len_B & 1 == 1:
		return medianOdd3(max(A[st_A], B[mid_B - 1]), B[mid_B], min(A[end_A], B[mid_B + 1]))
	else:
		return medianEven4(max(A[st_A], B[mid_B - 2]), B[mid_B - 1], B[mid_B], min(A[end_A], B[mid_B + 1]))


if __name__ == "__main__":
	tests = [
		(None, None),
		(None, [6]),
		([6], None),
		([], []),
		([], [6]),
		([7], []),
		([7], [8]),
		([3], [6]),
		([9], [11]),
		([9], [9]),
		([1, 2, 3, 4], [1, 2, 3, 4]),
		([1, 2, 6, 8], [4, 5, 6, 7]),
		([1, 2, 6, 8], [7, 8, 9, 10]),
		([1, 2, 6, 8], [9, 9, 9, 10]),
		([6, 7, 8, 9], [1, 2, 3, 4]),
		([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]),
		([6, 7, 8, 9, 10], [1, 2, 3, 4, 5]),
		([4, 7, 8, 9, 10], [1, 2, 3, 4, 5]),
		([1, 3, 6, 8, 10, 12], [9, 10, 11, 12, 14, 18]),
		([1, 2, 3, 6, 7, 10, 12, 14, 18, 24, 27], [11, 20, 29, 30, 31, 33, 37, 44, 46, 50, 54]),
		([1, 2, 3, 6, 7, 10, 12, 14, 18, 24], [20, 29, 30, 31, 33, 37, 44, 46, 50, 54]),
		([1, 2, 3, 6, 7, 10, 12, 14, 18, 24], [25, 29, 30, 31, 33, 37, 44, 46, 50, 54]),
		([3, 6], [8]),
		([7], [8, 9, 10]),
		([9], [1, 2, 3, 4]),
		([1, 2, 3, 4, 5], [9]),
		([1], [6, 7, 10, 11]),
		([4], [1, 2, 3, 4, 5]),
		([1, 2, 3, 4, 7, 10, 11], [9]),
		([3], [1, 2, 3, 4, 8, 11]),
		([3, 5], [1, 2]),
		([3, 5], [1, 9]),
		([3, 5], [4, 8]),
		([3, 6], [8, 10, 11, 14]),
		([7, 8], [8, 9, 10]),
		([9, 10], [1, 2, 3, 4]),
		([1, 2, 3, 4, 5], [2, 9]),
		([1, 3], [6, 7, 10, 11]),
		([4, 8], [1, 2, 3, 4, 5]),
		([1, 2, 3, 4, 7, 10, 11], [9, 11]),
		([3, 14], [1, 2, 3, 4, 8, 11]),
		([3, 8, 14], [1, 2, 3, 4, 8, 11]),
		([3, 10, 11, 14], [1, 2, 3, 4, 8, 11]),
		([3, 14, 21, 24, 24], [1, 2, 3, 4, 8, 11, 13, 17, 40, 44, 46]),
		([3, 14, 21, 24, 24, 28], [1, 2, 3, 4, 8, 11, 13, 17, 40, 44, 46]),
		([3, 14, 21, 24, 24], [1, 2, 3, 4, 8, 11, 13, 17, 40, 44, 46, 49]),
		([3, 14, 21, 24, 24, 40], [1, 2, 3, 4, 8, 11, 13, 17, 40, 44, 46, 52]),
		([1, 2, 6, 7], [3, 4, 5, 8]),
		([3, 4, 5, 8], [1, 2, 6, 7])
	]

	for t in tests:
		print t[0], t[1]
		print "Median:", findMedianTwoSortedArrays(t[0], t[1])		
		print "-------------------------------"