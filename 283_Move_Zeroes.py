
# coding: utf-8

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        nums[j:] = (len(nums) - j) * [0]
        return nums
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.moveZeroes([0,1,0,3,12])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))