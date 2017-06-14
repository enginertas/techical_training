#!/usr/bin/env python

def findRecursively(left, right, p):
    if not left or not right or p < 0:
        return 0
    
    left_1 = []
    left_0 = []
    right_0 = []
    right_1 = []
    for l in left:
        if l & (1 << p) > 0:
            left_1.append(l)
        else:
            left_0.append(l)
            
    for r in right:
        if r & (1 << p) > 0:
            right_1.append(r)
        else:
            right_0.append(r)
         
    max_xor = 0
    left_xor = 0
    right_xor = 0
    if left_1 and right_0:
        max_xor = (1 << p)
        left_xor = findRecursively(left_1, right_0, p - 1)
    if left_0 and right_1:
        max_xor = (1 << p)
        right_xor = findRecursively(right_1, left_0, p - 1)

    if max_xor > 0:
        return max_xor | max(left_xor, right_xor)
    
    if left_1:
        left = left_1
    else:
        left = left_0
        
    if right_0:
        right = right_0
    else:
        right = right_1
        
    return findRecursively(left, right, p - 1)
        

def findMaximumXOR(nums):
    max_num = max(nums)
    max_bits = 0
    while max_num:
        max_num = max_num >> 1
        max_bits += 1
    
    return findRecursively(nums, nums, max_bits - 1)


if __name__ == "__main__":
    print findMaximumXOR([3,10,5,25,2,8])
    print findMaximumXOR([20, 30, 12, 14, 1, 3, 5, 42, 7, 9])