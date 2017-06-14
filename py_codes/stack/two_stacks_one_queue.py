#!/usr/bin/env python

class Queue:
	def __init__(self):
		self.in_stack = []
		self.out_stack = []

	def enqueue(self, x):
		self.in_stack.append(x)

	def dequeue(self):
		if not self.out_stack:
			if not self.in_stack:
				return None
			while self.in_stack:
				self.out_stack.append(self.in_stack.pop())
		return self.out_stack.pop()

	def is_empty(self):
		if (not self.in_stack) and (not self.out_stack):
			return True
		else:
			return False


if __name__ == "__main__":
	q = Queue()
	print q.is_empty()
	q.enqueue(5)
	print q.is_empty()
	print q.dequeue()
	print q.is_empty()
	print q.dequeue()
	print q.is_empty()
	q.enqueue(6)
	print q.is_empty()
	q.enqueue(6)
	q.enqueue(8)
	q.enqueue(9)
	q.enqueue(4)
	q.enqueue(2)
	print q.is_empty()
	while not q.is_empty():
		print q.dequeue()
		print q.is_empty()
	print q.dequeue()
	print q.is_empty() 