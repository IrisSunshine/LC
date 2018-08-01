
# coding: utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0, 0]
            rob_left = dfs(root.left)
            rob_right = dfs(root.right)
            rob_to_children = rob_left[0] + rob_right[0]
            rob_to_root = max(rob_left[1] + rob_right[1] + root.val, rob_to_children)
            return [rob_to_root, rob_to_children]
        
        return dfs(root)[0]
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    a0, a1, a2, a3, a4, a5 = TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(3), TreeNode(1)
    a0.left, a0.right = a1, a2
    a1.left, a1.right = a3, a4
    a2.right = a5
    t = time()
    ans = sol.rob(a0)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))