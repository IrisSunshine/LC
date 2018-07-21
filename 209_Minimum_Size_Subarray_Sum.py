
# coding: utf-8

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not any(nums):
            return 0
        
        sums = sum(nums)
        if sums < s:
            return 0
        
        right = -1
        ans = 1e9
        sums = 0
        
        for left in range(len(nums)):                    
            if right <= left:
                sums = nums[left]
                right = left
            if left > 0:
                sums -= nums[left - 1]
            while right < len(nums) - 1 and sums < s:
                right += 1
                sums += nums[right]
            if sums < s and ans == 1e9:
                return 0
            if sums >= s:
                ans = min(ans,right - left + 1)
        return ans

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.minSubArrayLen(7,[2,3,1,2,4,3])
    print('ans = %s\ntime = %.3fms'%(ans,(time() - t) * 1000))