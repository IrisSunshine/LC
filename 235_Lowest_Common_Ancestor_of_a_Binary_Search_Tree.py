
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor = root
        if p.val > q.val:
            p_val, q_val = q.val, p.val
        else:
            p_val, q_val = p.val, q.val
        while ancestor:
            if p_val <= ancestor.val and q_val >= ancestor.val:
                return ancestor
            if p_val > ancestor.val:
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    a1,a2,a3,a4,a5,a6,a7,a8,a9 = TreeNode(6),TreeNode(2),TreeNode(8),TreeNode(0),TreeNode(4),TreeNode(7),TreeNode(9),TreeNode(3),TreeNode(5)
    a1.left, a1.right = a2, a3
    a2.left, a2.right = a4, a5
    a3.left, a3.right = a6, a7
    a5.left, a5.right = a8, a9
    t = time()
    ans = sol.lowestCommonAncestor(a1, a2, a5).val
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))