
# coding: utf-8

class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.bulbSwitch(50)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))