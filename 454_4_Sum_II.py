
# coding: utf-8

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic_ab = dict()
        dic_cd = dict()
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                s = A[i] + B[j]
                dic_ab[s] = dic_ab.get(s, 0) + 1
        for i in range(len(C)):
            for j in range(len(D)):
                s = C[i] + D[j]
                dic_cd[s] = dic_cd.get(s, 0) + 1
        for key in dic_ab:
            c = dic_cd.get(-key, 0)
            if c:
                ans += c * dic_ab.get(key, 0)
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.fourSumCount([ 1, 2], [-2,-1], [-1, 2], [ 0, 2])
    print ('ans: %s\ntime: %.3fms'%(ans,(time() - t) * 1000))