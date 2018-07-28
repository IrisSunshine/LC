
# coding: utf-8

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = ['abc', 'def', 'hgi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        letter = ['']
        for i in range(len(digits)):
            num = int(digits[i])
            if num == 1 or num == 0:
                return -1
            temp = [letter.copy() for m in range(len(dic[num - 2]))]
            for j in range(len(dic[num - 2])):
                for k in range(len(letter)):
                    temp[j][k] += dic[num - 2][j]
            letter = []
            for j in range(len(dic[num - 2])):
                letter += temp[j]
        return letter
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.letterCombinations('23')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))