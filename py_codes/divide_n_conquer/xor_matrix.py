#!/usr/bin/python

'''

Example Input:
10 42
1 2 3 4 5 6 7 1 2 3

Correct Output:
6 3 0 0 1 2 2 3 5 2

'''

import sys

Cols = 0
Rows = 0
Old_Arr = []
New_Arr = []
    
def readInput():
    global Cols, Rows, Old_Arr, New_Arr
    Cols, Rows = map(long, raw_input().strip().split())
    Old_Arr = map(int, raw_input().strip().split())
    New_Arr = [0] * Cols

def printArray(arr):
    for a in arr:
        sys.stdout.write(str(a) + ' ')

def switch():
    global New_Arr, Old_Arr
    tmp = Old_Arr
    Old_Arr = New_Arr
    New_Arr = tmp
   
def twice(amount):
    global New_Arr
    for i in xrange(Cols):
        New_Arr[i] = Old_Arr[i] ^ Old_Arr[(i + amount) % Cols]
    switch()

def solve(rows):
    global Old_Arr
    
    i, r = 1L, rows
    while True:
        while i < r:
            i *= 2
        
        if i == r:
            twice(i)
            return
        
        twice(i / 2)
            
        r = r - i / 2
        i = 1
        
         
if __name__ == "__main__":
    readInput()
    if not (Rows <= 1 or Cols < 1):
        solve(Rows - 1)
    printArray(Old_Arr)