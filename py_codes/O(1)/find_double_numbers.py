#!/usr/bin/env python

def findDoubleNumbers(a, b):
	if a >= b:
		return 0

	count = 0
	a += 1

	while True:
		rem = a % 100
		if (rem / 10) == (rem % 10):
			count += 1
		if a == b or rem == 99:
			break
		a += 1

	if a == b:
		return count

	while True:
		rem = b % 100
		if (rem / 10) == (rem % 10):
			count += 1
		if rem == 0:
			break
		b -= 1

	count += (b / 100 - a / 100 - 1) * 10
	return count

if __name__ == "__main__":
	tests = [
		((0, 0), 0),
		((1, 0), 0),
		((3, 2), 0),
		((501, 500), 0),
		((400, 400), 0),
		((10, 11), 1),
		((11, 12), 0),
		((10, 22), 2),
		((11, 22), 1),
		((74, 88), 2),
		((74, 89), 2),
		((74, 99), 3),
		((74, 98), 2),
		((74, 87), 1),
		((77, 87), 0),
		((77, 88), 1),
		((74, 100), 4),
		((74, 101), 4),
		((74, 110), 4),
		((74, 111), 5),
		((74, 122), 6),
		((98, 99), 1),
		((98, 100), 2),
		((99, 100), 1),
		((99, 101), 1),
		((99, 110), 1),
		((99, 111), 2),
		((98, 199), 11),
		((99, 199), 10),
		((98, 200), 12),
		((99, 200), 11),
		((99, 210), 11),
		((99, 211), 12),
		((98, 211), 13),
		((98, 311), 23),
		((98, 411), 33),
		((98, 37111), 3703)
	]

	test_i = 1
	for (a, b), r in tests:
		print "-------------- Test %d --------------" %test_i
		print "Input: (%d, %d)" %(a, b) 
		output = findDoubleNumbers(a, b)
		print "Output:", output
		assert output == r
		print "OK"
		test_i += 1

	print "** ALL TESTS ARE OK! **"