#!/usr/bin/env python

class Node():
	def __init__(self):
		self.key = None
		self.children = []

def sum_tree(root):
	result = root.key
	for c in root.children:
		result += sum_tree(c)
	return result

def trim_tree_by_height_helper(root, cur_h, height):
	if cur_h < height:
		for c in root.children:
			trim_tree_by_height_helper(c, cur_h + 1, height)
	elif cur_h == height:
		root.key = sum_tree(root)
		root.children = []

def trim_tree_by_height(root, height):
	if not root:
		return
	trim_tree_by_height_helper(root, 0, height)


'''
------------------------------------
TEST FUNCTIONS ARE BELOW
------------------------------------
'''
def build_tree(val):
	if val == None:
		return None
	child14 = Node()
	child14.key = 14
	child13 = Node()
	child13.key = 13
	child12 = Node()
	child12.key = 12
	child11 = Node()
	child11.key = 11
	child11.children.append(child12)
	child11.children.append(child13)
	child11.children.append(child14)
	child10 = Node()
	child10.key = 10
	child10.children.append(child11)
	child9 = Node()
	child9.key = 9
	child9.children.append(child10)
	child8 = Node()
	child8.key = 8
	child7 = Node()
	child7.key = 7
	child7.children.append(child8)
	child7.children.append(child9)
	child6 = Node()
	child6.key = 6
	child5 = Node()
	child5.key = 5
	child4 = Node()
	child4.key = 4
	child3 = Node()
	child3.key = 3
	child3.children.append(child6)
	child3.children.append(child7)
	child2 = Node()
	child2.key = 2
	child2.children.append(child4)
	child2.children.append(child5)
	child1 = Node()
	child1.key = 1
	root = Node()
	root.key = 0
	root.children.append(child1)
	root.children.append(child2)
	root.children.append(child3)
	return root

def print_tree(root):
	if not root:
		print None
	else:
		if root.children: 
			for c in root.children:
				print root.key, c.key
			for c in root.children:
				print_tree(c)
		else:
			print root.key, "no child"


if __name__ == "__main__":
	roots = [None, 0]
	for i in xrange(len(roots)):
		print "------------------- Tree", i, "-------------------"
		for j in xrange(10):
			print "** Trim by height", j, "**"
			root = build_tree(roots[i])
			trim_tree_by_height(root, j)
			print_tree(root)