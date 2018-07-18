
# coding: utf-8

# In[3]:

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = [0] * 26
        ord_a = ord('a')
        
        for i in range(len(s)):
            dic[ord(s[i]) - ord_a] += 1
            
        for i in range(len(s)):
            if dic[ord(s[i]) - ord_a] == 1:
                return i
        return -1
    
if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.firstUniqChar("loveleetcode")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))


# In[ ]:



