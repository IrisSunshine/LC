
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        
        def build(t):
            s = str(t.val)
            if t.left:
                s += '(' + build(t.left) + ')'
            elif t.right:
                s += '()'
            if t.right:
                s += '(' + build(t.right) + ')'
            return s
        
        return build(t)
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    a1,a2,a3,a4 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4)
    a1.left, a1.right = a2, a3
    a2.right = a4
    t = time()
    ans = sol.tree2str(a1)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))