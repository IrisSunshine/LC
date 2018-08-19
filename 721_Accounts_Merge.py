
# coding: utf-8

import collections

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                graph[email].append(i)
        visited = [False] * len(accounts)

        def dfs(idx, emails):
            if visited[idx]: return
            visited[idx] = True
            for email in accounts[idx][1:]:
                emails.add(email)
                for node in graph[email]:
                    dfs(node, emails)

        ans = []
        for i, account in enumerate(accounts):
            if visited[i]: continue
            name, emails = accounts[i][0], set()
            dfs(i, emails)
            ans.append([name] + sorted(emails))
        return ans
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
                ["John", "johnnybravo@mail.com"], 
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
                ["Mary", "mary@mail.com"]]
    t = time()
    ans = sol.accountsMerge(accounts)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))