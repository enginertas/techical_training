#!/usr/bin/env python

from collections import defaultdict

'''
Imagine a horizontal corridor bounded by y = y1 and y = y2 lines on a 2D-plane. Imagine there are
radars on that plane with center (x, y) and they are operating within a specific range (r).
This code determines if a burglar can reach x = +inf from x = -inf through barrier without
being detected by any radars.
Parameters:
	* radars: List[(x, y, r)] -> All radars located on the plane
		- x and y are integers
		- r is unsigned integer (>= 0)
	* corr_y1: int -> First horizontal barrier of the corridor.
	* corr_y2: int -> Second horizontal barrier of the corridor.
Returns:
	* bool -> If any route without being detected exists, True. Otherwise, False.
'''
def can_pass_through_radars(radars, corr_y1, corr_y2):
	if not radars:
		return True

	corr_down, corr_up = min(corr_y1, corr_y2), max(corr_y1, corr_y2)

	# Transform radar intersections into graph
	graph = construct_radar_intersection_graph(radars)

	# Starting from source nodes (on corridor up), try to reach corridor down via DFS. If the
	# whole corridor is vertically spanned by intersected radars, it means that there are NOT
	# any routes escaping from radars.
	return not graph_reaches_corridor_down(graph, radars, corr_down, corr_up)


def do_radars_intersect(radar1, radar2):
	x1, y1, r1 = radar1
	x2, y2, r2 = radar2
	return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2

'''
Use a modified version of line sweep algorithm. Even if encircling squares of circles
intersect, circles may not intersect. Ensure intersections via euclidean distances.
'''
def construct_radar_intersection_graph(radars):
	graph = [set() for _ in xrange(len(radars))]

	# Register the opening and closing y values to event list. Reverse sort for traversal 
	# up to bottom. Please note that, 'close' events should be processed later than 'open' events
	# T(n) = T(append) + T(sort) = O(n) + O(nlogn) = O(nlogn)
	events = []
	for idx, (_, y, r) in enumerate(radars):
		events.append((y + r, 'o', idx))
		events.append((y - r, 'c', idx))
	events.sort(reverse = True)

	# For each close event, just remove idx from interval tree -> O(logn).
	# For each open event, firstly, query and process all circles located in given range.
	#	Then, add idx to interval tree -> O(logn + k_i + logn) = O(logn + k_i)
	# We have n open and n close events.
	# T(n) = T(close) + T(open) = O(n * logn) + O(n * (logn + k_avg)) = O(nlogn + nk_avg)
	# Worst case: O(n ^ 2) where circles overlap a lot [k ~ O(n)].
	# Best case: O(nlogn) where circles are not tightly located [k ~ O(1)].
	radar_stack = set()
	for y, event_type, idx in events:
		if event_type == 'o':
			for idx_stack in radar_stack:
				if do_radars_intersect(radars[idx], radars[idx_stack]):
					graph[idx].add(idx_stack)
					graph[idx_stack].add(idx)
			radar_stack.add(idx)
		else:
			radar_stack.remove(idx)

	return graph


def graph_reaches_corridor_down(graph, radars, corr_down, corr_up):
	visited = [False] * len(graph)

	radar_stack = []
	for idx, (_, y, r) in enumerate(radars):
		if y - r <= corr_down:
			radar_stack.append(idx)
			visited[idx] = True

	# DFS. It looks like BFS since it has many sources. But please figure out the stack :)
	# Complexity: O(V + E) = O(n + k) where k is number of intersections.
	# Worst Case: O(n ^ 2) because there may be k ~ O(n^2) intersections.
	# Best Case: O(n) where there are not many intersections.
	while radar_stack:
		u = radar_stack.pop()
		_, y, r = radars[u]
		if y + r >= corr_up:
			return True

		for v in graph[u]:
			if not visited[v]:
				visited[v] = True
				radar_stack.append(v)

	return False


