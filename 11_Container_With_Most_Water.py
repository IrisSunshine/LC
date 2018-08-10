
# coding: utf-8

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                new_water = height[left] * (right - left)
                left += 1
            else:
                new_water = height[right] * (right - left)
                right -= 1
            if water < new_water:
                water = new_water
        return water
                
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.maxArea([1,2])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))