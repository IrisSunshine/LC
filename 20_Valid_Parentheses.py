
# coding: utf-8

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = []
        for x in s:
            if x in ['(','[','{']:
                p.append(x)
            elif x == ')':
                if len(p) == 0 or p[-1] != '(':
                    return False
                p.pop()
            elif x == ']':
                if len(p) == 0 or p[-1] != '[':
                    return False
                p.pop()
            elif x == '}':
                if len(p) == 0 or p[-1] != '{':
                    return False
                p.pop()
            else:
                return False
        return len(p) == 0
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.isValid('')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))