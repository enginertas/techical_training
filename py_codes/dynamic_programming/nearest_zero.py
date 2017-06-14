#!/usr/bin/env python

import sys

def find_distances_to_zero(arr):
	if not arr:
		return None

	distArray = [sys.maxint] * len(arr)
	
	for rng in [xrange(len(arr)), reversed(xrange(len(arr)))]:
		prevZeroDist = sys.maxint
		for i in rng:
			if arr[i] == 0:
				prevZeroDist = 1
				distArray[i] = 0
			else:
				distArray[i] = min(distArray[i], prevZeroDist)
				if prevZeroDist != sys.maxint:
					prevZeroDist += 1

	return distArray


if __name__ == "__main__":
	tests = [
		None,
		[],
		[0],
		[1],
		[0, 1],
		[1, 0],
		[1, 1],
		[0, 1, 1, 0],
		[1, 1, 1, 1],
		[0, 1, 1, 1, 0],
		[0, 1, 1, 1, 1, 0],
		[1, 1, 1, 1, 0],
		[0, 1, 1, 1, 1],
		[0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
		[0, 1, 1, 0, 1, 1, 1, 1, 0]
	]

	for t in tests:
		print t, "\t Distances:", find_distances_to_zero(t) 