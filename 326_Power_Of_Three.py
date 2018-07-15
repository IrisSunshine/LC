
# coding: utf-8

# In[ ]:

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divide = 1
        while divide <= n:
            if divide == n : 
            	return True
            divide *= 3
        return False

