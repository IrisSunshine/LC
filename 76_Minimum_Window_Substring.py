
# coding: utf-8

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_1, count_2 = {}, {}
        for letter in t:
            if letter in count_1:
                count_1[letter] += 1
                count_2[letter] += 1
            else:
                count_1[letter] = 1
                count_2[letter] = 1
        
        start = 0
        count = len(t)
        min_size = len(s) + 1
        min_start = 0
        for end in range(len(s)):
            if s[end] in count_1:
                count_2[s[end]] -= 1
                if count_2[s[end]] >= 0:
                    count -= 1
                if count == 0:
                    while True:
                        if s[start] in count_2:
                            if count_2[s[start]] < 0:
                                count_2[s[start]] += 1
                            else:
                                break
                        start += 1
                    if end - start + 1 < min_size:
                        min_size = end - start + 1
                        min_start = start
        if min_size <= len(s):
            return s[min_start:min_start + min_size]
        else:
            return ''
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.minWindow("ADOBECODEBANC", "ABC")
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))