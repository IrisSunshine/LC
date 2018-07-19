
# coding: utf-8

# In[7]:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        res = []
        level_0 = [root]
        level = [root]
        level_val = [root.val]
        
        while level:
            res.append(level_val)
            level_0 = level
            level = []
            level_val = []
            for k in range(len(level_0)):
                if level_0[k].left:
                    level.append(level_0[k].left)
                    level_val.append(level_0[k].left.val)
                if level_0[k].right:
                    level.append(level_0[k].right)
                    level_val.append(level_0[k].right.val)

        return res
    
if __name__ == '__main__':
    from time import time
    
    a1 = TreeNode(3)
    a2 = TreeNode(9)
    a3 = TreeNode(20)
    a4 = TreeNode(15)
    a5 = TreeNode(7)
    a1.left = a2
    a1.right = a3
    a3.left = a4
    a3.right = a5

    sol = Solution()
    t = time()
    ans = sol.levelOrder(a1)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))


# In[ ]:



