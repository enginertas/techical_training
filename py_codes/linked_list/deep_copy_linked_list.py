#!/usr/bin/env python

import sys

class Node():
	def __init__(self):
		self.next = None
		self.key = None

def deep_copy_linked_list(head):
	if not head:
		return None
	
	dummy = Node()
	tail = dummy
	
	while head:
		tail.next = Node()
		tail = tail.next
		tail.key = head.key
		tail.next = None
		head = head.next
	
	return dummy.next


'''
---------------------------------------------------
	Test codes are below
---------------------------------------------------
'''
def print_linked_list(head):
	if not head:
		print None
	else:
		while head:
			sys.stdout.write(str(head.key) + " ")
			head = head.next
		sys.stdout.write("\n")


def create_linked_list(arr):
	if not arr:
		return None

	head = None
	for el in reversed(arr):
		p = Node()
		p.next = head
		p.key = el
		head = p

	return head


def set_inf_linked_list(head):
	if not head:
		return

	while head:
		head.key = sys.maxint
		head = head.next


if __name__ == "__main__":
	tests = [None, [], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 0, 8]]
	for t in tests:
		ll = create_linked_list(t)
		print "---------------------------------"
		print "Before:"
		print_linked_list(ll)
		ll_copy = deep_copy_linked_list(ll)
		print "After Copy:"
		print_linked_list(ll_copy)
		print "After Set Inf:"
		set_inf_linked_list(ll_copy)
		print_linked_list(ll)
		print_linked_list(ll_copy)