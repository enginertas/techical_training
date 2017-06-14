#!/usr/bin/env python

'''
Example Input:
4, "IDI"

Desired Output:
[1, 4, 2]

'''

def solve(n, s):
	if n <= 0:
		return []

	arr = []
	min_el, max_el = 1, n
	for move in s:
		if move == 'I':
			arr.append(min_el)
			min_el += 1
		else:
			arr.append(max_el)
			max_el -= 1

	arr.append(min_el)
	return arr


if __name__ == "__main__":
	tests = [
		[-1, None, []],
		[0, None, []],
		[1, "", [1]],
		[2, "I", [1, 2]],
		[2, "D", [2, 1]],
		[3, "II", [1, 2, 3]],
		[3, "ID", [1, 3, 2]],
		[3, "DI", [3, 1, 2]],
		[3, "DD", [3, 2, 1]],
		[4, "III", [1, 2, 3, 4]],
		[4, "IID", [1, 2, 4, 3]],
		[4, "IDI", [1, 4, 2, 3]],
		[4, "IDD", [1, 4, 3, 2]],
		[4, "DII", [4, 1, 2, 3]],
		[4, "DID", [4, 1, 3, 2]],
		[4, "DDI", [4, 3, 1, 2]],
		[4, "DDD", [4, 3, 2, 1]]
	]

	print "** Running Tests **"

	test_i = 1
	for n, s, arr in tests:
		print "---------------- Test %d ----------------" %test_i
		print "Desired Response:", arr
		result = solve(n, s)
		print "Actual Response:", result
		assert arr == result
		test_i += 1

	print "** All tests are OK **"