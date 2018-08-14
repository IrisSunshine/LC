
# coding: utf-8

class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        queue = []
        for log in logs:
            l = log.split(':')
            if l[1] == 'start':
                if queue:
                    ans[queue[-1]] += int(l[2])
                queue.append(int(l[0]))
                ans[int(l[0])] -= int(l[2])
            else:
                queue.pop()
                ans[int(l[0])] += int(l[2]) + 1
                if queue:
                    ans[queue[-1]] -= int(l[2]) + 1
        return ans
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    n = 2
    logs = ["0:start:0",
     "1:start:2",
     "1:end:5",
     "0:end:6"]
    t = time()
    ans = sol.exclusiveTime(n, logs)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))