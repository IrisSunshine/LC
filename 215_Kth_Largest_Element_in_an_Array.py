
# coding: utf-8

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse = True)[k - 1]
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))