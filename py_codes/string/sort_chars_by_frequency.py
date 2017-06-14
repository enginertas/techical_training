#!/usr/bin/env python

def sort_chars_by_freq(s):
	chars = [0] * 256
	for ch in s:
		chars[ord(ch) % 256] += 1

	return ''.join(sorted(s, key = lambda x: (-chars[ord(x) % 256], x)))


if __name__ == "__main__":
	tests = ["", "c", "d", "ef", "fe", "eff", "ababccc", "eeddcc", "dancing queen"]
	for t in tests:
		print t, sort_chars_by_freq(t)