#!/usr/bin/env python

MOD = 10**9 + 7

def matrixMultiply2x1(matrix1, matrix2):
	result_matrix = [[], []]
	result_matrix[0].append((matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]) % MOD)
	result_matrix[1].append((matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]) % MOD)
	return result_matrix

def matrixMultiply2x2(matrix1, matrix2):
	result_matrix = [[], []]
	result_matrix[0].append((matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]) % MOD)
	result_matrix[0].append((matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]) % MOD)
	result_matrix[1].append((matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]) % MOD)
	result_matrix[1].append((matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]) % MOD)
	return result_matrix

'''
	* The solution is based on matrix exponentiation of 
		f(2n) = 4f(2n - 2) - f(2n - 4) recurrence relation

	* It is an log(n) approach instead of standard dynamic program approach with O(n)
'''
def solve(n):
	if n < 0 or n & 1 == 1:
		return 0

	if n == 0:
		return 1

	matrix = [[4, -1], [1, 0]]
	result = [[1, 0], [0, 1]]
	f1_f0_matrix = [[3], [1]]
	
	n = n / 2 - 1
	while n > 0:
		if n & 1 == 1:
			result = matrixMultiply2x2(matrix, result)
		n >>= 1
		matrix = matrixMultiply2x2(matrix, matrix)
	result = matrixMultiply2x1(result, f1_f0_matrix)

	return result[0][0]


if __name__ == "__main__":
	tests = [-2, -1, 0, 1, 3, 5, 7, 111, 2, 4, 6, 8, 10, 12, 30, 60, 100, 1000, 10**6, 10**7, 10**8, 10**9]

	test_i = 1
	for t in tests:
		print "---------------------- Test %d ----------------------" %test_i
		result = solve(t)
		print "Input:", t, "Output:", result
		test_i += 1