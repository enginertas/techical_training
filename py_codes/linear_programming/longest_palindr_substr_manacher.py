#!/usr/bin/python

class Solution(object):
    def placeSeperator(self, s):
        new_s = ['|'] * (2 * len(s) + 1)
        for i in xrange(len(s)):
            new_s[2 * i + 1] = s[i]
        return new_s
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        max_len, max_st, max_end = 0, -1, -1
        center, right = 0, 0
        new_s = self.placeSeperator(s)
        lps = [0] * len(new_s)
        
        for i in range(1, len(new_s)):
            lh, rh = None, None
            if right > i:
                lps[i] = 0
                lh = i - 1
                rh = i + 1
            else:
                mirror = 2 * center - i
                if lps[mirror] < right - i - 1:
                    lps[i] = lps[mirror]
                    lh = -1
                else:
                    lps[i] = right - i
                    rh = right + 1
                    lh = 2 * i - rh
            
            while lh >= 0 and rh < len(new_s) and new_s[lh] == new_s[rh]:
                lps[i] += 1
                lh -= 1
                rh += 1
                
            if i + lps[i] > right:
                right = i + lps[i]
                center = i
                
            if lps[i] > max_len:
                max_len, max_st, max_end = lps[i], i - lps[i], i + lps[i]
                
        return s[max_st/2:max_end/2]


if __name__ == "__main__":
    tests = [
        None,
        "",
        "a",
        "b",
        "ab",
        "ba",
        "aa",
        "bac",
        "bab",
        "bbb",
        "bba",
        "arpa",
        "atta",
        "ctta",
        "metot",
        "totot",
        "kaale",
        "abcde",
        "calloc",
        "ballad",
        "callac",
        "manekkine",
        "abaciacadacamlt"
    ]

    soln = Solution()
    for t in tests:
        print "Str:", t
        print "Result:", soln.longestPalindrome(t)
        print "---------------------"


