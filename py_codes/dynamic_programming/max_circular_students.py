#!/usr/bin/env python
'''
Example Input:
5
3 4 1 2 0

Example Output:
2

'''

def mod(x, n):
    if x < 0:
        return x + n
    elif x >= n:
        return x - n
    else:
        return x

def solve(n, arr):
    up = [0] * n
    down = [0] * n
    for i in xrange(n):
        if arr[i] == n or arr[i] == 0:
            continue
        up[mod(i + 1, n)] += 1
        down[mod(i - arr[i] + 1, n)] += 1
    
    cur_sum = 0
    t = 0
    for i in xrange(n):
        if arr[i] <= t:
            cur_sum += 1
        t += 1
    
    max_index = 0
    max_sum = cur_sum
    for i in range(1, n):
        cur_sum = cur_sum + up[i] - down[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_index = i
            
    return max_index + 1

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    print solve(n, arr)