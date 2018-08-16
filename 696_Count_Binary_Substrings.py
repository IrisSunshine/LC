
# coding: utf-8

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        prev, cur = 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                prev = cur
                cur = 1
            else:
                cur += 1
            if cur <= prev:
                ans += 1
        return ans
    
if __name__ =="__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.countBinarySubstrings('11001010')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))