
# coding: utf-8

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        if len(matrix)==0: return res
        
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd: 
            
            for j in range(colBegin, colEnd + 1): 
                res.append(matrix[rowBegin][j])
            
            rowBegin += 1
   
            for j in range(rowBegin, rowEnd + 1):        
                res.append(matrix[j][colEnd])
            
            colEnd -= 1
            
            if rowBegin <= rowEnd: 
                for j in range(colEnd, colBegin - 1, -1): 
                    res.append(matrix[rowEnd][j])
            rowEnd -= 1
            
            if colBegin <= colEnd:
                for j in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[j][colBegin])
            colBegin += 1
            
        return res

if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))