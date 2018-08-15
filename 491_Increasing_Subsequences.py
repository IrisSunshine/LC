
# coding: utf-8

class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         def dfs(nums, index, res, temp):
#             if len(temp) >= 2 and temp not in res:
#                 res.append(temp.copy())
#             for i in range(index, len(nums)):
#                 if not temp or temp[-1] <= nums[i]:
#                     temp += [nums[i]]
#                     dfs(nums, i + 1, res, temp)
#                     temp.pop()
        
#         ans = []
#         if len(nums) == 0 or len(nums) == 1:
#             return ans
#         dfs(nums, 0, ans, [])
#         return ans

        dp = set()
        for num in nums:
            for x in list(dp):
                if num >= x[-1]:
                    dp.add(x + (num,))
            dp.add((num,))
        return list(x for x in dp if len(x) > 1)
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findSubsequences([4, 6, 7, 7])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))