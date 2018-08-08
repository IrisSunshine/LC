
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def build(preorder, inorder):
            if len(preorder) == 0:
                return None
            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root
            r_num = inorder.index(preorder[0])
            root.left = build(preorder[1:r_num + 1], inorder[:r_num])
            root.right = build(preorder[r_num + 1:], inorder[r_num + 1:])
            return root
        
        return build(preorder, inorder)