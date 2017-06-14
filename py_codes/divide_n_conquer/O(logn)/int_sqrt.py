#!/usr/bin/env python

def int_sqrt(x):
	if not isinstance(x, int):
		print "non-integer is not supported"
		return None

	if x < 0:
		print "Undefined mathematical operation: x < 0"
		return None
	if x >= 2**32:
		print "Large integers (x >= 2^32 are not supported)"
		return None

	if x == 0:
		return 0
	if x == 1:
		return 1

	lb, rb = 1, x
	while lb <= rb:
		mid = (lb + rb) / 2
		prod = mid * mid
		
		if (prod == x) or (prod < x and (mid + 1) * (mid + 1) > x):
			return mid
		
		if prod < x:
			lb = mid + 1
		else:
			rb = mid - 1


if __name__ == "__main__":
	tests = [-5, -4, -2, -1, -0.3, 0, 0.4, 0.99, 1, 1.2, 1.3, 1.9, 2, 2.0, 2.3, 2.5, 2.7, 3, 4, 5, 
			6, 7, 8, 9, 10, 11, 12, 19, 20, 25, 34, 36, 39, 48, 49, 57, 88, 99, 100, 101, 65535, 65536, 65537,
			2**32 - 1, 2**32, 2**32 + 1]

	for t  in tests:
		print "-----------------------"
		print t
		print int_sqrt(t)