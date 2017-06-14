#!/usr/bin/env python

'''
Example Input:

3 5
0 0 0 0 0
1 9 9 9 1
0 0 0 0 0
3
0 0 2 4
0 3 2 3
1 1 1 3
'''

import sys
from heapq import *

Row_Count = 0
Col_Count = 0
Query_Count = 0
Table = []
Query_List = []    
     

def readInput():
    global Row_Count, Col_Count, Query_Count, Table, Query_List
    
    Row_Count, Col_Count = map(int, raw_input().split())
    for i in xrange(Row_Count):
        row = []
        
        entry_list = raw_input().split()
        for j in xrange(Col_Count):
            row.append(int(entry_list[j]))
        
        Table.append(row)
        
    Query_Count = int(raw_input())
    for i in xrange(Query_Count):
        Query_List.append(map(int, raw_input().split()))
    
    
def isValidSquare(row, col):
    return (row >= 0 and row < Row_Count) and (col >= 0 and col < Col_Count)
      
    
def processSingleQuery(start_row, start_col, end_row, end_col):
    shortest_paths = [ [ sys.maxint for j in range(Col_Count) ] for i in range(Row_Count) ]
    visited = [ [ False for j in range(Col_Count) ] for i in range(Row_Count) ]  
    bfs_heap = []
    heappush(bfs_heap, (Table[start_row][start_col], start_row, start_col))
    
    while bfs_heap:
        weight, row, col = heappop(bfs_heap)
        if visited[row][col]:
            continue

        visited[row][col] = True
        shortest_paths[row][col] = weight
        
        '''
        if row == end_row and col == end_col:
            break
        '''      
        if isValidSquare(row - 1, col) and not visited[row - 1][col] :
            if weight + Table[row - 1][col] < shortest_paths[row - 1][col] :
                heappush(bfs_heap, (weight + Table[row - 1][col], row - 1, col))
        if isValidSquare(row + 1, col) and not visited[row + 1][col]:
            if weight + Table[row + 1][col] < shortest_paths[row + 1][col] :
                heappush(bfs_heap, (weight + Table[row + 1][col], row + 1, col))
        if isValidSquare(row, col - 1) and not visited[row][col - 1]:
            if weight + Table[row][col - 1] < shortest_paths[row][col - 1] :
                heappush(bfs_heap, (weight + Table[row][col - 1], row, col - 1))
        if isValidSquare(row, col + 1) and not visited[row][col + 1]:
            if weight + Table[row][col + 1] < shortest_paths[row][col + 1] :
                heappush(bfs_heap, (weight + Table[row][col + 1], row, col + 1))
    
    return shortest_paths[end_row][end_col]
                        

if __name__ == '__main__':
    readInput()
    for i in xrange(Query_Count):
        print processSingleQuery(Query_List[i][0], Query_List[i][1], Query_List[i][2], Query_List[i][3])
