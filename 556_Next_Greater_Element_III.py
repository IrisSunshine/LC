
# coding: utf-8

class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        num = [int(x) for x in str(n)]
        
        i = len(num) - 1
        while i > 0 and num[i] <= num[i-1]:
            i -= 1
        if i <= 0:
            return -1
        
        for j in range(len(num) - 1, i - 1, - 1):
            if num[j] > num[i - 1]:
                break
        num[j], num[i - 1] = num[i - 1], num[j]
        temp = num[:i] + sorted(num[i:])
        ans = int("".join(map(str, temp)))     
        
        if ans > 2147483647:
            return -1
        return ans

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.nextGreaterElement(654323)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))