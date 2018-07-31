
# coding: utf-8

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.numTrees(6)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))