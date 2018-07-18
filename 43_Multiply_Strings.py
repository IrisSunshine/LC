
# coding: utf-8

# In[9]:

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        pos = [0] * (len1 + len2)
        n_0 = ord('0')
        ans = 0
        ansc = []
        
        for i in range(len2 - 1,-1,-1):
            for j in range(len1-1,-1,-1):
                #p = len1 + len2 - i - j - 2
                p = i + j + 1
                mult = (ord(num2[i]) - n_0) * (ord(num1[j]) - n_0)
                pos[p] += mult
        
        for k in range(len1 + len2):
            ans *= 10
            ans += pos[k]
            
        while ans != 0:
            ansc.insert(0, chr(ans % 10 + n_0))
            ans //= 10
            
        return ''.join(ansc)
            
if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.multiply("123", "456")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

