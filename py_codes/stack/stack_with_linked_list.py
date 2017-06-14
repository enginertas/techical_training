#!/usr/bin/env python

class Node():
	def __init__(self, key=None, next=None):
		self.key = key
		self.next = next

class Stack():
	def __init__(self):
		self._head = Node()
		self._size = 0

	def push(self, key):
		new_node = Node(key, self._head)
		self._head = new_node
		self._size += 1

	def is_empty(self):
		return self._size == 0

	def pop(self):
		if self.is_empty():
			return None
		key = self._head.key
		self._head = self._head.next
		self._size -= 1
		return key


if __name__ == "__main__":
	q = Stack()
	print q.is_empty()
	q.push(5)
	print q.is_empty()
	print q.pop()
	print q.is_empty()
	print q.pop()
	print q.is_empty()
	q.push(6)
	print q.is_empty()
	q.push(6)
	q.push(8)
	q.push(9)
	q.push(4)
	q.push(2)
	print q.is_empty()
	while not q.is_empty():
		print q.pop()
		print q.is_empty()
	print q.pop()
	print q.is_empty() 