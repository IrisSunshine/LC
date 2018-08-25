
# coding: utf-8

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        l, r = 0, len(s) - 1
        while l < len(s) and s[l] == " ":
            l += 1
        if l > r:
            return False
        while r >= 0 and s[r] == " ":
            r -= 1
        if s[l] == '+' or s[l] == '-':
            l += 1

        n, d, c, e = False, 0, 0, 0
        hrm = {"e", ".", "+", "-"}
        while l <= r:
            if s[l] == " ":
                return False
            if (s[l] < "0" or s[l] > "9") and s[l] not in hrm:
                return False
            if s[l] >= "0" and s[l] <= "9":
                n = True
            elif s[l] == "e":
                if e == 1 or l == r or not n:
                    return False
                e = 1
                n = False
            elif s[l] == '.':
                if d == 1 or e == 1:
                    return False
                d = 1
            elif s[l] == "+" or s[l] == "-":
                if c == 1 or e == 0 or n:
                    return False
                c = 1
            l += 1
        return n
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.isNumber('2e10')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))