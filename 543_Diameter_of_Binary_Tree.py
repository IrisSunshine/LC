
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, max_d):
            if not node:
                return 0
            depth_left, depth_right = 0, 0
            if node.left:
                depth_left = helper(node.left, max_d) + 1
            if node.right:
                depth_right = helper(node.right, max_d) + 1
            if depth_left + depth_right > max_d[0]:
                max_d[0] = depth_left + depth_right
            return max(depth_left, depth_right)
            
        if not root:
            return 0
        max_d = [0]
        helper(root, max_d)
        return max_d[0]
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    a1,a2,a3,a4,a5 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5)
    a1.left, a1.right = a2, a3
    a2.left, a2.right = a4, a5
    t = time()
    ans = sol.diameterOfBinaryTree(a1)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))