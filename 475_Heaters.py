
# coding: utf-8

class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        dist = 0
        num = 0
        for i in range(len(houses)):
            d_1 = abs(houses[i] - heaters[num])
            d_2 = abs(houses[i] - heaters[num + 1]) if num < len(heaters) - 1 else 1e9
            if d_2 < d_1:
                num += 1
            dist = max(dist, min(d_1, d_2))
        return dist

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findRadius([1,2,3,4],[1,4])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))