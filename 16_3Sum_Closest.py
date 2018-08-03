
# coding: utf-8

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best_sum = nums[0] + nums[1] + nums[-1]
        diff = abs(best_sum - target)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if nums[i] + nums[left] + nums[left + 1] < target or nums[i] + nums[right] + nums[right - 1] > target:
                while left < right:
                    t_sum = nums[i] + nums[left] + nums[right]
                    if t_sum == target:
                        return target
                    if abs(t_sum - target) < diff:
                        best_sum = t_sum
                        diff = abs(t_sum - target)
                    if t_sum > target:
                        right -= 1
                    else:
                        left += 1
        return best_sum
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.threeSumClosest([-1,-1,0], 1)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))