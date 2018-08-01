
# coding: utf-8

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        is_prime = [1] * n
        is_prime[0], is_prime[1] = 0, 0
        from math import sqrt
    
        for p in range(2, int(sqrt(n)) + 1):
            if is_prime[p]:
                is_prime[p * p: n: p] = [0] * ((n - 1) // p - p + 1)
        return sum(is_prime)
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.countPrimes(10)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))