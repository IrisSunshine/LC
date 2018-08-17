
# coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        node = head
        res = []
        while node:
            res.append(node)
            node = node.next
        left, right = 0, len(res) - 1
        for i in range(len(res) // 2):
            res[left].next = res[right]
            res[right].next = res[left + 1]
            left += 1
            right -= 1
        res[len(res) // 2].next = None
        return head
        
if __name__ == "__main__":
    from time import time
    sol = Solution()
    a1,a2,a3,a4,a5 = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
    a1.next,a2.next,a3.next,a4.next = a2,a3,a4,a5
    t = time()
    ans = sol.reorderList(a1)
    print('time = %.3fms'%((time() - t) * 1000))
    while ans:
        print('%s'%(ans.val), end=' -> ')
        ans = ans.next
    print('None')