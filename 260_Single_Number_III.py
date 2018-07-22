
# coding: utf-8

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        x_1 = 0
        t = 1
        for i in range(len(nums)):
            x ^= nums[i]
        while t & x == 0:
            t <<= 1
        for i in range(len(nums)):
            if nums[i] & t == 0:
                x_1 ^= nums[i]
        return [x_1,x ^ x_1]
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.singleNumber([1,2,1,3,2,5])
    print('ans = %s\ntime = %sms'%(ans,(time() - t) * 1000))