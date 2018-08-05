
# coding: utf-8

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        for i in range(len(nums)):
            n = abs(nums[i]) - 1
            if nums[n] > 0:
                nums[n] = - nums[n]
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))   