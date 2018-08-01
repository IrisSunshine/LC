
# coding: utf-8

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, len(s) + 1):
            num = int(s[i - 2: i])
            if 26 >= num >= 11 and num != 20:
                dp[i] = dp[i - 1] + dp[i - 2]
            elif num == 10 or num == 20:
                dp[i] = dp[i - 2]
            elif s[i - 1] != '0':
                dp[i] = dp[i - 1]
            else:
                return 0
        return dp[len(s)]

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.numDecodings('22645')
