def maximum_sum_rectangle(matrix):
	if not matrix or not matrix[0]:
		return None

	rows, cols = len(matrix), len(matrix[0])

	global_max = float('-inf')

	for left in range(cols):
		temp = [0] * rows
		for right in range(left, cols):
			local_max = float('-inf') 
			for i in range(rows):
				temp[i] += matrix[i][right]
				local_max = max(temp[i], temp[i] + local_max)
				global_max = max(local_max, global_max)

	return global_max


if __name__ == '__main__':
	tests = [
			(None, None),
			([], None),
			([[]], None),
			([[4]], 4),
			([[-3]], -3),
			([[-3, 1]], 1),
			([[3, -1]], 3),
			([[-3, -1]], -1),
			([[3, 1]], 4),
			([[-3], [1]], 1),
			([[-1], [3]], 3),
			([[3], [-1]], 3),
			([[-3], [-4]], -3),
			([[3], [4]], 7),
			([[-20, -19], [-18, -17]], -17),
			([[0, -19], [-18, -17]], 0),
			([[1, -19], [1, -17]], 2),
			([[-3, -4, -3, -2, -1, -6], 
				[-4, -5, -6, -7, -8, -9],
				[-2, 3, 5, 7, 9, -1],
				[1, 2, 3, 4, 5, -3],
				[-6, 1, 2, 1, 3, -8],
				[-7, 2, 2, 2, 2, -11],
				[-3, -2, -3, -5, -6, -14]], 53)
		
		]

	for idx, (matrix, result) in enumerate(tests):
		print ('-----------------------------------')
		print ('Test: ', idx)
		assert maximum_sum_rectangle(matrix) == result
		print ('OK')
