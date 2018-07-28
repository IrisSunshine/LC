
# coding: utf-8

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = sum(nums) % 2
        if t:
            return False
        target = sum(nums) // 2
        nums = sorted(nums)

        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        return (dp[target] > 0)
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.canPartition([1,5,11,15])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))