
# coding: utf-8

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not any(strs):
            return []
        
        res = {}
        for string in strs:
            string_0 = ''.join(sorted(string))
            if string_0 in res:
                res[string_0].append(string)
            else:
                res[string_0] = [string]
        
        return [res[x] for x in res]

if __name__ == '__main__':
    from time import time
    sol = Solution()
    t = time()
    ans = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print ('ans: %s\ntime: %.3fms'%(ans,(time() - t) * 1000))