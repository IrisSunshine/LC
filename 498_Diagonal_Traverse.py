
# coding: utf-8

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        if not n:
            return []
        ans = []
        x, y, k = 0, 0, 1
        for i in range(m * n):
            ans.append(matrix[y][x])
            if k > 0:
                dx, dy = x + 1, y - 1
            else:
                dx, dy = x - 1, y + 1
            if dx < n and dx >= 0 and dy < m and dy >=0:
                x, y = dx, dy
            else:
                if k > 0:
                    if x + 1 < n:
                        x += 1
                    else:
                        y += 1
                else:
                    if y + 1 < m:
                        y += 1
                    else:
                        x += 1
                k *= -1
        return ans

if __name__ == "__main__":
    from time import time
    sol = Solution()
    matrix = [[ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]]
    t = time()
    ans = sol.findDiagonalOrder(matrix)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))