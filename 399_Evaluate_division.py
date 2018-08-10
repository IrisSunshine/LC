
# coding: utf-8

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """ 
        import collections
        
        def dfs(x, y, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for e in d[x]:
                if e in visited:
                    continue
                visited.add(e)
                c = dfs(e, y, visited)
                if c > 0:
                    return c * d[x][e]
            return -1
                
        d = collections.defaultdict(dict)
        for i in range(len(equations)):
            d[equations[i][0]][equations[i][1]] = values[i]
            d[equations[i][1]][equations[i][0]] = 1.0 / values[i]
        
        ans  =[]
        for j in queries:
            if j[0] in d and j[1] in d:
                ans.append(dfs(j[0], j[1], set()))
            else:
                ans.append(-1.0)
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    equations = [["a","b"],["e","f"],["b","e"]]
    values = [3.4,1.4,2.3]
    queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
    t = time()
    ans = sol.calcEquation(equations, values, queries)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))