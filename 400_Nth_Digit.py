
# coding: utf-8

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = len(str(n))
        c = n
        for i in range(1, l):
            c -= 10 ** (i - 1) * 9 * i
        num, digit = c // l + 10 ** ( l - 1) - 1, c % l
        return str(num)[digit - 1]
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findNthDigit(876)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))