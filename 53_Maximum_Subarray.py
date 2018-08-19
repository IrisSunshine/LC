
# coding: utf-8

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))