
# coding: utf-8

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in xrange(1, len(s)):
            if s[:i]*(len(s)/i) == s:
                return True
        return False