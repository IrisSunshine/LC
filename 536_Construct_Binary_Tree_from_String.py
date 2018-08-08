
# coding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s) == 0:
            return None
        
        def str2tree_helper(s):
            i, sign, num = 0, 1, 0
            if s[0] == '-':
                i, sign = 1, -1
            while i < len(s) and s[i] != '(':
                num = num * 10 + int(s[i])
                i += 1
            root = TreeNode(num)
            if i == len(s):
                return root
            p, j = 1, i
            while p != 0:
                j += 1
                if s[j] == '(':
                    p += 1
                elif s[j] == ')':
                    p -= 1
            root.left = str2tree_helper(s[i + 1:j])
            if j + 2 < len(s):
                root.right = str2tree_helper(s[j + 2:-1])
            return root
                
        return str2tree_helper(s)
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.str2tree('4(2(3)(1))(6(5))')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))