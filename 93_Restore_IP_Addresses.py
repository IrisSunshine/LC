
# coding: utf-8

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        if len(s) < 4:
            return []
        
        res = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if a + b + c + d == len(s):
                            if int(s[:a]) < 256 and (a == 1 or s[0] != '0'):
                                if int(s[a:a + b]) < 256 and (b == 1 or s[a] != '0'):
                                    if int(s[a + b:a + b + c]) < 256 and (c == 1 or s[a + b] != '0'):
                                        if int(s[a + b + c:a + b + c + d]) < 256 and (d == 1 or s[a + b + c] != '0'):
                                            res.append('.'.join([s[:a],s[a:a + b],s[a + b:a + b + c],s[a + b + c:a + b + c + d]]))
        return res
    
if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.restoreIpAddresses("25525511135")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))