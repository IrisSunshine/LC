
# coding: utf-8

class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(graph, group, cur, flag):
            group[cur] = flag
            for x in graph[cur]:
                if group[x] != 0 and group[x] == flag:
                    return False
                if group[x] == 0 and not dfs(graph, group, x, - flag):
                    return False
            return True
        
        group = [0] * len(graph)
        for cur in range(len(graph)):
            if group[cur] == 0:
                if not dfs(graph, group, cur, 1):
                    return False
        return True

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))