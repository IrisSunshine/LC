
# coding: utf-8

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #left, right, up, down = 0, 0, 0, 0
        m = [['L', 'R', 'U', 'D'], [0, 0, 0, 0]]
        for e in moves:
            for i in range(4):
                if e == m[0][i]:
                    m[1][i] += 1
        return (m[1][0] == m[1][1] and m[1][2] == m[1][3])
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.judgeCircle('UURDRLDL')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))