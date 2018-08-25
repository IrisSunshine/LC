
# coding: utf-8

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        s = []
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry == 1:
            x = 0 if i < 0 else ord(num1[i]) - ord('0')
            y = 0 if j < 0 else ord(num2[j]) - ord('0')
            s.append(str((x + y + carry) % 10))
            carry = (x + y + carry) // 10
            i -= 1
            j -= 1
        return ''.join(s[::-1])
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.addStrings('123','7890')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))