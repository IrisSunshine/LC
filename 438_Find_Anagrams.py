
# coding: utf-8

# In[ ]:

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(s) < len(p):
            return []
        res = []
        len_s = len(s)
        len_p = len(p)
        
        c={}
        for ch in p:
            c[ch] = c.get(ch, 0) + 1

        for j in range (len_p - 1):
            c[s[j]] -= 1

        for i in range (len_s - len_p + 1):
            if s[i + len_p -1] not in c:
                c[s[i + len_p -1]] = 0
            c[s[i + len_p -1]] -= 1
            if not any(c.values()):
                res.append(i)
            c[s[i]] += 1
            
        return res
    
    
if __name__ == '__main__':
    sol = Solution()
    s = 'cbaebabacd'
    p =  'abc'
    print (sol.findAnagrams(s,p))

