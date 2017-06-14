#!/usr/bin/env python

def isCyclic_dfs(node, graph, visited, in_stack):
	if node not in visited:
		visited[node] = True
		in_stack[node] = True

		for v in graph[node]:
			if v in in_stack:
				return True
			if (v not in visited):
				if isCyclic_dfs(v, graph, visited, in_stack):
					return True

		del in_stack[node]

	return False



def isCyclic(graph):
    visited = {}
    in_stack = {}
    for u in graph:
        if isCyclic_dfs(u, graph, visited, in_stack):
        	return True
    return False


if __name__ == "__main__":
    tests = [
        {},
        {'A': []},
        {'A': [], 'B': []},
        {'A': ['B'], 'B': []},
        {'A':[21, 'A'], 21: []},
        {'A':[21], 21: ['A']},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['A']},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['B']},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['C'], 'C':[]},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['C'], 'C':['C']},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['C'], 'C':[42]},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['C'], 'C':[21]},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['C'], 'C':['A']},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['C'], 'C':[50], 50: []},
        {'A':[21], 21: ['B'], 'B':[42], 42: ['C'], 'C':[50], 50: ['A']},
        {'A':[32, 64], 32: ['B'], 64: ['B'], 'B':[43], 43: ['C'], 'C':[16, 40], 16:['E'], 'D':[43], 'E': [40], 40: []},
        {'A':[32, 64], 32: ['B'], 64: ['B'], 'B':[43], 43: ['C'], 'C':[16, 40], 16:['E'], 'D':[43], 'E': [40], 40: ['D']},
        {'A':[40, 45], 40:[], 45: [], 'B':[18], 18:['C'], 'C':[24], 24:['B']},
        {'A':[40, 45], 40:[], 45: [], 'B':[18], 18:['C'], 'C':[24], 24:['A']}
    ]

    for t in tests:
        print "------------"
        print t
        print isCyclic(t)