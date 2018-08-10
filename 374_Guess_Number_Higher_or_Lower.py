
# coding: utf-8

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left, right = 1, n
        while left < right:
            ans = (left + right) // 2
            flag = guess(ans)
            if flag == 0:
                return ans
            elif flag == 1:
                left = ans + 1
            else:
                right = ans - 1
        return left