
# coding: utf-8

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        if num >= 1000:
            ans += (num // 1000) * 'M'
            num %= 1000
        if num >= 900:
            ans += 'CM'
            num -= 900
        if num >= 500:
            ans += 'D'
            num -= 500
        if num >= 400:
            ans += 'CD'
            num -= 400
        if num >= 100:
            ans += (num // 100) * 'C'
            num %= 100
        if num >= 90:
            ans += 'XC'
            num -= 90
        if num >= 50:
            ans += 'L'
            num -= 50
        if num >= 40:
            ans += 'XL'
            num -= 40
        if num >= 10:
            ans += (num // 10) * 'X'
            num %= 10
        if num == 9:
            ans += 'IX'
            return ans
        if num >= 5:
            ans += 'V' + (num - 5) * 'I'
            return ans
        if num == 4:
            ans += 'IV'
            return ans
        ans += num * 'I'
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.intToRoman(1999)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))