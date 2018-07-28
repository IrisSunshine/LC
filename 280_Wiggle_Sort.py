
# coding: utf-8

class Solution(object):
    def wiggleSort (self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if i % 2:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.wiggleSort([3, 5, 2, 1, 6, 4])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))