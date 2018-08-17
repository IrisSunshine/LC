
# coding: utf-8

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         left = 0
#         right = len(s) - 1
#         while left < right:
            
#             while left < right:
#                 if not s[left].isalnum():
#                     left += 1
#                 else:
#                     break
#             while left < right:
#                 if not s[right].isalnum():
#                     right -= 1
#                 else:
#                     break
#             if s[left].lower() != s[right].lower():
#                 return False
#             left += 1
#             right -= 1
#         return True

        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist[:len(cleanlist) // 2] == cleanlist[:len(cleanlist) // 2:-1]

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.isPalindrome('A man, a plan, a canal: Panama')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))