if __name__ == '__main__':
	tests = [
		(([], 10, 10), True),
		(([], -3, 5), True),
		(([], 5, -3), True),
		(([(4, 5, 0)], 4, 4), True),
		(([(4, 5, 0)], 5, 5), False),
		(([(4, 5, 0)], 6, 6), True),
		(([(4, 5, 0)], 6, 7), True),
		(([(4, 5, 0)], 5, 6), True),
		(([(4, 5, 0)], 4, 5), True),
		(([(4, 5, 0)], 3, 4), True),
		(([(4, 5, 1)], 3, 3), True),
		(([(4, 5, 1)], 4, 4), False),
		(([(4, 5, 1)], 5, 5), False),
		(([(4, 5, 1)], 6, 6), False),
		(([(4, 5, 1)], 7, 7), True),
		(([(4, 5, 1)], 3, 4), True),
		(([(4, 5, 1)], 4, 5), False),
		(([(4, 5, 1)], 5, 6), False),
		(([(4, 5, 1)], 6, 7), True),
		(([(4, 5, 1)], 3, 5), True),
		(([(4, 5, 1)], 4, 6), False),
		(([(4, 5, 1)], 5, 7), True),
		(([(4, 5, 2)], 0, 2), True),
		(([(4, 5, 2)], 1, 3), True),
		(([(4, 5, 2)], 2, 4), True),
		(([(4, 5, 2)], 3, 5), False),
		(([(4, 5, 2)], 4, 6), False),
		(([(4, 5, 2)], 5, 7), False),
		(([(4, 5, 2)], 6, 8), True),
		(([(4, 5, 2)], 7, 9), True),
		(([(4, 5, 2)], 8, 10), True),
		(([(4, 5, 6)], -3, -2), True),
		(([(4, 5, 6)], -2, -1), True),
		(([(4, 5, 6)], -1, 0), False),
		(([(4, 5, 6)], 10, 11), False),
		(([(4, 5, 6)], 11, 12), True),
		(([(4, 5, 6)], 12, 13), True),
		(([(0, -2, 2), (0, 2, 2) ], 5, -4), True),
		(([(0, -2, 2), (0, 2, 2) ], 4, -5), True),
		(([(0, -2, 2), (0, 2, 2) ], 4, -4), False),
		(([(0, -2, 2), (1, 2, 2) ], 4, -4), True),
		(([(-1, -2, 2), (0, 2, 2) ], 4, -4), True),
		(([(-1, -2, 2), (0, 2, 2), (1, 0, 1) ], 4, -4), False),
		(([(-1, -2, 2), (0, 2, 2), (1, 1, 1) ], 4, -4), True),
		(([(-1, -2, 2), (0, 2, 2), (1, 1, 2) ], 4, -4), False),
		(([(-1, -2, 2), (0, 2, 2), (1, -1, 1) ], 4, -4), True),
		(([(-1, -2, 2), (0, 2, 2), (1, -1, 2) ], 4, -4), False),
		(([(20, -1, 2), (20, -2, 2), (20, -3, 2), (20, -4, 2), (20, 0, 2), (20, 1, 2),
			(20, 2, 2), (20, 3, 2), (20, 4, 2), (20, 6, 2), (18, 5, 2), (16, 4, 2),
			(14, 4, 2), (10, 4, 2), (6, 4, 2), (5, 3, 2), (4, 2, 2)], 0, 10), True),
		(([(20, -1, 2), (20, -2, 2), (20, -3, 2), (20, -4, 2), (20, 0, 2), (20, 1, 2),
			(20, 2, 2), (20, 3, 2), (20, 4, 2), (20, 6, 2), (18, 5, 2), (16, 4, 2),
			(14, 4, 2), (10, 4, 2), (6, 4, 2), (5, 3, 2), (4, 2, 2), (3, 4, 2),
			(2, 6, 2), (1, 8, 2)], 0, 10), False),
		(([(20, -1, 2), (20, -2, 2), (20, -3, 2), (20, -4, 2), (20, 0, 2), (20, 1, 2),
			(20, 2, 2), (20, 3, 2), (20, 4, 2), (20, 6, 2), (18, 5, 2), (16, 4, 2),
			(14, 4, 2), (10, 4, 2), (6, 4, 2), (5, 3, 2), (4, 2, 2), (3, 4, 2),
			(2, 6, 2), (-1, 8, 2)], 0, 10), False),
		(([(20, -1, 2), (20, -2, 2), (20, -3, 2), (20, -4, 2), (20, 0, 2), (20, 1, 2),
			(20, 2, 2), (20, 3, 2), (20, 4, 2), (20, 6, 2), (18, 5, 2), (16, 4, 2),
			(14, 4, 2), (10, 4, 2), (6, 4, 2), (5, 3, 2), (4, 2, 2), (3, 4, 2),
			(2, 6, 2), (-2, 8, 2)], 0, 10), True),
		(([(20, -1, 2), (20, -2, 2), (20, -3, 2), (20, -4, 2), (20, 0, 2), (20, 1, 2),
			(20, 2, 2), (20, 3, 2), (20, 4, 2), (20, 6, 2), (16, 4, 2),
			(14, 4, 2), (10, 4, 2), (6, 4, 2), (5, 3, 2), (4, 2, 2), (3, 4, 2),
			(2, 6, 2), (-1, 8, 2)], 0, 10), False),
		(([(20, -1, 2), (20, -2, 2), (20, -3, 2), (20, -4, 2), (20, 0, 2), (20, 1, 2),
			(20, 2, 2), (20, 6, 2), (16, 4, 2), (14, 4, 2), (10, 4, 2), (6, 4, 2),
			(5, 3, 2), (3, 4, 2), (2, 6, 2), (-1, 8, 2)], 0, 10), True),
		(([(-4, 4, 3), (-1, 3, 2), (-2, 2, 1), (-4, 0, 2), (-2, -2, 1), (1, -1, 1), 
			(2, 0, 2), (3, -4, 1), (5, -4, 3), (1, -6, 2)], 6, -8), True),
		(([(-4, 4, 3), (-1, 3, 2), (-2, 2, 1), (-4, 0, 2), (-2, -2, 1), (1, -1, 1), 
			(2, 0, 2), (3, -4, 1), (5, -4, 3), (1, -6, 2), (2, 4, 2)], 6, -8), False),
		(([(-4, 4, 3), (-1, 3, 2), (-2, 2, 1), (-4, 0, 2), (-2, -2, 1), (1, -1, 1), 
			(2, 0, 2), (3, -4, 1), (5, -4, 3), (1, -6, 2), (2, 4, 2)], 6, -9), True),
	]

	for (points, y1, y2), expected_res in tests:
		actual_res = can_pass_through_radars(points, y1, y2)
		print '--------------------------------------------'
		print points, (y1, y2), 'Actual: ', actual_res, 'Expected:', expected_res
		assert actual_res == expected_res
		print 'OK'
