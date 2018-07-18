
# coding: utf-8

# In[5]:

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        tail = len(gas) - 1
        start = 0
        tank = gas[tail] - cost[tail]
        
        while start < tail:
            if tank >= 0:
                tank += gas[start] - cost[start]
                start += 1
            else:
                tail -= 1
                tank += gas[tail] - cost[tail]
                
        if tank < 0: start = -1

        return start
        
        
if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))


# In[ ]:



