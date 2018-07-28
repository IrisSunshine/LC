
# coding: utf-8

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        d = x ^ y
        ans = 0
        for i in range(32):
            ans += 1 & d
            d >>= 1
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.hammingDistance(1,4)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))