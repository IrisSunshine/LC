
# coding: utf-8

class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n == 0 or n == 1:
            return n
        
        envelopes.sort(key = lambda x:(x[0], - x[1]))
        dp = []
        
        for i in range(n):
            left, right = 0, len(dp)
            t = envelopes[i][1]
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < t:
                    left = mid + 1
                else:
                    right = mid
            if right >= len(dp):
                dp.append(t)
            else:
                dp[right] = t

        return len(dp)
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))