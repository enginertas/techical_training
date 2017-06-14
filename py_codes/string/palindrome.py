#!/usr/bin/env python

import threading

THREAD_MIN = 8
THREAD_COUNT = 8

def is_palindrome(s):
	if not s:
		return True
	for i in xrange(len(s)/2):
		if s[i] != s[-i-1]:
			return False
	return True


def is_palindrome_partial(s, first_i, last_i, thread_id, exit_status):
	status = True
	for i in range(first_i, last_i):
		if s[i] != s[-i-1]:
			status = False
			break
	exit_status[thread_id] = status


def is_palindrome_with_thread(s):
	if not s:
		return True
	
	exit_status = []
	th_count = 0
	right = len(s) / 2
	if right < THREAD_MIN:
		exit_status = [-1]
		th_count = 1
		is_palindrome_partial(s, 0, right,  0, exit_status)
	else:
		th_count = THREAD_COUNT
		exit_status = [-1] * th_count
		interval = right / th_count
		for i in xrange(th_count):
			r = right
			if i < th_count - 1:
				r = interval * (i + 1)
			t = threading.Thread(is_palindrome_partial(s, interval * i, r, i, exit_status))
			t.start()

	while True:
		for i in xrange(th_count):
			if exit_status[i] == -1:
				continue
		break

	print "[DEBUG] Exit Statuses:", exit_status
	for i in xrange(th_count):
		if not exit_status[i]:
			return False
	return True


if __name__ == "__main__":
	tests = [None, [], "", "a", "b", "aa", "ab", "ba", "bca", "bcb", "aba", "cba", 
				"abba", "abaa", "cdddc", "cdadc", "cddac"]

	tests2 = ["abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba", "abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbca",
				"abbbbbbbbbbbbbbbbbbbbbbbbbbxbbbbbbbbbbbbbbbba", "cccccccccccccccccccccccdccccccccccccc",
				"cccccccccccccccdccccccccccccccc", "dbaaccccccccaabd", "dbaaccccacccaabd"]
	
	print "--------- Std Palindrome Tests: --------"
	for t in tests + tests2:
		print t, is_palindrome(t)

	print "--------- Palindrome with Thread Tests --------"
	for t in tests + tests2:
		print t, is_palindrome_with_thread(t)
