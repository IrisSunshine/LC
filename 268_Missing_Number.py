
# coding: utf-8

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums) + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.missingNumber([9,6,4,2,3,5,7,0,1])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))