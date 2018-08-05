
# coding: utf-8

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        s_sum, t_sum = 0, ord(t[-1])
        for i in range(len(s)):
            s_sum += ord(s[i])
            t_sum += ord(t[i])
        return chr(t_sum - s_sum)

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findTheDifference('abcd', 'abcde')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))