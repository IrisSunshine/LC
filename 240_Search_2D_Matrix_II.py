
# coding: utf-8

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r, c = len(matrix) -1, 0
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            if target == matrix[r][c]:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False
                
if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print (sol.searchMatrix(matrix, target))