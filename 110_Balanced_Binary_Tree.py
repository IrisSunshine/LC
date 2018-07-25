
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        if (not root.left) and (not root.right):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        elif (not root.left):
            return self.isBalanced(root.left)
        elif (not root.right):
            return self.isBalanced(root.right)
        else:
            return True
        
    def depth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return max(self.depth(root.left), self.depth(root.left)) + 1
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(2)
    a4 = TreeNode(3)
    a5 = TreeNode(3)
    a6 = TreeNode(4)
    a7 = TreeNode(4)
    a1.left, a1.right = a2, a3
    a2.left, a2.right = a4, a5
    a4.left, a4.right = a6, a7
    t = time()
    ans = sol.isBalanced(a1)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))