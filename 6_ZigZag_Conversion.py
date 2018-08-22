
# coding: utf-8

# In[ ]:

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        goDown = False
        curRows = 0
        rows = [''] * min(len(s), numRows)

        for i in range(len(s)):
            rows[curRows] += s[i]
            if curRows == 0 or curRows == numRows -1:
                goDown = not goDown
            curRows += 1 if goDown else -1
        ans = ''
        for row in rows:
            ans += row
            
        return ans

