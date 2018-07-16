
# coding: utf-8

# In[ ]:

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cs = set(s)
        dic = {}
        res = []
        for c in s:
            dic[c] = dic.get(c, 0) + 1
            
        for c in s:
            if c in cs:
                while len(res) and c < res[-1] and dic[res[-1]] > 0:
                    cs.add(res.pop())
                res.append(c)
                cs.remove(c)
            dic[c] -= 1
        return ''.join(res)

if __name__ == '__main__':
    sol = Solution()
    s = "cbcdcbca"
    print (sol.removeDuplicateLetters(s))

