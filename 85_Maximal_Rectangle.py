
# coding: utf-8

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        max_area = 0
        heights = [0] * (n + 1)
        
        for row in range(m):
            for j in range(n):
                if matrix[row][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            index = []
            for i in range(n + 1):
                while len(index) != 0 and heights[index[-1]] > heights[i]:
                    h = heights[index.pop()]
                    sidx = -1 if len(index) == 0 else index[-1]
                    area = h * (i - sidx - 1)
                    if area > max_area:
                        max_area = area
                index.append(i)
        
        return max_area
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    t = time()
    ans = sol.maximalRectangle(matrix)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))