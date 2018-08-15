
# coding: utf-8

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(word):
            left, right = 0, len(word)-1
            while left < right:
                if word[left] != word[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
    
        res = list()
        hamp = dict()
        for i, word in enumerate(words):
            hamp[word[::-1]] = i
            
        for i, word in enumerate(words):
            if '' in hamp and word and isPalindrome(word):
                res.extend([[i, hamp['']], [hamp[''], i]])
            if word in hamp and i != hamp[word]:
                res.append([i, hamp[word]])
            for j in range(1, len(word)):
                l, r = word[:j], word[j:]
                if l in hamp and isPalindrome(r):
                    res.append([i, hamp[l]])
                if r in hamp and isPalindrome(l):
                    res.append([hamp[r], i])
        return res
                        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.palindromePairs(["abcd","dcba","lls","s","sssll"])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))