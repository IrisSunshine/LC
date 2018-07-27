
# coding: utf-8

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        candy = [1 for i in range(n) ]
        for i in range(1,n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max((candy[i + 1] + 1),candy[i])
        return sum(candy)
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.candy([1,0,2,3,5,1,0,7,1,33,2,5,-9,7,8,9,0,1])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))