
# coding: utf-8

# In[ ]:

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        walker, runner = head, head
        has_circle = False
        while walker and runner and walker.next and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                has_circle = True
                break
        if has_circle:
            cur = head
            while cur != walker:
                cur = cur.next
                walker = walker.next
            return cur
        else:
            return None