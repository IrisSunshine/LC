
# coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        
        p1,p2 = [],[]
        n = l1
        digit = 0
        
        while n:
            p1.append(n.val)
            n = n.next
        n = l2
        while n:
            p2.append(n.val)
            n = n.next
        next_0 = None
        while len(p1) or len(p2):
            n1 = p1.pop() if len(p1) else 0
            n2 = p2.pop() if len(p2) else 0
            node = ListNode((digit + n1 + n2) % 10)
            digit = (digit + n1 + n2) // 10
            node.next = next_0
            next_0 = node
        if digit:
            node = ListNode(digit)
            node.next = next_0
        return node
    
if __name__ == '__main__':
    from time import time
    sol = Solution()
    a1 = ListNode(7)
    a2 = ListNode(2)
    a3 = ListNode(4)
    a4 = ListNode(3)
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a5 = ListNode(5)
    a6 = ListNode(6)
    a7 = ListNode(4)
    a5.next = a6
    a6.next=a7
    t1 = time()
    ans = sol.addTwoNumbers(a1, a5)
    t2 = time() 
    while ans:
        print (ans.val)
        ans = ans.next