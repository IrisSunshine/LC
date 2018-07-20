
# coding: utf-8

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0: return 
        m = len(board)
        n = len(board[0])
        
        for i in range(m): 
            for j in range(n):
                lives=self.liveNe(board, m, n, i, j)
                
                if board[i][j] == 1 and lives >= 2 and lives <= 3:
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        
        for i in range(m): 
            for j in range(n):
                board[i][j]>>=1

    def liveNe(self, board, m, n, i, j):
        lives = 0
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1): 
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1): 
                lives += board[x][y] & 1;
        
        lives -= board[i][j] & 1
        return lives

if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))