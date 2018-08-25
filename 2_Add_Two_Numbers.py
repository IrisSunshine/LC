
# coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1, c2 = l1, l2
        head = ListNode(0)
        d = head
        sums = 0
        while c1 or c2:
            sums //= 10
            if c1:
                sums += c1.val
                c1 = c1.next
            if c2:
                sums += c2.val
                c2 = c2.next
            d.next = ListNode(sums % 10)
            d = d.next
        if sums // 10 == 1:
            d.next = ListNode(1)
        return head.next

if __name__ == "__main__":
    sol = Solution()
    a1,a2,a3 = ListNode(2),ListNode(4),ListNode(3)
    b1,b2,b3 = ListNode(5),ListNode(6),ListNode(4)
    a1.next,a2.next,b1.next,b2.next = a2,a3,b2,b3
    ans = sol.addTwoNumbers(a1,b1)
    s = ''
    while ans:
        s += str(ans.val)
        ans = ans.next
    print(s[::-1])