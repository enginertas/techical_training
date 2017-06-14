#!/usr/bin/env python

'''
This leaderboard is intended to be used only for EXTREMELY SMALL leaderboards (i.e. 10 leaders).
	Therefore, we can guarantee constant time class functions

Please note that there are NOT any limits for URLs in URL Dictionary
'''
class Leaderboard():
	def __init__(self, windowSize = 10):
		self._windowSize = windowSize
		self._leaders = []
		
		for i in xrange(self._windowSize):
			self._leaders.append(["", -1])
		
		self._urlDict = {}


	def get_leaders(self):
		leaders = []
		
		for i in xrange(self._windowSize):
			if self._leaders[i][1] != -1:
				leaders.append(self._leaders[i])

		return leaders


	def _update_leaderboard(self, url, hitCount):
		urlIndex = -1
		for i in xrange(self._windowSize):
			if self._leaders[i][0] == url:
				self._leaders[i][1] = hitCount
				urlIndex = i
				break

		if urlIndex == -1:
			if self._leaders[-1][1] == -1 or self._leaders[-1][1] < hitCount:
				self._leaders[-1][0] = url
				self._leaders[-1][1] = hitCount
				urlIndex = self._windowSize - 1

		if urlIndex != -1:
			for i in reversed(range(1, urlIndex + 1)):
				if self._leaders[i][1] > self._leaders[i - 1][1]:
					self._leaders[i], self._leaders[i - 1] = self._leaders[i - 1], self._leaders[i]
				else:
					break


	def hit(self, url):
		if not url:
			return 

		if not self._urlDict.has_key(url):
			self._urlDict[url] = 0

		hitCount = self._urlDict[url] + 1
		self._urlDict[url] = hitCount

		self._update_leaderboard(url, hitCount)


'''
Tester codes are written below
'''
if __name__ == "__main__":
	tests = ["", "", "", None, None, "1.com", "1.com", "1.com", "2.com", "2.com", "2.com", "2.com", "2.com",
			"3.com", "4.com", "5.com", "5.com", "4.com", "4.com", "6.com", "7.com", "8.com", "8.com", "9.com", "10.com",
			"11.com", "11.com", "9.com", "12.com", "12.com", "13.com", "13.com", "13.com", "12.com", "12.com", "12.com",
			"12.com", "12.com", "6.com", "2.com", "2.com", "2.com"]

	l = Leaderboard(10)
	print "Leaders:", l.get_leaders()
	for t in tests:
		print "--------------------------------"
		print "Url hit:", t
		l.hit(t)
		print "Leaders:", l.get_leaders()