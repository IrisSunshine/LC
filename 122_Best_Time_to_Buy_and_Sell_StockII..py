
# coding: utf-8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(1, len(prices)):
            ret += max(0, prices[i] - prices[i - 1])
        return ret