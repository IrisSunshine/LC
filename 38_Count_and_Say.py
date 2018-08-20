
# coding: utf-8

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = '1'
        for i in range(n - 1):
            temp = ''
            count = 0
            mark = nums[0]
            for num in nums:
                if num == mark:
                    count += 1
                else:
                    temp += str(count) + mark
                    count = 1
                    mark = num
            nums = temp + str(count) + mark
        return nums
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.countAndSay(6)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))