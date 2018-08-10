
# coding: utf-8

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = 1
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.containsDuplicate([1,2,3,4,5,6,6])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))