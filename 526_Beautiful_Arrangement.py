
# coding: utf-8

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(num, index, cache):
            if index == 1:
                return 1
            if (index, num) in cache:
                return cache[(index, num)]
            ans = 0
            for i in range(len(num)):
                if num[i] % index == 0 or index % num[i] == 0:
                    ans += helper(num[:i] + num[i + 1:], index - 1, cache)
            cache[(index,num)] = ans
            return ans
        
        if N == 1:
            return 1
        num = tuple(i for i in range(1,N + 1))
        return helper(num, N, {})
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.countArrangement(15)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))