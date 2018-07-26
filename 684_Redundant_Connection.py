
# coding: utf-8

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        for i in range(len(edges) - 1, 0, -1):
            visited = []
            visited.append(edges[0][0])
            visited.append(edges[0][1])
            e = [0 for k in range(len(edges))]
            e[0], e[i] = 1, 1
            while 0 in e:
                count = 0
                for j in range(1,len(edges)):
                    if e[j] == 0:
                        f_0 = edges[j][0] in visited
                        f_1 = edges[j][1] in visited
                        if f_0 or f_1:
                            if not f_0:
                                visited.append(edges[j][0])
                            if not f_1:
                                visited.append(edges[j][1])
                            e[j] = 1
                            count += 1
                if count == 0:
                    break
            if len(visited) == len(edges):
                return edges[i]
        return -1
                    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findRedundantConnection([[1,2], [3,4], [2,3], [1,4], [1,5]])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))