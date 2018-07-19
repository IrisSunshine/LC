
# coding: utf-8

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic and i - dic[nums[i]] <= k:
                return True
            dic[nums[i]] = i
        
        return False
    
if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.containsNearbyDuplicate([1,2,3,1,2,3],2)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))