
# coding: utf-8

class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        health = [[1e9 for i in range(n)] for j in range(m)]
        health[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            down = min(i + 1, m - 1)
            for j in range(n - 1, -1, -1):
                right = min(j + 1, n - 1)
                health[i][j] = max((min(health[down][j], health[i][right]) - dungeon[i][j]), 1)
        return health[0][0]

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))