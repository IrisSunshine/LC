
# coding: utf-8

# In[ ]:

class Solution(object):
    def isMatch(self, s, t):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def d(i, j):
            if (i, j) not in memo:
                if j == len(t):
                    memo[i, j] = (i == len(s))
                else:
                    first_match = i < len(s) and t[j] in {s[i], '.'}
                    
                    if j+1 < len(t) and t[j+1] == '*':
                        ans = d(i,j+2) or first_match and d(i+1, j)
                        memo[i, j] = ans
                    else:
                        ans = first_match and d(i+1, j+1)
                        memo[i, j] = ans
             
            return memo[i, j]

        return d(0,0)

