#!/usr/bin/env python

import sys

class Node():
	def __init__(self):
		self.key = None
		self.left = None
		self.right = None


def is_tree_bst_helper(root, lb, rb):
	if not root:
		return True

	if root.key < lb or root.key > rb:
		return False

	return is_tree_bst_helper(root.left, lb, root.key) and is_tree_bst_helper(root.right, root.key, rb)		


def is_tree_bst(root):
	return is_tree_bst_helper(root, -sys.maxint, sys.maxint)	


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
		nodes[i + 1].key = arr[i][0]
		if arr[i][1] != -1:
			nodes[i + 1].left = nodes[arr[i][1]]
		if arr[i][2] != -1:
			nodes[i + 1].right = nodes[arr[i][2]]

	return nodes[1]


if __name__ == "__main__":
	tests = [
		(None, True),
		([], True),
		([[1, -1, -1]], True),
		([[1, 2, -1], [2, -1, -1]], False),
		([[2, 2, -1], [1, -1, -1]], True),
		([[1, -1, 2], [2, -1, -1]], True),
		([[2, -1, 2], [1, -1, -1]], False),
		([[3, 2, 3], [4, -1, -1], [5, -1, -1]], False),
		([[3, 2, 3], [2, -1, -1], [1, -1, -1]], False),
		([[3, 2, 3], [5, -1, -1], [1, -1, -1]], False),
		([[2, 2, 3], [1, -1, -1], [3, -1, -1]], True),
		([[20, 2, 3], [10, -1, -1], [30, 4, 5], [5, -1, -1], [40, -1, -1]], False),
		([[20, 2, 3], [10, -1, -1], [30, 4, 5], [19, -1, -1], [40, -1, -1]], False),
		([[20, 2, 3], [10, -1, -1], [30, 4, 5], [20, -1, -1], [40, -1, -1]], True),
		([[20, 2, 3], [10, -1, -1], [30, 4, 5], [25, -1, -1], [40, -1, -1]], True),
		([[20, 2, 3], [21, -1, -1], [30, 4, 5], [25, -1, -1], [40, -1, -1]], False),
		([[20, 2, 3], [20, -1, -1], [30, 4, 5], [25, -1, -1], [40, -1, -1]], True),
	]
	
	for i in xrange(len(tests)):
		root = generate_binary_tree(tests[i][0])
		result = is_tree_bst(root)
		test_stat = "FAIL"
		if result == tests[i][1]:
			test_stat = "ok"
		print "Case", i + 1, ":", result, "--------", test_stat


