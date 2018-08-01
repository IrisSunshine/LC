
# coding: utf-8

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)
                
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.hIndex([3,0,6,1,5])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))