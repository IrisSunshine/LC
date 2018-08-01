
# coding: utf-8

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        ans = 0
        ord_A = ord('A')
        for i in range(l):
            ans += (ord(s[i]) - ord_A + 1) * ( 26 ** (l - i - 1))
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.titleToNumber('ZY')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))