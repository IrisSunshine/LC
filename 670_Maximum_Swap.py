
# coding: utf-8

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = [int(x) for x in str(num)]
        n_1 = sorted(n, reverse = True)
        for i in range(len(n)):
            if n[i] != n_1[i]:
                temp = n[i]
                n[len(n) - n[::- 1].index(n_1[i]) - 1] = temp
                n[i] = n_1[i]
                break
        return int(''.join([str(x) for x in n]))
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.maximumSwap(98368)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))   