#!/usr/bin/env python

def solveIndexZero(n, k):
	if n == 1:
		return 0
	else:
		return (solveIndexZero(n - 1, k) + k) % n


def solve(n, k):
    return solveIndexZero(n, k) + 1

    
if __name__ == "__main__":
    n_cases = int(raw_input().strip())
    for i in xrange(n_cases):
        n, k = map(int, raw_input().strip().split())
        print solve(n, k)