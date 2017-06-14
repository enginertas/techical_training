#!/usr/bin/env python
import sys

'''
Example Input:
4 5
3 1
3 4
2 4
2 3
4 1

Expected Output:
4
2 3 4 1
'''

def create(graph, index):
    new_g = []
    visited = []
    in_q = []
    farthest = 0
    for i in xrange(len(graph)):
        new_g.append([])
        visited.append(False)
        in_q.append(False)
    q_i = 0
    queue = [(index, 0)]
    while q_i < len(queue):
        u, w = queue[q_i]
        farthest = u
        q_i += 1
        visited[u] = True
        for v, t in graph[u]:
            if not visited[v]:
                new_g[u].append((v, w + 1))
                new_g[v].append((u, w + 1))
                if not in_q[v]:
                    queue.append((v, w + 1))
                    in_q[v] = True
    return new_g, farthest

def search(graph, index):
    global Current_Path
    tmp_l = 0
    visited = [False] * len(graph)
    stack = [(index, 0)]
    while stack:
        max_w = 0
        max_u = -1
        u, prev_w = stack[-1]
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                if w > max_w:
                    max_w = w
                    max_u = v
        if max_w == 0:
            stack.pop()
        else:
            stack.append((max_u, prev_w + 1))
            if tmp_l < prev_w + 1:
                tmp_l = prev_w + 1
                Current_Path = stack[:]
    return tmp_l
    
def solve(n, m, graph):
    length = 0
    tmp_l = 0
    path = []
    
    # A bit more elimination for huge graph
    max_range = n
    if n > 500:
        max_range = 100000 / m
        
    # Algorithm itself
    for i in xrange(1, max_range + 1):
        new_g, j = create(graph, i)
        tmp_l = search(new_g, j)
        if length < tmp_l:
            length = tmp_l
            path = Current_Path 
        
    print length + 1
    for u in path:
        sys.stdout.write(str(u[0]) + ' ')

if __name__ == "__main__":
    n, m = map(int, raw_input().strip().split())   
    graph = [[]]
    for i in xrange(n):
        graph.append([])
    for i in xrange(m):
        u, v = map(int, raw_input().strip().split())
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    solve(n, m, graph)    
