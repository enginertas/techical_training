#!/usr/bin/env python

def isCharMatched(s_ch, p_ch):
    return p_ch == '.' or s_ch == p_ch

class Solution(object): 
    def _isMatchHelper(self, s_i, p_i):
        if (s_i, p_i) in self._memoized:
            return self._memoized[(s_i, p_i)]
        
        result = None
        if s_i == self._lens and p_i == self._lenp:
            result = True
        elif p_i == self._lenp:
            result = False
        else:
            if (p_i + 1 < self._lenp) and self._p[p_i + 1] == '*':
                if s_i < self._lens and isCharMatched(self._s[s_i], self._p[p_i]) and self._isMatchHelper(s_i + 1, p_i):
                    result = True
                else:
                    result = self._isMatchHelper(s_i, p_i + 2)
            else:
                if s_i < self._lens and isCharMatched(self._s[s_i], self._p[p_i]) and self._isMatchHelper(s_i + 1, p_i + 1):
                    result = True
                else:
                    result = False
        
        self._memoized[(s_i, p_i)] = result
        return result


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self._memoized = {}
        self._s, self._p = s, p
        self._lens, self._lenp = len(s), len(p)
        return self._isMatchHelper(0, 0)


if __name__ == "__main__":
    soln = Solution()

    tests = [
        ["", ""],
        ["sd", ""],
        ["a", ""],
        ["", "c"],
        ["", "c*"],
        ["", "c*c*"],
        ["c", "c*c*"],
        ["cc", "c*c*"],
        ["ccc", "c*c*"],
        ["cac", "c*ac*"],
        ["a", "c*c*"],
        ["ac", "c*c*"],
        ["a", "c*ac*"],
        ["a", "c*.c*"],
        ["a", "c*bc*"],
        ["aa","a"],
        ["aa","aa"],
        ["aaa","aa"],
        ["aa","a*"],
        ["aa",".*"],
        ["ab",".*"],
        ["aab","c*a*b"]
    ]

    test_i = 1
    for s, p in tests:
        print "------------- Test: %s ------------" %test_i
        print "String:", s, " Pattern:", p
        print "Match: ", soln.isMatch(s, p)
        test_i += 1