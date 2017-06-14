#!/usr/bin/env python

FIBONACCI_BASE = [1, 1, 0]
PROCESSED, NOT_PROCESSED = 1, 0
MOD = 10**9 + 7


def matrixMultiply(matrix1, matrix2):
    result_matrix = []
    result_matrix.append((matrix1[0] * matrix2[0] + matrix1[1] * matrix2[1]) % MOD)
    result_matrix.append((matrix1[0] * matrix2[1] + matrix1[1] * matrix2[2]) % MOD)
    result_matrix.append((matrix1[1] * matrix2[1] + matrix1[2] * matrix2[2]) % MOD)
    return result_matrix


def matrixMultiplyInPlace(matrix1, matrix2):
    m0 = (matrix1[0] * matrix2[0] + matrix1[1] * matrix2[1]) % MOD
    m1 = (matrix1[0] * matrix2[1] + matrix1[1] * matrix2[2]) % MOD
    m2 = (matrix1[1] * matrix2[1] + matrix1[2] * matrix2[2]) % MOD
    matrix1[0] = m0
    matrix1[1] = m1
    matrix1[2] = m2


def matrixSumInPlace(matrix1, matrix2):
    matrix1[0] = (matrix1[0] + matrix2[0]) % MOD
    matrix1[1] = (matrix1[1] + matrix2[1]) % MOD
    matrix1[2] = (matrix1[2] + matrix2[2]) % MOD    


def matrixSubstractInPlace(matrix1, matrix2):
    matrix1[0] = (matrix1[0] - matrix2[0]) % MOD
    matrix1[1] = (matrix1[1] - matrix2[1]) % MOD
    matrix1[2] = (matrix1[2] - matrix2[2]) % MOD  


def calculateFibonacciMatrix(n):
    matrix = FIBONACCI_BASE[:]
    result = [1, 0, 1]

    while n > 0:
        if n & 1 == 1:
            matrixMultiplyInPlace(result, matrix)
        n >>= 1
        matrixMultiplyInPlace(matrix, matrix)
        
    return result


def convertAllToFibonacciMatrices(node_values, n):
    for i in xrange(n):
        node_values[i] = calculateFibonacciMatrix(node_values[i])


def halveGraph(graph, n, root):
    visited = [False] * n
    halved_graph = []
    for i in xrange(n):
        halved_graph.append([])

    dfs_stack = [root]
    while dfs_stack:
        cur_node = dfs_stack.pop()
        visited[cur_node] = True
        for u in graph[cur_node]:
            if not visited[u]:
                halved_graph[cur_node].append(u)
                dfs_stack.append(u)

    return halved_graph

def solve(graph, node_values, n, root):
    total_sum = [0, 0, 0]
    local_sum = []
    for i in xrange(n):
        local_sum.append([0, 0, 0])
    
    state_stack = [NOT_PROCESSED]
    dfs_stack = [root]
    while dfs_stack:
        cur_node = dfs_stack[-1]
        cur_state = state_stack[-1]
        if cur_state == NOT_PROCESSED:
            state_stack[-1] = PROCESSED              
            for u in graph[cur_node]:
                state_stack.append(NOT_PROCESSED)
                dfs_stack.append(u)
        else:
            matrixSumInPlace(local_sum[cur_node], node_values[cur_node])
            matrixSumInPlace(total_sum, node_values[cur_node])
            cur_edges = graph[cur_node]
            all_edges_mult_sum = [0, 0, 0]
            if len(cur_edges) == 1:
                mult_i = matrixMultiply(local_sum[cur_edges[0]], node_values[cur_node])
                matrixSumInPlace(local_sum[cur_node], mult_i)
                matrixSumInPlace(total_sum, mult_i)
                matrixSumInPlace(total_sum, mult_i)
            else:
                for i in xrange(len(cur_edges)):
                    mult_i = matrixMultiply(local_sum[cur_edges[i]], node_values[cur_node])
                    matrixSumInPlace(local_sum[cur_node], mult_i)
                    matrixSumInPlace(all_edges_mult_sum, mult_i)
                    matrixSumInPlace(total_sum, mult_i)
                    matrixSumInPlace(total_sum, mult_i)
                for i in xrange(len(cur_edges)):
                    sum_i = matrixMultiply(local_sum[cur_edges[i]], all_edges_mult_sum)
                    mult_i = matrixMultiply(local_sum[cur_edges[i]], node_values[cur_node])
                    mult_i = matrixMultiply(local_sum[cur_edges[i]], mult_i)
                    matrixSubstractInPlace(sum_i, mult_i)
                    matrixSumInPlace(total_sum, sum_i)
            dfs_stack.pop()
            state_stack.pop()
            
    return total_sum[0]
    

def readInput():
    n = int(raw_input().strip())
      
    graph = []
    for i in xrange(n):
        graph.append([])
    
    for i in xrange(n - 1):
        x, y = map(int, raw_input().strip().split())
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)
        
    root = None
    for i in xrange(n):
        if len(graph[i]) == 1:
            root = i
            break
    graph = halveGraph(graph, n, root)
           
    node_values = map(int, raw_input().strip().split())
    convertAllToFibonacciMatrices(node_values, n)

    print solve(graph, node_values, n, root)
        
    
if __name__ == "__main__":
    readInput()