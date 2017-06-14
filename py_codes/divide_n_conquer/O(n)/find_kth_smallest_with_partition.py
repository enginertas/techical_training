#!/usr/bin/env python

'''
Example Input:
9
1 9 7 8 6 3 4 5 2


Expected Output:
5
'''

import sys

def swap(arr, ind1, ind2):
    tmp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = tmp
    
    
def partition(low, high, arr):
    pivot = arr[high]
    s1 = low - 1
    for i in range(low, high):
        if arr[i] < pivot:
            s1 += 1
            swap(arr, s1, i)
    
    s1 += 1
    swap(arr, s1, high)
    return s1
            
    
def getAtIndex(low, high, arr, d_index):    
    mid = partition(low, high, arr)
    if mid == d_index:
        return arr[d_index]
    elif mid < d_index:
        return getAtIndex(mid + 1, high, arr, d_index)
    else:
        return getAtIndex(low, mid - 1, arr, d_index)
    
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    print getAtIndex(0, n - 1, arr, n/2)
    
    