
# coding: utf-8

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def TakeMaxium(i, j,dp):
            if (i, j) not in dp:
                if i == j:
                    return nums[i]
                dp[i,j] = max((nums[i] - TakeMaxium(i + 1, j, dp)), (nums[j] - TakeMaxium(i, j - 1, dp)))
            return dp[i, j]
        
        dp = {}
        return (TakeMaxium(0, len(nums)-1, dp) >= 0)

    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.PredictTheWinner([3,100,1,2])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))