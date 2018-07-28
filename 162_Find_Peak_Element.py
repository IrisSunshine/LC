
# coding: utf-8

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right =0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findPeakElement([1,2,1,3,5,6,4])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))