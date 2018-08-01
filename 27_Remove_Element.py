
# coding: utf-8

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.removeElement( [0,1,2,2,3,0,4,2],2)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))