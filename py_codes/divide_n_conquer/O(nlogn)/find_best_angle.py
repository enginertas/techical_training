#!/usr/bin/env python

from math import degrees, atan2
import bisect

def calculateAngleByPoint(x, y):
	return degrees(atan2(y, x)) % 360

def findBestAngle(points, angle_range):
	if not points:
		return 0, 0

	if abs(angle_range) >= 360 and abs(angle_range) % 360 == 0:
		return 0, len(points)

	angle_range %= 360
	best_angle, max_count = 0, 0
	
	angles = []
	for x, y in points:
		angles.append(calculateAngleByPoint(x, y))
	angles.sort()

	print angles

	for i in xrange(len(angles)):
		end_angle = angles[i] + angle_range
		if end_angle < 360:
			count = bisect.bisect_right(angles, end_angle) - i
		else:
			count = len(angles) - i + bisect.bisect_right(angles, end_angle - 360)

		if count > max_count:
			best_angle, max_count = angles[i], count

	return best_angle, max_count

if __name__ == "__main__":
	big_array =[
		(5,0), (6,0), (7,0), (5,1), (7.5, 1.5), (10, 2), (15, 3), (20, 4), (7, 2), (14, 4), 
		(13, 4), (3, 1), (6, 2), (5, 2), (10, 4), (1, 1), (2, 2), (4, 4), (8, 8), (1, 1.2),
		(2, 2.4), (3, 3.6), (3, 3.62), (3, 3.63), (3, 3.64), (0, 5), (0, 10), (-1, 10), (-2, 20), (-5, 5), 
		(-7, 1), (-5, 0), (-6, -2), (-3, -1), (-1, -3), (-1, -5), (-1, -7), (0, -7), (0, -4), 
		(0, -3), (1, -8), (1, -7), (2, -14), (1.5, -10.5), (3, -21), (5, -1), (10, -2), 
		(7.5, -1.5), (12.5, -2.5), (15, -3), (6, -1), (9, -1.5), (12, -2), (15, -2.5), (15, -2.4)
	]
	tests = [
		(None, 50),
		([], 210),
		([(1,1)], 0),
		([(1,1)], 50),
		([(1,1)], 380),
		([(1,1)], -20),
		([(1,1), (2,2), (3, 4)], 0),
		([(1,1), (2,2), (3, 4), (3, 4)], 0),
		([(1,1), (2,2), (3, 4), (3, 4), (3, 4)], 0),
		([(1,1), (2,2), (3, 4)], 8.1301),
		([(1,1), (2,2), (3, 4)], 8.1302),
		([(1,1), (2,2), (4, 3)], 8.1301),
		([(1,1), (2,2), (4, 3)], 8.1302),
		([(1,1), (2,2), (-3, -3)], 539),
		([(1,1), (2,2), (-3, -3)], 540),
		([(1,1), (2,2), (3, -3)], -271),
		([(1,1), (2,2), (3, -3)], -270),
		(big_array, 0),
		(big_array, 10),
		(big_array, 12),
		(big_array, 33),
		(big_array, 410.5),
		(big_array, 410.51),
		(big_array, -270),
		(big_array, -180),
		(big_array, 630),
		(big_array, -11.4),
		(big_array, -11.3),
		(big_array, 360),
		(big_array, 720),
		(big_array, -1080)
	]

	test_i = 0
	for points, angle in tests:
		print "----------------- Test %d -----------------" %test_i
		print "Points:", points, "Angle:", angle
		best_angle, max_count = findBestAngle(points, angle)
		print "Best Angle:", best_angle, "Max Count:", max_count