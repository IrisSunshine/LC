
# coding: utf-8

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def Combination(m, n):
            a, b = 1, 1
            m_0 = min(m, n - m)
            for i in range(n - m_0):
                a *= (n - i)
                b *= (n - m_0 - i)
            return int(a / b)
        
        ans = 0
        for i in range(n - n // 2, n + 1):
            num_2 = n - i
            ans += Combination(num_2, i)
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.climbStairs(4)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))