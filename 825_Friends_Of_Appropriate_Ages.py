
# coding: utf-8

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        people = [0] * 120
        count = 0
        for a in ages:
            people[a - 1] += 1
        for i in range(120):
            if people[i]:
                for j in range((i + 1) // 2 + 7, i + 1):
                    if people[j]:
                        if i == j:
                            count += people[i] * (people[i] - 1)
                        else:
                            count += people[i] * people[j]
        return count
            

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.numFriendRequests([16,16])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))