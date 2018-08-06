
# coding: utf-8

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif mid == 0 or nums[mid] != nums[mid - 1]:
                return nums[mid]
            else:
                right = mid - 1
                
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.singleNonDuplicate([3,3,7,7,10,11,11])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))