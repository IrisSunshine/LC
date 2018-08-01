
# coding: utf-8

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        map_1, map_2 = [0] * 26, [0] * 26
        ord_a = ord('a')
        for i in range(len(s1)):
            map_1[ord(s1[i]) - ord_a] += 1
            map_2[ord(s2[i]) - ord_a] += 1
        if map_1 == map_2:
            return True
        for i in range(len(s2) - len(s1)):
            map_2[ord(s2[i]) - ord_a] -= 1
            map_2[ord(s2[i + len(s1)]) - ord_a] += 1
            if map_1 == map_2:
                return True
        return False
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.checkInclusion("hello","ooolleoooleh")
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))