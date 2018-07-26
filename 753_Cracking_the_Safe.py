
# coding: utf-8

class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        goal = k ** n
        init = "0" * n
        self.ans = init
        vis = set()
        vis.add(init)
        self.DFS(init, n, k, goal,vis)
        return self.ans
        
    def DFS(self, init, n, k, goal, visit):
        if len(visit) == goal:
            self.ans = init
            return True
        l = len(init)
        for i in range(k):
            e = init[l - n + 1: l] + str(i)
            if e not in visit:
                visit.add(e)
                init += str(i)
                if self.DFS(init, n, k, goal, visit):
                    return True
                visit.remove(e)
                init = init[: -1]
                
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.crackSafe(3,4)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))