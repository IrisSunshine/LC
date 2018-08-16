
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root, sum):
            if root == None:
                return None
            helper(root.right, sum)
            root.val += self.sum
            self.sum = root.val
            helper(root.left, sum)
            
        self.sum = 0
        helper(root, 0)
        return root