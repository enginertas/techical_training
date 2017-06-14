#!/usr/bin/env python

class Node():
	def __init__(self):
		self.key = None
		self.left = None
		self.right = None


def is_balanced_binary_helper(root):
	if not root:
		return -1

	left_h = is_balanced_binary_helper(root.left)
	right_h = is_balanced_binary_helper(root.right)
	if left_h == None or right_h == None or (abs(left_h - right_h) > 1):
		return None

	return max(left_h, right_h) + 1


def is_balanced_binary(root):
	return is_balanced_binary_helper(root) != None



'''
	Test codes are below
'''
def generate_binary_tree(arr):
	if not arr:
		return None

	n = len(arr)

	nodes = []
	for i in xrange(n + 1):
		nodes.append(Node())

	for i in xrange(n):
		if arr[i][0] != -1:
			nodes[i + 1].left = nodes[arr[i][0]]
		if arr[i][1] != -1:
			nodes[i + 1].right = nodes[arr[i][1]]

	return nodes[1]


if __name__ == "__main__":
	tests = [
		(None, True),
		([], True),
		([[-1, -1]], True),
		([[2, -1], [-1, -1]], True),
		([[-1, 2], [-1, -1]], True),
		([[2, 3], [-1, -1], [-1, -1]], True),
		([[2, -1], [3, -1], [-1, -1]], False),
		([[2, -1], [-1, 3], [-1, -1]], False),
		([[-1, 2], [-1, 3], [-1, -1]], False),
		([[2, -1], [3, 4], [-1, -1], [-1, -1]], False),
		([[2, 3], [4, 5], [-1, -1], [6, -1], [-1, -1], [-1, -1]], False),
		([[2, 3], [4, 5], [-1, 7], [-1, -1], [-1, 6], [-1, -1], [-1, -1]], True)
	]
	
	for i in xrange(len(tests)):
		root = generate_binary_tree(tests[i][0])
		result = is_balanced_binary(root)
		test_stat = "FAIL"
		if result == tests[i][1]:
			test_stat = "ok"
		print "Case", i + 1, ":", result, "--------", test_stat


