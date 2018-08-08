
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        def build(inorder, postorder):
            if len(inorder) == 0:
                return None
            root = TreeNode(postorder[-1])
            if len(inorder) == 1:
                return root
            r_num = inorder.index(postorder[-1])
            root.left = build(inorder[:r_num], postorder[:r_num])
            root.right = build(inorder[r_num + 1:], postorder[r_num:-1])
            return root
        
        return build(inorder, postorder)