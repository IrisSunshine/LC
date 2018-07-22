
# coding: utf-8

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        after = []
        state = []
        cur = []
        for i in range(numCourses):
            after.append([])
            state.append(0)
        #after = [[] for numCourse in range(numCourses)]
        for i in range(len(prerequisites)):
            after[prerequisites[i][1]].append(prerequisites[i][0])
            state[prerequisites[i][0]] += 1
        for i in range(numCourses):
            if state[i] == 0 :
                cur.append(i)
        while len(ans) < numCourses:
            if len(cur) > 0:
                p = cur.pop()
                ans.append(p)
                for i in range(len(after[p])):
                    state[after[p][i]] -= 1
                    if state[after[p][i]] == 0:
                        cur.append(after[p][i])
            else:
                return []
        return ans
    
if __name__ =="__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))