
# coding: utf-8

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        flag = 1 if (dividend < 0) == (divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        mult_divisor = divisor
        mult = 1
        temp = mult_divisor + mult_divisor
        ans = 0
        nums = [[mult_divisor, 1]]
        while dividend >= temp:
            mult_divisor =temp
            mult += mult
            nums.append([mult_divisor, mult])
            temp = mult_divisor + mult_divisor
        ans += mult
        dividend -= mult_divisor
        for i in range(len(nums) - 2, - 1, - 1):
            if dividend > nums[i][0]:
                dividend -= nums[i][0]
                ans += nums[i][1]
            elif dividend == nums[i][0]:
                dividend -= nums[i][0]
                ans += nums[i][1]
                break
        if flag < 0:
            ans = - ans
        return min(max(-2147483648, ans), 2147483647)
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.divide(-2147483648, -1)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))