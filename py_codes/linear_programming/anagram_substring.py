#!/usr/bin/env python

def areOccArrEqual(word1_occ, word2_occ, k):
	for i in xrange(k):
		if word1_occ[i] != word2_occ[i]:
			return False
	return True


def hasSubstring(word1, word2):
	if len(word1) < len(word2):
		return False

	word2_occ = [0] * 256
	for c in word2:
		word2_occ[ord(c)] += 1
	
	word1_occ = [0] * 256
	for i in xrange(len(word2)):
		word1_occ[ord(word1[i])] += 1
	
	i, j = 0, len(word2) - 1
	while True:
		if areOccArrEqual(word1_occ, word2_occ, 256):
			return True
		
		j += 1
		if j == len(word1):
			return False

		word1_occ[ord(word1[i])] -= 1
		i += 1		
		word1_occ[ord(word1[j])] += 1


if __name__ == "__main__":
	tests = [
		("", ""),
		("", " "),
		("", "a"),
		("", "av"),
		("", "adax"),
		(" ", ""),
		("  ", ""),
		("a", ""),
		("ab", ""),
		("aba", "a"),
		("asa", "b"),
		("kaa", "k"),
		("aka", "k"),
		("aak", "k"),
		("arkt", "ar"),
		("arkt", "kr"),
		("arkt", "rk"),
		("arkt", "kt"),
		("arkt", "tk"),
		("arkt", "rb"),
		("sadad", "ada"),
		("sadad", "asd"),
		("sadad", "add"),
		("sadad", "aaa"),
		("lazimlik", "azimli"),
		("lazimlik", "azl"),
		("lazimlik", "ilk"),
		("lazimlik", "iilk"),
		("sedat", "ades"),
		("sedat", "adet"),
		("sedat", "adrt"),
		("salam", "lasam"),
		("kasam", "aksam"),
		("kasam", "cksam"),
	]

	for t in tests:
		print t, hasSubstring(t[0], t[1])