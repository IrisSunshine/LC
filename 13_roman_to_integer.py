
# coding: utf-8

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = [1,5,10,50,100,500,1000]
        symbol = ['I','V','X','L','C','D','M']
        ans = 0
        for i in range(len(s) - 1):
            try:
                digit = symbol.index(s[i])
                digit_0 = symbol.index(s[i + 1])
            except:
                return -1
            if digit_0 == digit + 1 or digit_0 == digit + 2:
                ans -= nums[digit]
            else:
                ans += nums[digit]
        ans += nums[symbol.index(s[-1])]
        return ans

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.romanToInt('MCMXCIV')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))