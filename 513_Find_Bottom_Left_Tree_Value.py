
# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level, level_1 = [root], []
        while 1:
            for i in range(len(level)):
                if level[i].left:
                    level_1.append(level[i].left)
                if level[i].right:
                    level_1.append(level[i].right)
            if len(level_1) == 0:
                break
            level, level_1 = level_1, []
        return level[0].val
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    a1,a2,a3,a4,a5,a6,a7 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(6),TreeNode(7)
    a1.left, a1.right = a2, a3
    a2.left = a4
    a3.left, a3.right = a5, a6
    a5.left = a7
    t = time()
    ans = sol.findBottomLeftValue(a1)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))