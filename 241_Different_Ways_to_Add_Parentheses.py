
# coding: utf-8

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        def dfs(s, cache):
            ops = {'+':lambda x,y:x + y, '-':lambda x,y:x - y, '*':lambda x,y:x * y}
            if s not in cache:
                ret = []
                for i in range(len(s)):
                    if s[i] in ['+','-','*']:
                        for left in dfs(s[0:i], cache):
                            for right in dfs(s[i + 1:], cache):
                                ret.append(ops[s[i]](left, right))
                if len(ret) == 0:
                    ret.append(int(s))
                cache[s] = ret
            return cache[s]
        
        return dfs(input, {})
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.diffWaysToCompute('2*3-4*5')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))