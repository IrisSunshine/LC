
# coding: utf-8

class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l = len(num)
        if l < 3:
            return False
        for i in range(0, (l - 3) // 2 + 1):
            if i > 0 and num[0] == '0':
                return False
            m = min(l - i - 2, (l + i - 1) // 2)
            for j in range(i + 1, m + 1):
                if j > i + 1 and num[i + 1] == '0':
                    break
                a = int(num[0: i + 1])
                b = int(num[i + 1: j + 1])
                num_0 = num[j + 1: l]
                while len(num_0):
                    s = str(a + b)
                    if num_0[0: len(s)] != s:
                        break
                    num_0 = num_0[len(s):]
                    a, b = b, a + b
                if len(num_0) == 0:
                    return True
        return False
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.isAdditiveNumber('198019823962')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))