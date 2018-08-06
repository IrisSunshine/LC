
# coding: utf-8

class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        ret = []
        for i in range(len(asteroids)):
            if len(ret) == 0 or ret[-1] < 0 or (ret[-1] > 0) == (asteroids[i] > 0):
                ret.append(asteroids[i])
            else:
                while len(ret) and ret[-1] > 0 and ret[-1] < - asteroids[i]:
                    ret.pop()
                if len(ret) == 0 or ret[-1] < 0:
                    ret.append(asteroids[i])
                elif ret[-1] == - asteroids[i]:
                    ret.pop()
        return ret
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.asteroidCollision([2,-1])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))