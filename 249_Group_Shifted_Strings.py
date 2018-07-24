
# coding: utf-8

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = []
        nums = []
        ans = []
        for i in range(len(strings)):
            word = []
            for j in strings[i]:
                n = ord(j) - ord(strings[i][0])
                word.append(n if n >= 0 else n + 26)
            if word not in dic:
                dic.append(word)
                nums.append([i])
            else:
                a = dic.index(word)
                nums[a].append(i)
        for i in range(len(nums)):
            cat = []
            for j in nums[i]:
                cat.append(strings[j])
            ans.append(cat)
        return ans
    
if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))