
# coding: utf-8

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = []
        word = []
        for i in range(len(s)):
            word.append(s[i])
            if s[i] in ['a','e','i','o','u']:
                vowel.append(s[i])
        c = len(vowel) - 1
        for i in range(len(word)):
            if word[i] in ['a','e','i','o','u']:
                word[i] = vowel[c]
                c -= 1
        return ''.join(word)

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.reverseVowels('hello')
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))