
# coding: utf-8

class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        
        if k == 0:
            for i in range(len(nums)):
                if i == len(nums) - 1:
                    return False
                if nums[i] == 0:
                    if nums[i + 1] == 0:
                        return True
        
        sum_seen = set()
        sum_now = 0
        for i in range(len(nums)):
            sum_now = (sum_now + nums[i]) % k
            if i:
                if sum_now == 0 or sum_now in sum_seen:
                    return True
            sum_seen.add(sum_now)

        return False
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.checkSubarraySum([0,0,3],0)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))