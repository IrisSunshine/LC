
# coding: utf-8

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        maxium = m + n
        ans = [[maxium for i in range(n)] for j in range(m)]
        flag = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                    flag = 0
        if flag:
            return[[-1 for i in range(n)] for j in range(m)]
        flag = 1
        while flag:
            flag = 0
        for i in range(m):
            up = max((i - 1),0)
            down = min((i + 1),(m - 1))
            for j in range(n):
                left = max((j - 1),0)
                right = min((j + 1),(n - 1))
                if ans[i][j] >= maxium:
                    ans[i][j] = min(ans[up][j],ans[down][j],ans[i][left],ans[i][right]) + 1
                if ans[i][j] >= maxium:
                    flag = 1
        return ans

if __name__ == '__main__':
    from time import time
    sol = Solution()
    ipt = [[0, 0, 0], [0, 1, 0],[1, 1, 1]]
    t = time()
    ans = sol.updateMatrix(ipt)
    print('time: %.3fms'%((time() - t) * 1000))
    print('input:')
    for i in range(len(ipt)):
        print(ipt[i])
    print('ans:')
    for i in range(len(ans)):
        print(ans[i])