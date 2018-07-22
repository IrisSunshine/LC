
# coding: utf-8

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.singleNumber([4,1,2,1,2])
    print('ans = %s\ntime = %.3fms'%(ans,(time() - t) * 1000))