#!/usr/bin/env python

import sys

def calculateGcd(gcd_arr, max_arr):
    gcd_arr[1] = max_arr
    for i in xrange(max_arr, 1, -1):
        j = i << 1
        while j <= max_arr:
            if gcd_arr[j] and gcd_arr[j] > gcd_arr[i]:
                gcd_arr[i] = gcd_arr[j]
            j += i
    
    
def maximumGcdAndSum(A, B):
    max_A, max_B = max(A), max(B)
    gcd_A = [0] * (max_A + 1)
    gcd_B = [0] * (max_B + 1)
    
    for el in A:
        gcd_A[el] = el
    calculateGcd(gcd_A, max_A)
    
    for el in B:
        gcd_B[el] = el
    calculateGcd(gcd_B, max_B)
    
    for i in xrange(min(max_A, max_B), 0, -1):
        if gcd_A[i] and gcd_B[i]:
            return gcd_A[i] + gcd_B[i]

        
if __name__ == "__main__":
    A = []
    B = []
    for i in xrange(1, 1000000, 2):
        A.append(i)
    for i in xrange(2, 1000000, 2):
        B.append(i)

    print max(A), max(B), len(A), len(B)

    res = maximumGcdAndSum(A, B)
    print res
