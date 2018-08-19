
# coding: utf-8

import collections
import heapq

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = dict()
        for i in range(len(words)):
            if dic.__contains__(words[i]) == False:
                dic[words[i]] = 1
            else:
                dic[words[i]] += 1
        heap = [[-dic[key], key] for key in dic.keys()]
        ans = list()
        heapq.heapify(heap)
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    t = time()
    ans = sol.topKFrequent(words, 4)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))