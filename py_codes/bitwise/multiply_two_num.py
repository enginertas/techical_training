#!/usr/bin/env python

def multiply_pos(a, b):
	result = 0
	while b > 0:
		if b & 1 == 1:
			result += a
		a <<= 1
		b >>= 1
	return result

def multiply(a, b):
	if a == 0 or b == 0:
		return 0

	if a < 0 and b < 0:
		return multiply_pos(-a, -b)
	elif a < 0 and b > 0:
		return -multiply_pos(-a, b)
	elif a > 0 and b < 0:
		return -multiply_pos(a, -b)
	else:
		return multiply_pos(a, b)

if __name__ == "__main__":
	tests = [(0, 0), (0, 47), (47, 0), (-37, -2), (-40, -1050), (-50, 60), (-70, 10),
				(10, -40), (50, -100), (6, 8), (12, 90), (106, 100)]
	for a, b in tests:
		print a, '*', b, '=', multiply(a, b)