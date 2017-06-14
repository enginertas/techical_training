#!/usr/bin/env python

def reverseInt(no):
	if no < 0:
		return None

	digit = -1
	
	x = no
	while x > 0:
		digit += 1
		x /= 10

	x = no
	result = 0
	while x > 0:
		result += (x % 10) * (10 ** digit)
		digit -= 1
		x /= 10

	return result

if __name__ == "__main__":
	tests = [-2, -1, 0, 1, 2, 3, 6, 9, 10, 11, 12, 13, 18, 20, 21, 23, 29, 41, 50,
		77, 99, 100, 101, 109, 110, 112, 116, 119, 120, 167, 1000, 1001, 1100, 1010]

	for t in tests:
		print t, reverseInt(t)