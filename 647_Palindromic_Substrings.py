
# coding: utf-8

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
#         count = 0
#         n = len(s)
#         dp = [[0] * n for k in range(n)]
#         for j in range(n):
#             for i in range(j + 1):
#                 dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
#                 if dp[i][j]:
#                     count += 1
#         return count

        n = len(s)
        count = 0
        for mid in range(n * 2 - 1):
            left = mid // 2
            right = left + (mid & 1)
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.countSubstrings('dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))