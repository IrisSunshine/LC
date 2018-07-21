
# coding: utf-8

class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        possible_1 = nums[:]
        for i in range(len(nums)):
            if i > 0:
                if possible_1[i] > possible_1[i - 1]:
                    possible_1[i] = possible_1[i - 1]
        queue = []
        best = -1e9
        for i in range(len(nums) - 1,0,-1):
            while any(queue) and queue[-1] < nums[i]:
                if queue[-1] > best:
                    best = queue[-1]
                queue.pop()
            queue.append(nums[i])
            if best != -1e9 and possible_1[i - 1] < best:
                return True
        return False
    
if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.find132pattern([-1, 3, 2, 0])
    print ('ans: %s\ntime: %.3fms'%(ans,(time() - t) * 1000))