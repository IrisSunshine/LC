
# coding: utf-8

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         def isPalindrome(s):
#             left, right = 0, len(s) - 1
#             while left < right:
#                 if s[left] != s[right]:
#                     return False
#                 left += 1
#                 right -= 1
#             return True
        
#         left, right = 0, len(s) - 1
#         while left < right:
#             if s[left] != s[right]:
#                 return isPalindrome(s[left:right]) or isPalindrome(s[left + 1:right + 1])
#             left += 1
#             right -= 1
#         return True

        if s == s[::-1]:
            return True
        reverse = s[::-1]
        for i in range(len(s)):
            if s[i] != reverse[i]:
                new_s = s[:i] + s[i + 1:]
                new_reverse = reverse[:i] + reverse[i + 1:]
                return new_s == new_s[::-1] or new_reverse == new_reverse[::-1]
        return False
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.validPalindrome('ebcbbececabbacecbbcbe')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))