
# coding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            for i in range(start, end + 1):
                left_child = helper(start, i - 1)
                right_child = helper(i + 1, end)
                for l_c in left_child:
                    for r_c in right_child:
                        root = TreeNode(i)
                        root.left = l_c
                        root.right = r_c
                        res.append(root)
            return res
        
        if n == 0:
            return []
        return helper(1,n)