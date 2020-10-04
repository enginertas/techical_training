def find_nonnegative_subarray_sum_to_k(arr, k):
	start, end = 0, 0
	cur_sum = 0

	while end < len(arr):
		cur_sum += arr[end]

		while cur_sum > k:
			cur_sum -= arr[start]
			start += 1

		# Initial check is required for (k = 0) case.
		if start <= end and cur_sum == k:
			return True
		else:
			end += 1

	return False


if __name__ == '__main__':
	tests = [
		# k = 0 cases
		(([], 0), False),
		(([4], 0), False),
		(([0], 0), True),
		(([4, 0, 4], 0), True),
		(([1, 3], 0), False),

		# k != 0 and empty case
		(([], 3), False),

		# Tests for subarray sums starting from index 0
		(([1, 8, 3, 14, 17, 75], 1), True),
		(([1, 8, 3, 14, 17, 75], 9), True),
		(([1, 8, 3, 14, 17, 75], 12), True),
		(([1, 8, 3, 14, 17, 75], 26), True),
		(([1, 8, 3, 14, 17, 75], 43), True),
		(([1, 8, 3, 14, 17, 75], 118), True),

		# Tests for single element equals to k
		(([1, 8, 3, 14, 17, 75], 8), True),
		(([1, 8, 3, 14, 17, 75], 3), True),
		(([1, 8, 3, 14, 17, 75], 14), True),
		(([1, 8, 3, 14, 17, 75], 17), True),
		(([1, 8, 3, 14, 17, 75], 75), True),

		# Generic cases
		(([1, 8, 3, 14, 17, 75], 9), True),
		(([1, 8, 3, 14, 17, 75], 11), True),
		(([1, 8, 3, 14, 17, 75], 13), False),
		(([1, 8, 3, 14, 17, 75], 117), True),
		(([1, 8, 3, 14, 17, 75], 116), False),
		(([1, 8, 3, 14, 17, 75], 41), False),
		(([1, 8, 3, 14, 17, 75], 42), True),
		(([1, 8, 3, 14, 17, 75], 92), True),
		(([1, 8, 3, 14, 17, 75], 91), False),
		(([1, 8, 3, 14, 17, 75], 31), True),
		(([1, 8, 3, 14, 17, 75], 34), True),
		(([1, 8, 3, 14, 17, 75], 33), False),
		(([15, 2, 4, 8, 9, 5, 10, 22], 23), True),]

	for (arr, k), result in tests:
		print ('----------------------')
		print (arr, k)
		assert result == find_nonnegative_subarray_sum_to_k(arr, k), '%s, %s' % (arr, k)
		print ('OK')

	print('All tests are passed')
